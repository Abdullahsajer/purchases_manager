from django.db import models
from invoices_app.models import InvoiceItem
from receipts_app.models import ReceiptItem

class MatchResult(models.Model):
    STATUS_CHOICES = [
        ('match', 'مطابق'),
        ('missing', 'ناقص'),
        ('extra', 'صنف زائد'),
    ]

    invoice_item = models.ForeignKey(InvoiceItem, on_delete=models.CASCADE, verbose_name="بند الفاتورة")
    receipt_item = models.ForeignKey(ReceiptItem, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="بند الاستلام")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, verbose_name="حالة المطابقة")
    difference = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name="الفرق في الكمية")

    def __str__(self):
        return f"{self.invoice_item.product.name} - {self.get_status_display()}"

    class Meta:
        verbose_name = "نتيجة مطابقة"
        verbose_name_plural = "نتائج المطابقة"
