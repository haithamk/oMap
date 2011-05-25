from piston.handler import BaseHandler, AnonymousBaseHandler
from map_data.models import Data1
from django.contrib.auth.models import User

class AnonymousDataHandler(AnonymousBaseHandler):
   model = Data1
   fields = ('data_type')


class DataHandler(BaseHandler):
    allowed_methods = ('GET',)
    model = Data1
    anonymous = AnonymousDataHandler
    fields = ('data_type', 'date', 'data', 'location', ('user',()))
    exclude = ( 'objects')

    def read(self, request, polygon=None):
        return Data1.objects.all()