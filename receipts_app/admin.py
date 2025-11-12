from django.contrib import admin
from .models import Receipt, ReceiptItem

class ReceiptItemInline(admin.TabularInline):
    model = ReceiptItem
    extra = 1

@admin.register(Receipt)
class ReceiptAdmin(admin.ModelAdmin):
    list_display = ('receipt_number', 'date', 'received_by')
    search_fields = ('receipt_number',)
    inlines = [ReceiptItemInline]
