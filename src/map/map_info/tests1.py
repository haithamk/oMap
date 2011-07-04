from django.test import TestCase
 	
from django.test.client import Client
	
from django.core.urlresolvers import reverse
	
from django.contrib.gis.geos import *
	
from django.contrib.auth.models import User, AnonymousUser
	
from django import template

import time
	
#from knesset.mks.server_urls import mock_pingback_server
	
from django.utils import simplejson as json
	
	
from models import Layer, Point
	

	
just_id = lambda x: x.id
	

	
class ViewsTest(TestCase):
	

	
 def setUp(self):
	#TODO maybe better to separate them into couple of tests
	
	#adding users
	self.jacob = User.objects.create_user('jacob', 'jacob@jacob.org','JKM')
	
	self.valentino = User.objects.create_user('valentino', 'valentino@valentino.org','JKM')#############

	self.layer = Layer.objects.create(name='layer 1', owner=self.jacob)
	
	self.layer = Layer.objects.create(name='layer 2', owner=self.valentino)	
	
	####### FIRST POINT ###########
	self.p1 = Point.objects.create(user = self.jacob, layer = self.layer, 
		point='POINT (31 31)', subject = 'p1', description= 'This is p1',
		report_date = "2010-07-14", views_count = 0, date_added = "2010-07-11")
		

	####### SECOND POINT ###########
	self.p2 = Point.objects.create( layer = self.layer, user = self.jacob,
		point = 'POINT (32 32)', address = 'whatever2',  
		subject = 'p2', description= 'This is p2', views_count=1,
		report_date = "2010-07-14", date_added = "2010-07-12")

	###########ADDING LAYERS ################
	self.layer2 = Layer.objects.create(name='layer 5', owner=self.jacob)
		
	####### THIRD POINT ###########
	self.p3 = Point.objects.create(user = self.jacob, layer = self.layer, 
		point =  'POINT (34 34)', address= 'whatever3' ,
		subject = 'p3', description= 'This is p3',views_count=6,
		report_date = "2010-07-14", date_added = "2010-07-13")
	
	self.layer3 = Layer.objects.create(name='layer 6', owner=self.jacob)
	
	####### FOURTH POINT ###########
	self.p4 = Point.objects.create( layer = self.layer3, user = self.jacob,
		point = 'POINT (36 36)',  address = 'whatever4',  
		subject = 'p4', description= 'This is p4', views_count=2,
		report_date = "2010-07-14", date_added = "2010-07-14")

	

 def testMainView(self):
	
  res = self.client.get(reverse('map_info.views.main'))
	
  self.assertEqual(res.status_code, 200)
	
  self.assertTemplateUsed(res, 'site/index.html')
	
  self.assertEqual(map(just_id, res.context['points']), [ self.p1.id, self.p2.id, self.p3.id, self.p4.id , ])

	#we can't check this because the of the date resolution
  #self.assertEqual(map(just_id, res.context['most_recent']), [ self.p4.id, self.p3.id, self.p2.id,  ])

  self.assertEqual(map(just_id, res.context['hot_topics']), [self.p3.id, self.p4.id, self.p2.id, ])


 # delete points, but i am not sure if possible, since the tear down will delete everything anyway ... 
  self.p1.delete()
  #Point.objects.get(id = self.p1.id).delete()
  res = self.client.get(reverse('map_info.views.main'))
  self.assertEqual(map(just_id, res.context['points']), [self.p2.id, self.p3.id, self.p4.id ,])
 
  self.p2.delete()
  res = self.client.get(reverse('map_info.views.main'))
  self.assertEqual(map(just_id, res.context['points']), [ self.p3.id, self.p4.id ,])
 	
 def tearDown(self):
	
  self.p3.delete()
	
  self.p4.delete()
	
  self.layer.delete()
	
  self.jacob.delete()
