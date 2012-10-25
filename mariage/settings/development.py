# -*- coding: utf-8 -*-
import os
from common import *


DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '../mariage.sqlite',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}


# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/"

STATIC_URL = '/static/' # static files (css, js, etc.)
MEDIA_URL = '/media/' # uploads
STATIC_ROOT = os.path.join(os.path.dirname(PROJECT_DIR), 'files', 'static')
MEDIA_ROOT = os.path.join(os.path.dirname(PROJECT_DIR), 'files', 'uploaded')


#TINYMCE_JS_ROOT = STATIC_ROOT + '/tiny_mce'


#MIDDLEWARE_CLASSES += ('debug_toolbar.middleware.DebugToolbarMiddleware', )

#INSTALLED_APPS += ('debug_toolbar' ,)
INTERNAL_IPS = ('127.0.0.1',)

