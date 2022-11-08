import os
from django.conf.locale.ru import formats as ru_formats
# from dotenv import load_dotenv
from bd_config import (SECRET_KEY, DB_NAME, DB_USERNAME, DB_PASSWORD, REDIS_HOST_CONF, REDIS_PORT_CONF)


ru_formats.DATETIME_FORMAT = "d M Y H:i:s"
ru_formats.TIME_FORMAT = "H:i:s"


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# load_dotenv('main_env.env')


SECRET_KEY = SECRET_KEY

DEBUG = True

ALLOWED_HOSTS = [
    '*',
]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework.authtoken',
    'rest_framework',
    'drf_yasg',
    'notes',
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

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'project.wsgi.application'
ASGI_APPLICATION = "project.asgi.application"


# DATABASES = {
#     'default': {
#         'NAME': os.environ.get('NAME_DB'),
#         'ENGINE': 'django.db.backends.postgresql',
#         'USER': os.environ.get('USER_DB'),
#         'PASSWORD': os.environ.get('PASSWORD_DB')
#     },
# }

DATABASES = {
    'default': {
        'NAME': DB_NAME,
        'ENGINE': 'django.db.backends.postgresql',
        'USER': DB_USERNAME,
        'PASSWORD': DB_PASSWORD
    },
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


LANGUAGE_CODE = 'ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


STATIC_URL = 'static/'

if not DEBUG:
    STATIC_ROOT = ''

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static")
]


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REDIS_HOST = REDIS_HOST_CONF
REDIS_PORT = REDIS_PORT_CONF


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication'
    ]
}