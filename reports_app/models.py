from django.db import models
from accounts_app.models import Employee

class ReportLog(models.Model):
    name = models.CharField(max_length=150, verbose_name="اسم التقرير")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ الإنشاء")
    created_by = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, verbose_name="تم توليده بواسطة")
    description = models.TextField(blank=True, null=True, verbose_name="الوصف")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "سجل تقرير"
        verbose_name_plural = "سجلات التقارير"
