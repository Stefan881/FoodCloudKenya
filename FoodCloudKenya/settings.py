"""
Django settings for FoodCloudKenya project.

Generated by 'django-admin startproject' using Django 5.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
# from dotenv import load_dotenv
import dj_database_url
import os
print(os.environ.get('DATABASE_URL'))
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
# load_dotenv(os.path.join(BASE_DIR/".eVar",".env"))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = os.environ.get("SECRET_KEY")
SECRET_KEY='django-insecure-g-x_b$l153fsmxt&v*%2(ci%-9lzgykk8!k7=0vw27u8)v)*b#'
# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = os.environ.get("DEBUG","True").lower == "false"
DEBUG=False 

# ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS", "").split(",")
ALLOWED_HOSTS = ['127.0.0.1','localhost','foodcloudkenya-3.onrender.com']





# Application definition

SITE_ID = 3

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'SavorySpot',
    'crispy_forms',
    'crispy_bootstrap4',
    'users',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
]

SOCIALACCOUNT_PROVIDERS = {
    "google": {
        "scope": [
            "profile",
            "email"
        ],
        "AUTH_PARAMS": {"access_type": "online"}
    }
}

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap4"

CRISPY_TEMPLATE_PACK = "bootstrap4"

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
]

ROOT_URLCONF = 'FoodCloudKenya.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
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

WSGI_APPLICATION = 'FoodCloudKenya.wsgi.application'

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

# DATABASES = {
#     'default':dj_database_url.config(
#         default = "sqlite:///" + os.path.join(BASE_DIR, "db.sqlite3")
#     )
    
# }


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'foodcloudkenya',
        'USER': 'postgres',
        'PASSWORD': '12345678',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


# dj_database_url = os.environ.get("DATABASE_URL")


# DATABASES['default'] = dj_database_url.parse(os.environ.get('DATABASE_URL'))

# db_from_env = dj_database_url.config()

# DATABASES = {
#     'default': db_from_env
# }

DATABASES['default'] = dj_database_url.parse("postgres://foodcloudkenya_user:8wDV7dRn3IHctOggkAA2RIT7VdqJa4rI@dpg-cnu6l87sc6pc73b6gr10-a.oregon-postgres.render.com/foodcloudkenya")


#DATABASE_URL="postgres://foodcloudkenya_user:8wDV7dRn3IHctOggkAA2RIT7VdqJa4rI@dpg-cnu6l87sc6pc73b6gr10-a.oregon-postgres.render.com/foodcloudkenya"


# postgres://foodcloudkenya_user:8wDV7dRn3IHctOggkAA2RIT7VdqJa4rI@dpg-cnu6l87sc6pc73b6gr10-a.oregon-postgres.render.com/foodcloudkenya

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')


STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# STATIC_ROOT = 'BASE_DIR/AllStatic/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'ondeyostephen0@gmail.com'
EMAIL_HOST_PASSWORD = 'fbjy pjlg mqyx gcti'
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False


AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend"

)

LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/"

