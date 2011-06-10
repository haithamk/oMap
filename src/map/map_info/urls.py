from django.conf.urls.defaults import *

urlpatterns = patterns('',
    
    (r'^add/$','map_info.views.add_point'),
    (r'^$', 'map_info.views.main'),
)