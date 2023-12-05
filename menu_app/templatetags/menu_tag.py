from django import template
from django.utils.safestring import mark_safe
from menu_app.models import MenuItem
from django.template.loader import render_to_string

register = template.Library()


@register.simple_tag(takes_context=True)
def render_dict(context, data):
    levels = context['request'].META['PATH_INFO'].split('/')[2:]
    levels = [i for i in levels if i != '']
    context['index_menu'] = True if levels == [''] else False
    menu_name = data

    def test_url(url):
        for i in url:
            if not i.isdigit():
                return False
        return True

    def get_owner(id, owner, db):
        result = {}
        for i in db:
            if i.owner_name == owner:
                result[i.name] = {'url': f'{id}/{i.id}', 'name': i.name, 'id_menu': i.id_menu.id, 'dict': {}}
        return result

    def get_menu(req, base):
        owner = get_owner('','', base)
        end = owner
        for i in req:
            try:
                for q in base:
                    if not req == [''] and int(i) == int(q.id):
                        _ = end[q.name]
                        end[q.name]['dict'] = get_owner(end[q.name]['url'], q.name, base)
                        end = end[q.name]['dict']
            except KeyError:
                pass
        return owner

    def get_data(data):
        text = "<ul>"
        for k, v in data.items():
            text += "<li><a href='/menu/{}{}'>{}</a>".format(v['id_menu'], v['url'], v['name'])
            if isinstance(v["dict"], dict):
                text += get_data(v['dict'])
            text += '</li>'
        text += '</ul>'
        return text

    if test_url(levels[1:]):
        db = list(MenuItem.objects.filter(menu_name=menu_name))
        text = get_data(get_menu(levels[1:], db))
        return render_to_string('menu_template.html', {'data': mark_safe(text), 'name': menu_name})