from django.contrib import admin
from django.urls import include, path

from .views import index, item_list

urlpatterns = [
    path('', index, name='home'),
    path('lab/<int:lab_id>/', item_list, name='item_list'),
]
