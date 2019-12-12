from django.contrib import admin
from .models import *


class ItemAdmin(admin.ModelAdmin):
    list_display = ('id_item', 'id_lab', 'name', 'desc', 'entry_date', 'id_type', 'dismissed')
    actions = ['dismiss_item', 'undismiss_item']

    def dismiss_item(self, request, queryset):
        queryset.update(dismissed=True)

    def undismiss_item(self, request, queryset):
        queryset.update(dismissed=False)

    dismiss_item.short_description = "Dar de baja"
    undismiss_item.short_description = "Dar de alta"


admin.site.register(Item, ItemAdmin)
admin.site.register(Lab)
admin.site.register(Type)



