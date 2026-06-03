from pathlib import Path
from dotenv import load_dotenv
import os

BASE_DIR = Path(__file__).resolve().parent.parent

# Load .env
load_dotenv(os.path.join(BASE_DIR, '.env'))

SECRET_KEY = 'django-insecure-dx3w+p=k$%vb(aw_zba)j693k2^z1h7c!_4y#t6&h8gml+suxq'

DEBUG = False

ALLOWED_HOSTS = [
    'bimiworldwide.com',
    'www.bimiworldwide.com',
    'localhost',
    '127.0.0.1',
    '*',  # testing ke liye, baad me hata dena
]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'website',
    'custom_admin',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'bimi_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'bimi_project.wsgi.application'

# PostgreSQL
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'bimi_db',
        'USER': 'postgres',
        'PASSWORD': 'pass123',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'

USE_I18N = True
USE_TZ = True

# Static Files
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

STATIC_ROOT = BASE_DIR / 'staticfiles'

# Media Files
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Domain
BASE_URL = "https://www.bimiworldwide.com"

CSRF_TRUSTED_ORIGINS = [
    "https://bimiworldwide.com",
    "https://www.bimiworldwide.com",
]

# TEMPORARILY DISABLE SSL SETTINGS FOR TESTING
SECURE_SSL_REDIRECT = False
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False

SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'

SECURE_HSTS_SECONDS = 0
SECURE_HSTS_INCLUDE_SUBDOMAINS = False
SECURE_HSTS_PRELOAD = False

# Email Settings
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = os.getenv("SMTP_HOST")
EMAIL_PORT = int(os.getenv("SMTP_PORT", 587))

EMAIL_HOST_USER = os.getenv("SMTP_EMAIL")
EMAIL_HOST_PASSWORD = os.getenv("SMTP_PASSWORD")

EMAIL_USE_TLS = True

FROM_EMAIL = os.getenv("FROM_EMAIL")
REPLY_TO_EMAIL = os.getenv("REPLY_TO_EMAIL")