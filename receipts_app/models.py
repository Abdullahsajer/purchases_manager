from django.db import models
from products_app.models import Product
from accounts_app.models import Employee

class Receipt(models.Model):
    receipt_number = models.CharField(max_length=100, unique=True, verbose_name="رقم الاستلام")
    date = models.DateField(verbose_name="تاريخ الاستلام")
    received_by = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, verbose_name="المستلم")
    notes = models.TextField(blank=True, null=True, verbose_name="ملاحظات")

    def __str__(self):
        return f"استلام {self.receipt_number}"

    class Meta:
        verbose_name = "استلام"
        verbose_name_plural = "الاستلامات"


class ReceiptItem(models.Model):
    receipt = models.ForeignKey(Receipt, on_delete=models.CASCADE, related_name='items', verbose_name="الاستلام")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="الصنف")
    quantity = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="الكمية المستلمة")

    def __str__(self):
        return f"{self.product.name} ({self.quantity})"

    class Meta:
        verbose_name = "بند استلام"
        verbose_name_plural = "بنود الاستلامات"
