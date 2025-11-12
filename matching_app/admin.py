from django.contrib import admin
from .models import MatchResult

@admin.register(MatchResult)
class MatchResultAdmin(admin.ModelAdmin):
    list_display = ('invoice_item', 'receipt_item', 'status', 'difference')
    list_filter = ('status',)
    search_fields = ('invoice_item__product__name',)
