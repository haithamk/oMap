from piston.handler import BaseHandler, AnonymousBaseHandler
from map_info.models import Point, Layer
from django.contrib.auth.models import User
from django.contrib.gis.measure import D  # ``D`` is a shortcut for ``Distance``


####### Get Layers Names Handler ##################################################################

class GetLayersNamesAnonymousHandler(AnonymousBaseHandler):
   model = Layer
   fields = ('data_type')


class GetLayersNamesHandler(BaseHandler):
    'api handler for layer/names/'

    allowed_methods = ('GET',)
    model = Layer
    anonymous = GetLayersNamesAnonymousHandler
    fields = ('name', )
   # fields = (('user',('username')),)

    def read(self, request):
        #return Layer.objects.get(name= layer_name).points.all()
        return Layer.objects.all()



####### Search Within Handler #####################################################################

class SearchWithinAnonymousHandler(AnonymousBaseHandler):
   model = Point
   fields = ('data_type')


class SearchWithinHandler(BaseHandler):
    'api handler for point/search/layer=<layer>&within=<polygon>'
    
    allowed_methods = ('GET',)
    model = Point
    anonymous = SearchWithinAnonymousHandler
    fields = ('subject', 'description', 'point', 'date_added', 'report_date','layer', 'name', 'id', )
   # fields = (('user',('username')),)
    exclude = ( 'objects')

    def read(self, request, layer_name, polygon):
        #return Layer.objects.get(name= layer_name).points.all()
        poly = "POLYGON((-70 80, -50 -75, 160 -70, 160 70, -70 80))"
        poly2 = "POLYGON((30 40, 30 25, 40 25, 40 40, 30 40))"
        return Layer.objects.get(name = layer_name).points.filter(point__within = poly)


####### Search Around Handler #####################################################################


class SearchAroundAnonymousHandler(AnonymousBaseHandler):
   model = Point
   fields = ('data_type')


class SearchAroundHandler(BaseHandler):
    'api handler for point/search/layer=<layer>&around=<point>&r=<distance>'

    allowed_methods = ('GET',)
    model = Point
    anonymous = SearchAroundAnonymousHandler
    fields = ('subject', 'description', 'point', 'date_added', 'report_date','layer', 'name', 'id', )
   # fields = (('user',('username')),)
    exclude = ( 'objects')

    def read(self, request, layer_name, point, distance):
        #return Layer.objects.get(name= layer_name).points.all()
        pnt = "POINT (19.0722656215841013 -10.3149192839854464)"
        dst = D(m=5)
        return Layer.objects.get(name = layer_name).points.filter(point__distance_lte=(pnt, dst))



