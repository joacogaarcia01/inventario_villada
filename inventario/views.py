from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import View

from .models import Item, Lab


class Index(View):

    def get(self, request):
        print(request.method)
        labs = Lab.objects.all()
        ctx = {'labs': labs}
        return render(request, 'index.html', ctx)

    def post(self, request):
        name = request.POST['name']
        lab = Lab(name=name)
        lab.save()
        return redirect('index')


class LabDelete(View):

    def get(self, request, *args, **kwargs):
        lab_id = kwargs['lab_id']
        lab = Lab.objects.get(pk=lab_id)
        lab.delete()
        return redirect('index')


def item_list(request, lab_id):
    items = Item.objects.filter(id_lab_id=lab_id)
    ctx = {'items': items, "lab_id": lab_id}
    return render(request, 'item/list.html', ctx)

def create_object(request):
    name = request.POST['name']
    lab_id = request.POST["lab_id"]
    lab = Lab.objects.get(pk= lab_id)
    obj = Item(name=name, id_lab=lab)
    obj.save()
    return redirect('/')
