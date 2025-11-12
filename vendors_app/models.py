from django.db import models

class Vendor(models.Model):
    name = models.CharField(max_length=150, verbose_name="اسم المورد")
    commercial_number = models.CharField(max_length=50, blank=True, null=True, verbose_name="السجل التجاري")
    contact_name = models.CharField(max_length=100, blank=True, null=True, verbose_name="اسم جهة الاتصال")
    phone = models.CharField(max_length=20, blank=True, null=True, verbose_name="رقم الهاتف")
    email = models.EmailField(blank=True, null=True, verbose_name="البريد الإلكتروني")
    address = models.TextField(blank=True, null=True, verbose_name="العنوان")
    active = models.BooleanField(default=True, verbose_name="نشط")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "مورد"
        verbose_name_plural = "الموردون"
