from piston.handler import BaseHandler, AnonymousBaseHandler
from models import BaseData

class AnonymousDataHandler(AnonymousBaseHandler):
   model = BaseData
   fields = ('data_type')


class DataHandler(BaseHandler):
    allowed_methods = ('GET',)
    model = BaseData
    anonymous = AnonymousDataHandler

    def read(self, request, id=None):
        return BaseData.objects.all()