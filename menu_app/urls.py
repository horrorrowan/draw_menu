from django.urls import path, re_path
from .views import *


urlpatterns = [
    path('', index_redirect, name="index"),
    re_path(r'^menu/', IndexView.as_view(), name='index'),
    re_path(r'^menu/\d+(?:/\d+)*$', IndexView.as_view(), name="index"),
]
