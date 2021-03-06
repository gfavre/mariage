# -*- coding: utf-8 -*-
import os
from common import *

ADMINS = (('Gregory Favre', 'gregory.favre@gmail.com'),)


DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'grfavre_mariage',
        'USER': 'grfavre_mariage',
        'PASSWORD': 'mariagedbp4ssw0rd',
        'HOST': '',
        'PORT': '',
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'django_cache',
    }
}

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/"

STATIC_URL = '/static/' # static files (css, js, etc.)
MEDIA_URL = '/static/media/' # uploads
STATIC_ROOT = '/home/grfavre/webapps/mariage_static/'
MEDIA_ROOT = '/home/grfavre/webapps/mariage_static/media/'
STATICFILES_DIRS = ('/home/grfavre/webapps/mariage/mariage/media',)


EMAIL_HOST = 'smtp.webfaction.com'
EMAIL_HOST_USER = 'grfavre_mariage'
EMAIL_HOST_PASSWORD = 'mariagedbp4ssw0rd'
DEFAULT_FROM_EMAIL = 'mariage@nonoetgreg.ch'
SERVER_EMAIL = 'mariage@nonoetgreg.ch'

