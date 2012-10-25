from django.utils.translation import ugettext as _
from django.conf import settings

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from cmsplugin_photologue.models import PhotologueGalleryPlugin

class CMSSlideshowPlugin(CMSPluginBase):
    model = PhotologueGalleryPlugin
    name = _("Sideshow")
    render_template = "plugins/slideshow.html"
    
    def render(self, context, instance, placeholder):
        context.update({'gallery': instance.gallery, 'placeholder':placeholder})
        return context

plugin_pool.register_plugin(CMSSlideshowPlugin)