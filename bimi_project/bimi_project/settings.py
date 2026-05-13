from pathlib import Path
from dotenv import load_dotenv
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-dx3w+p=k$%vb(aw_zba)j693k2^z1h7c!_4y#t6&h8gml+suxq'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

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


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }


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

# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = 'static/'


# Project ke root static folder ka path
STATICFILES_DIRS = [
    BASE_DIR / "static",
]

# (Optional) — Agar production ke liye collect karna ho to
STATIC_ROOT = BASE_DIR / "staticfiles"


import os
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# ========================================
BASE_URL = "https://a7c2-2401-4900-88f0-3f9b-8d47-2bd6-4d0b-ce8a.ngrok-free.app"  # 👈 local testing
# For Production Use
# BASE_URL = "https://yourdomain.com"


CSRF_TRUSTED_ORIGINS = [
    "https://a7c2-2401-4900-88f0-3f9b-8d47-2bd6-4d0b-ce8a.ngrok-free.app",
    "http://127.0.0.1:8000",
    "http://localhost:8000",
]
# =============================================================


#========Mail Sending Settings=======
import os

BASE_DIR = Path(__file__).resolve().parent.parent

# LOAD .env FILE
load_dotenv(os.path.join(BASE_DIR, '.env'))


# =========================================================
# EMAIL SETTINGS
# =========================================================

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = os.getenv("SMTP_HOST")

EMAIL_PORT = int(os.getenv("SMTP_PORT", 587))

EMAIL_HOST_USER = os.getenv("SMTP_EMAIL")

EMAIL_HOST_PASSWORD = os.getenv("SMTP_PASSWORD")

EMAIL_USE_TLS = True

# CUSTOM
FROM_EMAIL = os.getenv("FROM_EMAIL")

REPLY_TO_EMAIL = os.getenv("REPLY_TO_EMAIL")

#=====================================