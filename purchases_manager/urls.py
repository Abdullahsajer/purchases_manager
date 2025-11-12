from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render

# 🎯 دالة الصفحة الرئيسية
def home(request):
    return render(request, 'home.html')

urlpatterns = [
    # ⚙️ لوحة تحكم Django
    path('admin/', admin.site.urls),

    # 🏠 الصفحة الرئيسية
    path('', home, name='home'),

    # 👤 إدارة المستخدمين والصلاحيات
    path('accounts/', include('accounts_app.urls')),

    # 🏢 إدارة الموردين
    path('vendors/', include('vendors_app.urls')),

    # 🧰 إدارة المنتجات والأصناف
    path('products/', include('products_app.urls')),

    # 🧾 إدارة الفواتير وبنودها
    path('invoices/', include('invoices_app.urls')),

    # 📦 تسجيل الأصناف المستلمة فعليًا
    path('receipts/', include('receipts_app.urls')),

    # 🔍 المطابقة بين الفواتير والاستلام
    path('matching/', include('matching_app.urls')),

    # 📊 التقارير ولوحات المعلومات
    path('reports/', include('reports_app.urls')),
]
