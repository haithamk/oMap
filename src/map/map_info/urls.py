from django.conf.urls.defaults import *


urlpatterns = patterns('',
    (r'^point/view/(\d+)/$','map_info.views.view_detailed'),
    (r'^point/add_comment/(\d+)/$','map_info.views.add_comment'),
    (r'^add/$','map_info.views.add_point'),
    (r'^getfile/(?P<file>.*)/$','map_info.views.get_file'),
    (r'^$', 'map_info.views.main'),
)