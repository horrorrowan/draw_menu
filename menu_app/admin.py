from django.contrib import admin
from .models import MenuList, MenuItem

# Создаем класс администратора для модели MenuItem
class YourModelAdmin(admin.ModelAdmin):
   # Поля, которые будут доступны только для чтения в административном интерфейсе
   readonly_fields = ('menu_name','owner_name',)

   # Переопределяем метод сохранения модели
   def save_model(self, request, obj, form, change):
       # Если поле menu_name пустое, устанавливаем его значение равным name объекта id_menu
       if not obj.menu_name:
           obj.menu_name = obj.id_menu.name
       # Если поле owner_name пустое и есть имя владельца, устанавливаем его значение равным имени владельца
       try:
           if not obj.owner_name and obj.owner_id.name:
               obj.owner_name = obj.owner_id.name
       # Если у объекта нет атрибута owner_id, пропускаем исключение
       except AttributeError:
           pass
       # Сохраняем объект, вызывая метод родительского класса
       super().save_model(request, obj, form, change)

# Регистрируем модели в административном интерфейсе
admin.site.register(MenuList)
admin.site.register(MenuItem, YourModelAdmin)
