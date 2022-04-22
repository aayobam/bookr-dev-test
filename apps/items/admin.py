from django.contrib import admin
from apps.items.models import OrderedItems


@admin.register(OrderedItems)
class AdminOrderedItems(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name', 'email', 'phone_no', 'product', 'quantity', 'price')
