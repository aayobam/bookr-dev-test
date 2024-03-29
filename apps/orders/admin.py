from django.contrib import admin
from .models import Order


@admin.register(Order)
class AdminOrder(admin.ModelAdmin):
    list_display = ('order_by', 'first_name', 'last_name', 'email', 'phone_no', 'paid_amount', 'reference')
    search_field = ('product', 'reference', 'order_by', 'email')
    readonly_fields = ["reference", 'order_by']
