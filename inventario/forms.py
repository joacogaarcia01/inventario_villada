from django.forms import ModelForm, HiddenInput, SelectDateWidget, SplitDateTimeWidget
from .models import Lab, Type, Item


class LabForm(ModelForm):
    class Meta:
        model = Lab
        fields = '__all__'


class TypeForm(ModelForm):
    class Meta:
        model = Type
        fields = '__all__'


class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = '__all__'
        widgets = {'id_lab': HiddenInput(), 'dismissed': HiddenInput(), 'entry_date': SelectDateWidget()}
