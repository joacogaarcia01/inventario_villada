from django.http import HttpResponse
from django.shortcuts import render

from .models import Item, Lab

def index(request):
    labs = Lab.objects.all()
    ctx = {'labs': labs}
    return render(request, 'index.html', ctx)

def item_list(request, lab_id):
    items = Item.objects.filter(id_lab_id=lab_id)
    ctx = {'items': items}
    return render(request, 'item/list.html', ctx)
