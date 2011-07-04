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
	

	self.jacob = User.objects.create_user('jacob', 'jacob@jacob.org','JKM')
        self.valentino = User.objects.create_user('valentino', 'valentino@valentino.org','JKM')#############
	c = Client()
	response = c.post('/accounts/login/', {'username': 'haitham', 'password': '12345'})
	self.assertEqual(response.status_code, 200)
	
	###########ADDING LAYERS ################
	self.layer1 = Layer.objects.create(name='layer 1', owner=self.jacob)
	self.layer2 = Layer.objects.create(name='layer 5', owner=self.jacob)	
	self.layer3 = Layer.objects.create(name='layer 2', owner=self.valentino)
	
	
	
	

 def testMainView(self):
	
  res = self.client.get(reverse('map_info.views.main'))
	
  self.assertEqual(res.status_code, 200)
	
  self.assertTemplateUsed(res, 'site/index.html')
	

  c = Client()
  response = c.post('/accounts/login/', {'username': 'haitham', 'password': '12345'})
  self.assertEqual(response.status_code, 200)


####### FIRST POINT ###########
  response1 = c.post('/map/add/', {'layer' : self.layer1, 
		'point' : 'POINT (32 32)', 'address' : 'whatever2',  
		'subject' : 'p1', 'description': 'This is p1', 'views_count':1,
		'report_date' : "2010-07-14"})
  self.assertEqual(response1.status_code, 200)
	
	
	####### SECOND POINT ###########
  response1 = c.post('/map/add/', {'layer' : self.layer2, 
		'point' : 'POINT (34 34)', 'address' : 'whatever3',  
		'subject' : 'p2', 'description': 'This is p2', 'views_count':6,
		'report_date' : "2010-07-14"})
  self.assertEqual(res.status_code, 200)
		
	####### THIRD POINT ###########
  response1 = c.post('/map/add/', {'layer' : self.layer3, 
		'point' : 'POINT (36 36)', 'address' : 'whatever3',  
		'subject' : 'p3', 'description': 'This is p3', 'views_count':3,
		'report_date' : "2010-07-14"})
  self.assertEqual(res.status_code, 200)

  res = self.client.get(reverse('map_info.views.main'))
	
  self.assertEqual(res.status_code, 200)
	
  self.assertTemplateUsed(res, 'site/index.html')
  
  self.assertEqual(len(res.context['points']), 0)

	
 def tearDown(self):
	
  self.layer1.delete()
  self.layer2.delete()
  self.layer3.delete()
	
  self.jacob.delete()

