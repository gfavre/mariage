#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.db import models
from cmsplugin_contact.models import BaseContact
from django.utils.translation import ugettext_lazy as _

class CustomContact(BaseContact):
    name_label = models.CharField(_(u"Libellé du nom"), default="Votre nom", max_length=100)
    presence_label = models.CharField(_(u'Libellé de la demande'), default=_(u'Serez-vous présents?'), max_length=100)