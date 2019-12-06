from django.contrib import admin
from django.urls import include, path

from .views import create_lab, index, item_list, create_object

urlpatterns = [
    path('', index, name='home'),
    path('test/', create_lab, name='create_lab'),
    path('objecto/', create_object, name='create_object'),
    path('lab/<int:lab_id>/', item_list, name='item_list'),

]
