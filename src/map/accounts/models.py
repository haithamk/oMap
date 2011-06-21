from django.db import models
from django.contrib.auth.models import User


#big TODO : complete UserProfile fields
class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True)
    url = models.URLField("Website", blank=True)
    address = models.TextField("address")
