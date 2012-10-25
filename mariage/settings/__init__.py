# -*- coding: utf-8 -*-

import os
from django.utils import importlib

ENVMAP = {
    'production':['mariage-production',],
    'development':['mariage']
}

def update_current_settings(file_name):
    """
    Given a filename, this function will insert all variables and
    functions in ALL_CAPS into the global scope.
    """
    new_settings = importlib.import_module(file_name)
    for k, v in new_settings.__dict__.items():
        if k.upper() == k:
            globals().update({k:v})


if 'ENV_TO_USE' in os.environ:
    current_env = os.environ['ENV_TO_USE']
else:
    current_env = os.path.split(os.environ.get('VIRTUAL_ENV', 'mariage'))[1]

to_load = []
for k, v in ENVMAP.items():
    if current_env in v:
        to_load.append(k)

update_current_settings('mariage.settings.common')
for x in to_load:
    try:
        update_current_settings('mariage.settings.%s' % x)
    except ImportError:
        print "Error importing %s" % x