from pathlib import Path

# 📁 المسار الأساسي للمشروع
BASE_DIR = Path(__file__).resolve().parent.parent

# 🔐 مفتاح الأمان (غيّره في بيئة الإنتاج)
SECRET_KEY = 'django-insecure-(ezysnb9ch_0cdk_^hcvg41l+8vmjjl==ysh%z&r7!gw7nspck'

# ⚙️ وضع التطوير
DEBUG = True

# 🌍 النطاقات المسموح بها
ALLOWED_HOSTS = []


# 🧩 التطبيقات المثبتة
INSTALLED_APPS = [
    # 🧱 تطبيقات Django الأساسية
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # 🧩 تطبيقات المشروع المخصصة
    'accounts_app',
    'vendors_app',
    'products_app',
    'invoices_app',
    'receipts_app',
    'matching_app',
    'reports_app',
]


# 🧱 الوسطاء (Middleware)
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',  # ✅ دعم تعدد اللغات
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# 🚦 روابط المشروع
ROOT_URLCONF = 'purchases_manager.urls'


# 🎨 إعدادات القوالب
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # ✅ مجلد القوالب العام
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


# 🧰 إعدادات WSGI
WSGI_APPLICATION = 'purchases_manager.wsgi.application'


# 🗄️ قاعدة البيانات (SQLite الافتراضية)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# 🔑 تحقق من كلمات المرور
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


# 🌐 اللغة والمنطقة الزمنية
LANGUAGE_CODE = 'ar'  # ✅ اللغة العربية
TIME_ZONE = 'Asia/Riyadh'  # ✅ التوقيت المحلي للرياض
USE_I18N = True
USE_L10N = True
USE_TZ = True


# 🗂️ الملفات الثابتة (Static Files)
STATIC_URL = 'static/'
STATICFILES_DIRS = [
    BASE_DIR / "static",
]

# 📁 إعدادات الملفات المرفقة (وسائط)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# 🧾 الإعداد الافتراضي للمفاتيح
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'accounts_app.Employee'

