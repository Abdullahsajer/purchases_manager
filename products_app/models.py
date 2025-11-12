from django.db import models

class Product(models.Model):
    code = models.CharField(max_length=50, unique=True, verbose_name="كود الصنف")
    name = models.CharField(max_length=200, verbose_name="اسم الصنف")
    unit = models.CharField(max_length=50, verbose_name="الوحدة")
    reference_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="السعر المرجعي")
    active = models.BooleanField(default=True, verbose_name="نشط")

    def __str__(self):
        return f"{self.code} - {self.name}"

    class Meta:
        verbose_name = "صنف"
        verbose_name_plural = "الأصناف"
