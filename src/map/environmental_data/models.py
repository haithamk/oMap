from django.db import models
from map.users.models import User


class BaseLayer(models.Model):
    location = None #poisiton as defined in the GIS

class DataLayer(models.Model):
# each layer is a table inside the database the data are defined for each Layer alone
    'environmental data'
    layer_name =  models.CharField(max_length=64)

    date = models.DateField
    data1 = None
    data2 = None
    #data3 ......

#---------------------=====================---------------------

class Comment(models.Model):
    user = models.ForeignKey(BasicUser)
    comment =  models.CharField(max_length = 400)

#---------------------=====================---------------------

class Region(models.Model):
    area = None # use polygon/multipolygon from GIS

#---------------------=====================---------------------
