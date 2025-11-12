from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'unit', 'reference_price', 'active')
    list_filter = ('active',)
    search_fields = ('code', 'name')
