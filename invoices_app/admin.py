from django.contrib import admin
from .models import Invoice, InvoiceItem

class InvoiceItemInline(admin.TabularInline):
    model = InvoiceItem
    extra = 1

@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('invoice_number', 'vendor', 'date', 'created_by', 'approved')
    list_filter = ('approved', 'vendor')
    search_fields = ('invoice_number', 'vendor__name')
    inlines = [InvoiceItemInline]
