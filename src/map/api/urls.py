from django.conf.urls.defaults import *
from piston.resource import Resource


from handlers import GetWithinHandler, GetDistanceLessHandler, GetLayersNamesHandler

getdata_withitn_handler = Resource(GetWithinHandler)
getdata_distance_less_handler = Resource(GetDistanceLessHandler)
getdata_layers_names = Resource(GetLayersNamesHandler)

urlpatterns = patterns('',
    url(r'^getdata/layers-names', getdata_layers_names, { 'emitter_format': 'json' }),
    url(r'^getdata/(?P<layer_name>[^/]+)/within/(?P<polygon>[^/]+)/', getdata_withitn_handler, { 'emitter_format': 'json' }),
    url(r'^getdata/(?P<layer_name>[^/]+)/distance-less/(?P<point>[^/]+)/(?P<distance>[^/]+)/', getdata_distance_less_handler, { 'emitter_format': 'json' }),
)