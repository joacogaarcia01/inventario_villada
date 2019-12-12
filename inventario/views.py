from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.views import View
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from inventario.forms import ItemForm, LabForm
from .models import Item, Lab, Type


class Index(View):

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        labs = Lab.objects.all()
        ctx = {'labs': labs, 'form': LabForm}
        return render(request, 'index.html', ctx)


class LabGet(View):

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        id_type = request.GET.get('type', None)
        lab = Lab.objects.get(id_lab=kwargs['lab_id'])
        if id_type:
            items = Item.objects.filter(id_lab_id=kwargs['lab_id'], id_type=id_type)
        else:
            items = Item.objects.filter(id_lab_id=kwargs['lab_id'])

        types = Type.objects.all()
        ctx = {'items': items, 'lab_id': kwargs['lab_id'], 'lab': lab, 'form': ItemForm, 'types': types}
        return render(request, 'item/list.html', ctx)


class LabCreate(View):

    @method_decorator(staff_member_required)
    def post(self, request, *args, **kwargs):
        form = LabForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lab_list')
        return render(request, 'lab/list.html', {'form': form})

    def get(self, request, *args, **kwargs):
        return redirect('lab_list')


class LabDelete(View):

    @method_decorator(staff_member_required)
    def get(self, request, *args, **kwargs):
        lab_id = kwargs['lab_id']
        lab = Lab.objects.get(pk=lab_id)
        lab.delete()
        return redirect(request.GET.get('next', '/'))


class ItemCreate(View):

    @method_decorator(staff_member_required)
    def post(self, request, *args, **kwargs):
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(request.POST.get('next', '/'))
        return render(request, 'item/list.html', {'form': form})

    def get(self, request, *args, **kwargs):
        return redirect('lab_list')


class ItemDelete(View):

    @method_decorator(staff_member_required)
    def get(self, request, *args, **kwargs):
        item = Item.objects.get(pk=kwargs['item_id'])
        item.delete()
        return redirect(request.GET.get('next', '/'))


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('lab_list')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})
