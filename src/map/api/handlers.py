from piston.handler import BaseHandler, AnonymousBaseHandler
from map_info.models import Point, Layer
from django.contrib.auth.models import User
from django.contrib.gis.measure import D  # ``D`` is a shortcut for ``Distance``


####### Get Layers Names Handler ##############################################
class GetLayersNamesAnonymousHandler(AnonymousBaseHandler):
    """Anonymous user handler for layers info.

    Anonymous users have a read access to the layers names.

    """
    model = Layer
    fields = ('name',)


class GetLayersNamesHandler(BaseHandler):
    """Authenticated users handler for layers info.

    Authenticated users have a read access to the layers names,
    Write and update access are not available at this stage.

    """

    allowed_methods = ('GET',)
    model = Layer
    anonymous = GetLayersNamesAnonymousHandler
    fields = ('name', )

    def read(self, request):
        """returns all layers."""
        
        return Layer.objects.all()



####### Search Within Handler #################################################

class SearchWithinAnonymousHandler(AnonymousBaseHandler):
    """Anonymous user handler for search within quires.

    Anonymous user can see only the points id and layer.

    """
    
    model = Point
    fields = ('id', 'layer', )


class SearchWithinHandler(BaseHandler):
    """Authenticated user handler for search within quires.

    Searches for all points inside the borders of a given polygon.
    Authenticated request have read access to:
      subject, description, point, address, date_added, report_date, layer,
      name, id.
     Write and update access are not available at this stage.
     'api handler for point/search/layer=<layer>&within=<polygon>'

    """

    allowed_methods = ('GET',)
    model = Point
    anonymous = SearchWithinAnonymousHandler
    fields = ('subject', 'description', 'point', 'address', 'date_added',
              'report_date','layer', 'name', 'id', )
   # fields = (('user',('username')),)
    exclude = ( 'objects')

    def read(self, request, layer_name, polygon):
        """ returns all points of a given layer inside a given polygon.

        Keyword arguments:
        layer_name: the layer name.
        polygon: the polygon.

        """

        poly = "POLYGON((-70 80, -50 -75, 160 -70, 160 70, -70 80))"
        poly2 = "POLYGON((30 40, 30 25, 40 25, 40 40, 30 40))"
        return Layer.objects.get(name = layer_name).points.filter(
            point__within = poly)


####### Search Around Handler #################################################


class SearchAroundAnonymousHandler(AnonymousBaseHandler):
    """Anonymous user handler for search around quires.

    Anonymous user can see only the points id and layer.

    """

    model = Point
    fields = ('id', 'layer', )


class SearchAroundHandler(BaseHandler):
    """Authenticated user handler for search around quires.

    Searches for all points with a given distance from a given point.
    Authenticated request have read access to:
      subject, description, point, address, date_added, report_date, layer,
      name, id.
    Write and update access are not available at this stage.
    'api handler for point/search/layer=<layer>&around=<point>&r=<distance>'

    """

    allowed_methods = ('GET',)
    model = Point
    anonymous = SearchAroundAnonymousHandler
    fields = ('subject', 'description', 'point', 'address', 'date_added',
              'report_date','layer', 'name', 'id', )
    exclude = ( 'objects')

    def read(self, request, layer_name, point, distance):
        """returns points in a given distance from a given point in given layer

        Keyword arguments:
        layer_name: the layer name.
        point: the point. The center of the circle.
        distance: the radius of the circle.
        
        """
        pnt = "POINT (19.0722656215841013 -10.3149192839854464)"
        dst = D(m=5)
        return Layer.objects.get(name = layer_name).points.filter(
            point__distance_lte=(pnt, dst))



