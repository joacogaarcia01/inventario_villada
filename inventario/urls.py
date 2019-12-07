from django.contrib import admin
from django.urls import include, path

from .views import Index, LabDelete, item_list, create_object

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('delete/<int:lab_id>/', LabDelete.as_view(), name='lab_delete'),
    path('objecto/', create_object, name='create_object'),
    path('lab/<int:lab_id>/', item_list, name='item_list'),
]
