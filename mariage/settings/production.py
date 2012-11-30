# -*- coding: utf-8 -*-
import os
from common import *

ADMINS = (('Gregory Favre', 'gregory.favre@gmail.com'),)


DEBUG = False
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

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/"

STATIC_URL = '/static/' # static files (css, js, etc.)
MEDIA_URL = '/media/' # uploads
STATIC_ROOT = '/home/grfavre/webapps/mariage_static/'
MEDIA_ROOT = '/home/grfavre/webapps/mariage_static/media/'
STATICFILES_DIRS = ('/home/grfavre/webapps/mariage/mariage/media',)
