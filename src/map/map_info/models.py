"""
Models and Manager for map information
======================================

>>> miki= User.objects.create_user('miki', 'miki', 'miki')
>>> layer=Layer.objects.create(name='first layer', description='This is the first layer',owner=miki)
>>> point=SimplePoint.objects.create(name='a point', description='This is the first point', layer=layer,
>>>                                  owner=miki, point=...)
>>> points=layer.points.all()
>>> points.count()
1
>>> points[0].name
a point
>>> areas=layer.areas.all()
>>> areas.count()
0
>>> area=SimpleArea.objects.create(name='an area', description='This is the first area', layer=layer, 
                                   polygon=....)
>>> areas.count()
1
"""

from django.contrib.gis.db import models
from django.contrib.auth.models import User

class Layer(models.Model):
    owner = models.ForeignKey(User, related_name='points')
    pass

class BasePoint(models.Model):0
    layer = models.ForeignKey(Layer, related_name='points')
    owner = models.ForeignKey(User, related_name='points')
    point = models.PointField()
    #TODO  add more fields and base methods

class SimplePoint(BasePoint):
    pass
