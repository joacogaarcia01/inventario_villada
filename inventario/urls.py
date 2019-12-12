from django.contrib import admin
from django.urls import include, path

from inventario.views import Index, LabGet, LabCreate, LabDelete, ItemDelete, ItemCreate

urlpatterns = [
    path('lab/', Index.as_view(), name='lab_list'),
    path('lab/create/', LabCreate.as_view(), name='lab_create'),
    path('lab/<int:lab_id>/', LabGet.as_view(), name='lab_detail'),
    path('lab/<int:lab_id>/delete', LabDelete.as_view(), name='lab_delete'),
    path('lab/<int:lab_id>/create/', ItemCreate.as_view(), name='item_create'),
    path('item/<int:item_id>/delete', ItemDelete.as_view(), name='item_delete'),
]
