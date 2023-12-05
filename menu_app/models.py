from django.db import models


class MenuList(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=50)


class MenuItem(models.Model):
    def __str__(self):
        return self.name

    id_menu = models.ForeignKey(MenuList, on_delete=models.CASCADE, related_name='id_item')
    menu_name = models.CharField(max_length=50, blank=True)
    name = models.CharField(max_length=50)
    owner_id = models.ForeignKey('self', on_delete=models.DO_NOTHING, related_name='ownerid', blank=True, null=True)
    owner_name = models.CharField(max_length=50, blank=True)
