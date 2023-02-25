"""
Django settings for django_freelance project.

Generated by 'django-admin startproject' using Django 4.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-kh_3vj!qnn-r1^$ex+s3tmrtfux!fg8lq%#ujp602=5g_3ig@4'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'freelance.apps.FreelanceConfig',  # наше приложение freelance
    'rest_framework',  # DRF
    'djoser',  # djoser
    'corsheaders',  # corsheaders
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "corsheaders.middleware.CorsMiddleware",  # corsheaders
    "django.middleware.common.CommonMiddleware",  # corsheaders
]

ROOT_URLCONF = 'django_freelance.urls'

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

WSGI_APPLICATION = 'django_freelance.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',  # стандартная БД
        # 'NAME': BASE_DIR / 'db.sqlite3',  # стандартная БД
        'ENGINE': 'django.db.backends.postgresql',  # БД PostrgeSQL
        'NAME': 'freelance',  # Имя нашей БД
        'USER': 'postgres',  # пользователь postgres - который создал БД
        'PASSWORD': 'blog1234',  # пароль в PostgreSQL, для пользователя postgres
        'HOST': '127.0.0.1',  # либо просто - 'localhost'
        'PORT': '5432',  # стандартный порт
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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

# Для corsheaders - разрешённые хосты
CORS_ALLOWED_ORIGINS = [
    # "https://example.com", # измени на деплое
    # "https://sub.example.com", # измени на деплое
    "http://localhost:8080",  # тестовый web сервер джанги
    # "http://127.0.0.1:9000",  # можно ужалить
]

# Для corsheaders - список разрешённых методов обращения к серверу
CORS_ALLOW_METHODS = [
    "DELETE",
    "GET",
    "OPTIONS",
    "PATCH",
    "POST",
    "PUT",
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

# LANGUAGE_CODE = 'en-En'  # англ. в admin
# TIME_ZONE = 'UTC'  # стандарт
LANGUAGE_CODE = 'ru-Ru'  # русский язык в admin

TIME_ZONE = 'Europe/Moscow'  # время по МСК

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'