import os
from pathlib import Path
# from dotenv import load_dotenv

# Load environment variables from .env file
# load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = '$!@%0u0@m&x85($hsavn*qrcq54)=4a+f8!n#sgs1ko-8q+&mt'

DEBUG = True

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'ComplaintMS',
    'django.contrib.admin',
    'crispy_forms',
    'crispy_bootstrap5',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'reportlab',
    'django_extensions',
]

CRISPY_ALLOWED_TEMPLATE_PACKS = ["bootstrap5"]
CRISPY_TEMPLATE_PACK = "bootstrap5"

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Security Settings (disabled for development)
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'
# SECURE_HSTS_SECONDS = 31536000
# SECURE_HSTS_INCLUDE_SUBDOMAINS = True
# SECURE_HSTS_PRELOAD = True

# Session Security (disabled for development)
# SESSION_COOKIE_SECURE = True
SESSION_COOKIE_HTTPONLY = True
# CSRF_COOKIE_SECURE = True
CSRF_COOKIE_HTTPONLY = True

# Cache Settings
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'unique-snowflake',
    }
}

ROOT_URLCONF = 'web.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'web.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Kolkata'
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# Static files configuration
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'ComplaintMS/static'),
]

CRISPY_TEMPLATE_PACK = 'bootstrap5'

LOGIN_REDIRECT_URL = '/login_redirect/'
LOGIN_URL = 'signin'
LOGOUT_URL = 'logout'
LOGOUT_REDIRECT_URL = '/logout-page/'
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'

# Gemini API Configuration
GEMINI_API_KEY = 'AIzaSyANYxaSUCnrxb_PA-NJhPsNaHSbUwt2Rrw'

EMAIL_PORT = 587
EMAIL_HOST_USER = 'vineshreddy'  # add email address here
EMAIL_HOST_PASSWORD = ''  # email password
DEFAULT_FROM_EMAIL = ''  # add email address here
EMAIL_USE_TLS = True

AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
)

SITE_ID = 1

# ✅ Recommended by Django 3.2+ to avoid warnings
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
