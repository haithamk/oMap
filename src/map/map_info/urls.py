from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^view/(?P<point_id>[^/]+)/$','map_info.views.view_detailed'),
    (r'^add/$','map_info.views.add_point'),
    (r'^$', 'map_info.views.main'),
)