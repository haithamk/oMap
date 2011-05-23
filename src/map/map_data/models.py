from django.contrib.gis.db import models
from django.contrib.auth.models import User
from django.contrib.gis import admin

class BaseData(models.Model):
    data_type = models.TextField()
    user = models.ForeignKey(User)
    location = models.PointField()
    objects = models.GeoManager()
    date = models.DateField()

class Data1(BaseData):
     data =  models.TextField()

admin.site.register(Data1, admin.OSMGeoAdmin)


class Data2(models.Model):
     data_type =  models.TextField()
     data =  models.TextField()
     user = models.ForeignKey(User)
     date = models.DateField()
     location = models.PointField()
     objects = models.GeoManager()

admin.site.register(Data2, admin.OSMGeoAdmin)
