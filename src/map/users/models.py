
from django.db import models
from map.environmental_data.models import Region

class UserBasic(models.Model):
    'common fields for all users'
    user_name = models.TextField("user name", primary_key = True)
    name = models.TextField("full name")
    password = models.TextField("password")  #Haitham: is this the right way to do it? is it safe?
    email = models.EmailField("email address",blank=True, null=True)
    register_data = models.DateField("registration date")

    class Meta:
        abstract = True

class User(UserBasic):
    'regular users aka citizens'
    address =  models.TextField("home address", blank = True) #maybe be changed for more efficient navigation. maybe to divide the map to regions
    auto_update_addresses = None # a list of addresses for the auto update

#---------------------=====================---------------------

class SuperUser(UserBasic):
    'can add data aka local authorities'
    position = models.TextField("user title")
    region = models.ForeignKey(Regions)   #The region for this user

#---------------------=====================---------------------

class Moderator(UserBasic):
    'supervise the data and user comments'
    position = models.TextField("user title")

#---------------------=====================---------------------

class Admin(UserBasic):
    'can add superusers and moderators'