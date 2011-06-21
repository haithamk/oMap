from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import redirect_to
from django.views.static import *
from django.conf import settings


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^map/', include('map_info.urls')),
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    (r'^accounts/', include('accounts.urls')),
    (r'^api/', include('api.urls'), { 'emitter_format': 'json' }),
     # Required to make static serving work
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    (r'^/$', redirect_to, {'url': '/map/'}),

    # Examples:
    # url(r'^$', 'map.views.home', name='home'),
    # url(r'^map/', include('map.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
