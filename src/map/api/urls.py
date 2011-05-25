from django.conf.urls.defaults import *
from piston.resource import Resource


from handlers import DataHandler

data_handler = Resource(DataHandler)

urlpatterns = patterns('',
    url(r'^getdata/(?P<polygon>[^/]+)/', data_handler),
)