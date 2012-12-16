from django.db import models
from django.utils.translation import ugettext as _

from cms.models import CMSPlugin
from photologue.models import Photo


class SizedPhotologuePhotoPlugin(CMSPlugin):
    SIZES = (
        (u'thumbnail', _('Small')),
        (u'medium', _('Medium')),
        (u'full', _('Large')),
    )
    ALIGNMENT = (
        (u'left', _('Floating left')),
        (u'right', _('Floating right')),
    )
    photo = models.ForeignKey(Photo)
    size = models.CharField(_('Photo Size'), max_length=20, choices=SIZES, default='medium', help_text=_('Size to be displayed'))
    alignment = models.CharField(_('Position'), max_length=20, choices=ALIGNMENT, default='left')




# Create your models here.
