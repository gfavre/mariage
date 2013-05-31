# -*- coding: utf-8 -*-

HOSTMAP = {
    'development': ['GFiMac27.local', 'kismac2.epfl.ch', 'iMac-de-Gregory-Favre.local', 'MacBook-Air-de-Gregory.local'],
    'production':['web224.webfaction.com', 'web392.webfaction.com',],
    }

import socket, re
from django.utils import importlib

def update_current_settings(file_name):
    """
    Given a filename, this function will insert all variables and
    functions in ALL_CAPS into the global scope.
    """
    new_settings = importlib.import_module(file_name)
    for k, v in new_settings.__dict__.items():
        if k.upper() == k:
            globals().update({k:v})

current_hostname = socket.gethostname()
to_load = []

for k, v in HOSTMAP.items():
    for pattern in v:
        if re.match(pattern, current_hostname):
            to_load.append(k)

update_current_settings('mariage.settings.common')
for x in to_load:
    try:
        update_current_settings('mariage.settings.%s' % x)
    except ImportError, msg:
        print "Error importing %s" % x
        print msg
