from django.contrib import admin
from .models import ReportLog

@admin.register(ReportLog)
class ReportLogAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'created_by')
    search_fields = ('name', 'created_by__username')
    list_filter = ('created_at',)
