from django.utils.translation import ugettext as _
from django.conf import settings

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from cmsplugin_photologue.models import PhotologueGalleryPlugin
from photologue.models import Photo

from models import SizedPhotologuePhotoPlugin

class GalleryPlugin(CMSPluginBase):
    model = PhotologueGalleryPlugin
    name = _("Galerie photo")
    render_template = "gallery/gallery.html"
    
    def render(self, context, instance, placeholder):
        context.update({'gallery': instance.gallery, 'placeholder':placeholder})
        return context

plugin_pool.register_plugin(GalleryPlugin)



class PhotoPlugin(CMSPluginBase):
    model = SizedPhotologuePhotoPlugin
    name = _("Photo seule")
    render_template = "gallery/photo.html"
    
    def render(self, context, instance, placeholder):
        thumbnail_url = getattr(instance.photo, 'get_%s_url' % instance.size)()
        size_to_twitterbootstrap = {'thumbnail': 'span2',
                                    'medium': 'span4',
                                    'full': 'span9'}
        alignment_to_twitterbootstrap = {'left': 'pull-left', 'right': 'pull-right'}
        context.update({'photo':instance.photo, 'placeholder':placeholder})
        context.update({'slug_field': 'title_slug',
                        'thumbnail_url': thumbnail_url, 
                        'queryset': Photo.objects.filter(is_public=True), 
                        'size': size_to_twitterbootstrap[instance.size], 
                        'position': alignment_to_twitterbootstrap[instance.alignment]
                       })
        return context

plugin_pool.register_plugin(PhotoPlugin)

