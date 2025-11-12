from django.contrib import admin
from .models import Vendor

@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display = ('name', 'commercial_number', 'phone', 'email', 'active')
    list_filter = ('active',)
    search_fields = ('name', 'commercial_number', 'email')
