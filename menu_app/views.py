from django.views.generic import TemplateView
from .models import MenuItem, MenuList
import json
from django.shortcuts import redirect
from django.conf import settings


def index_redirect(request):
    return redirect('menu/')


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if not MenuList.objects.exists():
            with open(str(settings.BASE_DIR)+'/MenuList.json', 'r') as f:
                data = json.load(f)
            for item in data:
                MenuList.objects.create(name=item['name'])

        if not MenuItem.objects.exists():
            with open(str(settings.BASE_DIR)+'/MenuItem.json', 'r') as f:
                data = json.load(f)
            for item in data:
                MenuItem.objects.create(id_menu_id=item['id_menu_id'],
                                        menu_name=item['menu_name'],name=item['name'],
                                        owner_id_id=item['owner_id_id'], owner_name=item['name'])

            MenuItem.objects.all().update(owner_name='')
            menu_items = MenuItem.objects.all()
            for menu_item in menu_items:
                if menu_item.owner_id:
                    owner_name = MenuItem.objects.get(id=menu_item.owner_id.id).name
                    menu_item.owner_name = owner_name
                    menu_item.save()

        return context
