from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.http import HttpResponse
from django.views.generic.simple import redirect_to


from cms.sitemaps import CMSSitemap
from photologue.models import Photo

admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'^photologue/', include('photologue.urls')),
    (r'^tinymce/', include('tinymce.urls')),
    (r'^accounts/login/$', 'django.contrib.auth.views.login'),
    (r'^google7f92da28d3dd66e7\.html$', lambda r: HttpResponse("google-site-verification: google7f92da28d3dd66e7.html", mimetype="text/plain")),
    url(r'^sitemap.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': {'cmspages': CMSSitemap}}),
    url(r'^robots.txt$', redirect_to, {'url': settings.STATIC_URL + 'robots.txt', 'permanent': True}),
    url(r'^favicon.ico$', redirect_to, {'url': settings.STATIC_URL + 'favicon.ico', 'permanent': True}),
    url(r'^apple-touch-icon.png$', redirect_to, {'url': settings.STATIC_URL + 'apple-touch-icon.png', 'permanent': True}),
    url(r'^humans.txt$', redirect_to, {'url': settings.STATIC_URL + 'humans.txt', 'permanent': True}),
    url(r'^', include('cms.urls')),
)



if settings.DEBUG:
    urlpatterns = patterns('',
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    url(r'', include('django.contrib.staticfiles.urls')),
) + urlpatterns


#Monkeypatches
Photo._meta.ordering = ['date_added']
