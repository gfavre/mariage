from django.utils.translation import ugettext as _
from django.conf import settings

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from cmsplugin_photologue.models import PhotologueGalleryPlugin

class GalleryPlugin(CMSPluginBase):
    model = PhotologueGalleryPlugin
    name = _("Galerie photo")
    render_template = "gallery/gallery.html"
    
    def render(self, context, instance, placeholder):
        context.update({'gallery': instance.gallery, 'placeholder':placeholder})
        return context

plugin_pool.register_plugin(GalleryPlugin)



class PhotoPlugin(CMSPluginBase):
    model = PhotologueGalleryPlugin
    name = _("Photo seule")
    render_template = "gallery/photo.html"
    
    def render(self, context, instance, placeholder):
        context.update({'gallery': instance.gallery, 'placeholder':placeholder})
        return context

plugin_pool.register_plugin(PhotoPlugin)

