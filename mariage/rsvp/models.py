from django.db import models
from cmsplugin_contact.models import BaseContact
from django.utils.translation import ugettext_lazy as _

class CustomContact(BaseContact):
    presence_label = models.CharField(_('Presence label'),
                                     default=_('Will you attend'), max_length=20)