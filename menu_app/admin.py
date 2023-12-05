from django.contrib import admin
from .models import MenuList, MenuItem


class YourModelAdmin(admin.ModelAdmin):
    readonly_fields = ('menu_name','owner_name',)

    def save_model(self, request, obj, form, change):
        if not obj.menu_name:
            obj.menu_name = obj.id_menu.name
        try:
            if not obj.owner_name and obj.owner_id.name:
                obj.owner_name = obj.owner_id.name
        except AttributeError:
            pass
        super().save_model(request, obj, form, change)


admin.site.register(MenuList)
admin.site.register(MenuItem, YourModelAdmin)
