from django.db import models
from django.contrib.auth.models import AbstractUser

class Employee(AbstractUser):
    ROLE_CHOICES = [
        ('purchasing', 'موظف مشتريات'),
        ('warehouse', 'موظف مستودع'),
        ('accountant', 'محاسب'),
        ('manager', 'مدير'),
    ]

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, verbose_name="الدور الوظيفي")
    phone = models.CharField(max_length=20, blank=True, null=True, verbose_name="رقم الجوال")
    department = models.CharField(max_length=100, blank=True, null=True, verbose_name="القسم")

    def __str__(self):
        return f"{self.username} - {self.get_role_display()}"

    class Meta:
        verbose_name = "الموظف"
        verbose_name_plural = "الموظفون"
