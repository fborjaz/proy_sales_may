"""
Django settings for proy_sales project.
"""

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# ------------------------------------------------------------------------------
# Configuración Principal del Proyecto
# ------------------------------------------------------------------------------

SECRET_KEY = 'django-insecure-_fyjq%+2u$$(rf3y5vl-6ktqwsj&bc^phj4pw=ty7*!lta+a$='
DEBUG = True  # Desactivar en producción (False)
ALLOWED_HOSTS = []

# ------------------------------------------------------------------------------
# Aplicaciones
# ------------------------------------------------------------------------------

INSTALLED_APPS = [
    # Aplicaciones Django por defecto
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Tus aplicaciones
    'core.apps.CoreConfig',

    # Aplicaciones de terceros
    'django_extensions',
]

# ------------------------------------------------------------------------------
# Middleware
# ------------------------------------------------------------------------------

MIDDLEWARE = [
    # Middleware de seguridad
    'django.middleware.security.SecurityMiddleware',

    # Manejo de sesiones
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',

    # Autenticación
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',

    # Protección clickjacking
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'proy_sales.urls'  # Archivo principal de URLs

# ------------------------------------------------------------------------------
# Plantillas
# ------------------------------------------------------------------------------

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # Directorio base de plantillas
        'APP_DIRS': True,  # Buscar plantillas en las apps
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',  # Variables de depuración
                'django.template.context_processors.request',  # Objeto request
                'django.contrib.auth.context_processors.auth',  # Información de autenticación
                'django.contrib.messages.context_processors.messages',  # Mensajes del sistema
            ],
        },
    },
]

WSGI_APPLICATION = 'proy_sales.wsgi.application'  # Configuración WSGI

# ------------------------------------------------------------------------------
# Base de datos
# ------------------------------------------------------------------------------

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'factur.sqlite3',
    }
}

# ------------------------------------------------------------------------------
# Validación de contraseñas
# ------------------------------------------------------------------------------

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

# ------------------------------------------------------------------------------
# Configuración de la visualización del modelo en django-extensions
# ------------------------------------------------------------------------------
GRAPH_MODELS = {
    'all_applications': True,
    'group_models': True,
}

# ------------------------------------------------------------------------------
# Internacionalización
# ------------------------------------------------------------------------------

LANGUAGE_CODE = 'es-ec'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# ------------------------------------------------------------------------------
# Archivos Estáticos y Media
# ------------------------------------------------------------------------------

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [ BASE_DIR / 'static' ]

MEDIA_ROOT = BASE_DIR / 'media'
MEDIA_URL = '/media/'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
