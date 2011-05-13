#encoding: utf-8

from django.db import models

#Haitham:   (how models works? will the following model be defined in 1 database?)
#daonb: all models are deifned in one database - as define in the project's settings.py
#Haitham:   (what does foreign key means?)
#daonb: a one-to-many relationship, helping you connect two models using a 
#       direct, non-exclusive link from one models to another. 
#       please use the related_name of attributed of ForeignKey field to 
#       better name the reverse relationship.
#Haitham:   how the different model interact?
#daonb: using ForeignKeys and ManyToMany relatinshps for start
#Haitham:   can we change the models (add/remove fields) in the future?
#daonb: it's tricky, but the south app helps
#Haitham:   how to store user comments EFFICIENTLY? do we have to deal with it now?
#daonb: no. "We should forget about small efficiencies, say about 97% of the time: 
#       premature optimization is the root of all evil" Donald Knuth
#Haitham:   how the data is stored? by a stand alone data base for each layer (can layer be added dynamically by admins)?
#           or by a generic field in the data database (can we define a generic field)?
#           i guess that a stand alone data base for each layer is better
#daonb: not necessarly. we should keep the number of the 'moving parts' to a minimum and
#       sql databases are fully capble of handling all our layers in one database
#   where the physical data base will be created?
#   daonb: in the database defined in the project's settings.py
#   what is the optimal char fields length
#   daonb: use TextField and don't worry about running out of chars

class UserBasic(models.Model):
    'common fields for all users'
    user_name = models.CharField("user name",max_length=64, primary_key = True)
    name = models.CharField("full name",max_length=64)
    password = models.CharField("password",max_length=64)  #Haitham: is this the right way to do it? is it safe?
    email = models.EmailField("email address",blank=True, null=True)
    register_data = models.DateField("registration date")

class Users(UserBasic):
    'regular users aka citizens'
    address =  models.CharField("home address", max_length = 100, blank = True) #maybe be changed for more efficient navigation. maybe to divide the map to regions
    auto_update_adresses = None # a list of addresses for the auto update

#---------------------=====================---------------------

class SuperUsers(UserBasic):
    'can add data aka local authorities'
    position = models.CharField("user title", max_length = 64)
    region = models.ForeignKey(Regions)   #The region for this user

#---------------------=====================---------------------

class Moderators(UserBasic):
    'supervise the data and user comments'
    position = models.CharField("user title", max_length = 64)

#---------------------=====================---------------------

class Admins(UserBasic):
    'can add superusers and moderators'

#---------------------=====================---------------------

class DataLayer(models.Model):
# each layer is a table inside the database the data are defined for each Layer alone
    'environmental data'
    layer_name =  models.CharField(max_length=64)
    position = None #poisiton as defined in the GIS
    date = models.DateField
    data1 = None
    data2 = None
    #data3 ......

#---------------------=====================---------------------

class Comments(models.Model):
    user = models.ForeignKey(BasicUser)
    comment =  models.CharField(max_length = 400)

#---------------------=====================---------------------

class Regions(models.Model):
    area = None # use polygon/multipolygon from GIS

#---------------------=====================---------------------
