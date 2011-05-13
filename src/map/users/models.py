
from django.db import models
from map.environmental_data.models import Region

class UserBasic(models.Model):
    'common fields for all users'
    user_name = models.CharField("user name",max_length=64, primary_key = True)
    name = models.CharField("full name",max_length=64)
    password = models.CharField("password",max_length=64)  #Haitham: is this the right way to do it? is it safe?
    email = models.EmailField("email address",blank=True, null=True)
    register_data = models.DateField("registration date")

    class Meta:
        abstract = True

class User(UserBasic):
    'regular users aka citizens'
    address =  models.CharField("home address", max_length = 100, blank = True) #maybe be changed for more efficient navigation. maybe to divide the map to regions
    auto_update_addresses = None # a list of addresses for the auto update

#---------------------=====================---------------------

class SuperUser(UserBasic):
    'can add data aka local authorities'
    position = models.CharField("user title", max_length = 64)
    region = models.ForeignKey(Regions)   #The region for this user

#---------------------=====================---------------------

class Moderator(UserBasic):
    'supervise the data and user comments'
    position = models.CharField("user title", max_length = 64)

#---------------------=====================---------------------

class Admin(UserBasic):
    'can add superusers and moderators'