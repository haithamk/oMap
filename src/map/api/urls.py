from django.conf.urls.defaults import *
from piston.resource import Resource


from handlers import SearchWithinHandler, SearchAroundHandler, GetLayersNamesHandler

search_withitn_handler = Resource(SearchWithinHandler)
search_around_handler = Resource(SearchAroundHandler)
getdata_layers_names = Resource(GetLayersNamesHandler)

urlpatterns = patterns('',
    url(r'^layer/names/', getdata_layers_names, { 'emitter_format': 'json' }),
    url(r'^point/search/layer=(?P<layer_name>[^&]+)&within=(?P<polygon>[^/]+)/', search_withitn_handler, { 'emitter_format': 'json' }),
    url(r'^point/search/layer=(?P<layer_name>[^&]+)&around=(?P<point>[^&]+)&r=(?P<distance>[^/]+)/', search_around_handler, { 'emitter_format': 'json' }),
)