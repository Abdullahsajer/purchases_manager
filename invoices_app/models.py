from django.db import models
from vendors_app.models import Vendor
from products_app.models import Product
from accounts_app.models import Employee

class Invoice(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, verbose_name="المورد")
    invoice_number = models.CharField(max_length=100, unique=True, verbose_name="رقم الفاتورة")
    date = models.DateField(verbose_name="تاريخ الفاتورة")
    created_by = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, verbose_name="أُدخلت بواسطة")
    notes = models.TextField(blank=True, null=True, verbose_name="ملاحظات")
    approved = models.BooleanField(default=False, verbose_name="معتمدة")

    def __str__(self):
        return f"فاتورة {self.invoice_number} - {self.vendor.name}"

    class Meta:
        verbose_name = "فاتورة"
        verbose_name_plural = "الفواتير"


class InvoiceItem(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, related_name='items', verbose_name="الفاتورة")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="الصنف")
    quantity = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="الكمية")
    unit_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="سعر الوحدة")

    def total_price(self):
        return self.quantity * self.unit_price

    def __str__(self):
        return f"{self.product.name} ({self.quantity})"

    class Meta:
        verbose_name = "بند فاتورة"
        verbose_name_plural = "بنود الفواتير"
