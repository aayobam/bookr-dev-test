from django.contrib import admin
from .models import Product

@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    list_display = ('id', 'category', 'name', 'price', 'quantity', 'created_at', 'updated_at')
    search_field = ('name', 'category')