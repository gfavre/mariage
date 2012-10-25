# -*- coding: utf-8 -*-
import os
from common import *

ADMINS = (('Gregory Favre', 'gregory.favre@epfl.ch'),)


DEBUG = False
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': { 'read_default_file': '/data/www/cosadoca-production/private/my.cnf'
        },
    }
}

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/"

STATIC_URL = '/static/' # static files (css, js, etc.)
MEDIA_URL = '/media/' # uploads
STATIC_ROOT = '/data/www/cosadoca-production/htdocs/static'
MEDIA_ROOT = '/data/www/cosadoca-production/htdocs/uploaded'
STATICFILES_DIRS = (os.path.join(os.path.dirname(PROJECT_DIR), 'cosadoca', 'media'),)

FILER_STORAGES['public']['main']['OPTIONS']['location'] = MEDIA_ROOT
FILER_STORAGES['private']['main']['OPTIONS']['location'] = MEDIA_ROOT

INTERNAL_IPS = ('127.0.0.1',)
HAYSTACK_WHOOSH_PATH = os.path.join('/data/www/cosadoca-production/private/cosadoca_index')


