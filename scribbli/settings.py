"""
Django settings for scribbli project.

Generated by 'django-admin startproject' using Django 2.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
from datetime import timedelta

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ml=)_f=*a*670hmo&1hd#6)u)9m5t$%@q^ln6(wg5#f2ne_5p!'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    '*',
    'localhost',
]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'django.contrib.staticfiles',

    # ---- Django addons ----
    'mptt',
    'graphene_django',
    'graphql_jwt.refresh_token.apps.RefreshTokenConfig',

    # subapps
    'scribbli',
    'scribbli.profiles',
    'scribbli.universe',
    'scribbli.characters',
    'scribbli.stories',
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

ROOT_URLCONF = 'scribbli.urls'

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

WSGI_APPLICATION = 'scribbli.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.'
                'UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.'
                'MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.'
                'CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.'
                'NumericPasswordValidator',
    },
]


# Supported authenticators
# https://docs.djangoproject.com/en/2.1/ref/settings/#std:setting-AUTHENTICATION_BACKENDS

AUTHENTICATION_BACKENDS = [
    'graphql_jwt.backends.JSONWebTokenBackend',
    'django.contrib.auth.backends.ModelBackend',
]


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'

# Define the default site id for `django.contrib.sites`
SITE_ID = 1

# Define the url to redirect to once logged in
LOGIN_REDIRECT_URL = 'profile-detail--mine'

# Define urls where the django debug toolbar should render
INTERNAL_IPS = ('localhost', '127.0.0.1')

# Customize type of AutoField to use when PK is not defined
# https://docs.djangoproject.com/ens/3.2/releases/3.2/#customizing-type-of-auto-created-primary-keys

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Configure DRF
REST_FRAMEWORK = {
    # Should use versioning
    'DEFAULT_VERSIONING_CLASS': 'rest_framework.versioning.'
                                'AcceptHeaderVersioning',
    'DEFAULT_VERSION': '1.0',

    # Disable the browsable API
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    ),
}

# Configure Graphene schema
GRAPHENE = {
    'SCHEMA': 'scribbli.schema.schema',
    'MIDDLEWARE': [
        'graphql_jwt.middleware.JSONWebTokenMiddleware',
    ],
}

# JWT
GRAPHQL_JWT = {
    'JWT_PAYLOAD_HANDLER': 'app.utils.jwt_payload',
    'JWT_AUTH_HEADER_PREFIX': 'Bearer',
    'JWT_VERIFY_EXPIRATION': True,
    'JWT_LONG_RUNNING_REFRESH_TOKEN': True,
    'JWT_EXPIRATION_DELTA': timedelta(minutes=5),
    'JWT_REFRESH_EXPIRATION_DELTA': timedelta(days=7),
    'JWT_SECRET_KEY': 'ml=)_f=*a*670hmo&1hd#6)u)9m5t$%@q^ln6(wg5#f2ne_5p!',
    'JWT_ALGORITHM': 'HS256',
}
