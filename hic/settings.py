"""
Django settings for hic project.

Generated by 'django-admin startproject' using Django 2.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '_%q)@_kgh_n(uim74u3d4=2_c0(u-ga)eqb2271)4z%3vdfkf^'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# AUTH_USER_MODEL = 'main.User'
LOGIN_REDIRECT_URL = '/inicio/'

# Application definition
# Estas son las app que se comparten publicamente
SHARED_APPS = [
    'tenant_schemas',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'crispy_forms',
    'colorfield',
    'customer'
]

TENANT_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'colorfield',
    'crispy_forms',
    'hic.main',
    'hic.paciente',
    'hic.consulta',

    'hic.cita',
]

INSTALLED_APPS = [
    'tenant_schemas',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cloudinary',
    'crispy_forms',
    'colorfield',
    'customer',
    'hic.main',
    'hic.paciente',
    'hic.consulta',
    'hic.cita',

]

MIDDLEWARE = [
    'tenant_schemas.middleware.TenantMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'hic.urls'

## CLOUDINARY CONFIGURATIONS
CLOUDINARY = {
    'max_length': 200,
    'cloud_name': 'h3dx0',
    'api_key': '862856891596518',
    'api_secret': '9L4z9ALHfOpHl7SXuNq5b5AFimQ',
}

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
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

WSGI_APPLICATION = 'hic.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases
#
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'hic',
#         'USER': 'postgres',
#         'PASSWORD': 'postgres',
#         'HOST': '127.0.0.1',
#         'PORT': 5432,
#     }
# }

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'hic',
#         'USER': 'hic',
#         'PASSWORD': 'Hic123.',
#         'HOST': '127.0.0.1',
#         'PORT': '',
#     }
# }

DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.postgresql_psycopg2',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'ENGINE': 'tenant_schemas.postgresql_backend',
        'NAME': 'hic_multi',
        'USER': 'hic_multi',
        'PASSWORD': 'Hic123.',
        'HOST': '127.0.0.1',
        'PORT': 5432,
    }
}
DATABASE_ROUTERS = (
    'tenant_schemas.routers.TenantSyncRouter',
)


TENANT_MODEL = "customer.Client"# app.Model

HIC_DIR = "hic/hic_pdf/"
HIC_HOST = 'http://localhost:8000/'
HIC_LOCAL_DIR = '/home/h3dx0/Dev/hic_general/'  # Password validation
#
# if HEROKU_SERVER:
#     DATABASES['default']['ENGINE'] = 'django.db.backends.postgresql_psycopg2',
#     DATABASES['default']['HOST'] = 'ec2-54-204-37-92.compute-1.amazonaws.com'
#     DATABASES['default']['NAME'] = 'd7d24no9il8lab'
#     DATABASES['default']['USER'] = 'xfmhcrrcfkfqhd'
#     DATABASES['default']['PASSWORD'] = '20c6d0dde4247ee6fafebde54be72db4b191feec35218a6d77139b6641d83379'
#     DATABASES['default']['PORT'] = 5432
#     HIC_HOST = 'https://sichic.herokuapp.com/'
#     HIC_LOCAL_DIR = '/home/h3dx0/Dev/nreed/'
#
# DIGITAL_SERVER = False
#
# if DIGITAL_SERVER:
#     DATABASES['default']['ENGINE'] = 'django.db.backends.postgresql_psycopg2',
#     DATABASES['default']['HOST'] = 'localhost'
#     DATABASES['default']['NAME'] = 'hic_cub'
#     DATABASES['default']['USER'] = 'hic_cub'
#     DATABASES['default']['PASSWORD'] = 'Hic123.'
#     DATABASES['default']['PORT'] = 5432
#     HIC_HOST = 'http://cmdcuba.com.mx/'
#     HIC_LOCAL_DIR = '/home/h3dx0/python_projects/hic_cuba/'
# else:
#     HIC_HOST = 'http://localhost:8000/'
#     HIC_LOCAL_DIR = '/home/h3dx0/Dev/hic/'  # Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'es-es'

TIME_ZONE = 'America/Mexico_City'

USE_I18N = True

USE_L10N = True

USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# # Extra places for collectstatic to find static files.
# STATICFILES_DIRS = (
#     os.path.join(BASE_DIR, 'static'),
# )
