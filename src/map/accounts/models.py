from django.db import models
from django.contrib.auth.models import User


#big TODO : complete UserProfile fields
class UserProfile(models.Model):
    """Additional user information

    This class is supposed to hold the user details that are not holden in
    auth.User.

    .. note::
     Currently not in use.

    """

    user = models.ForeignKey(User, unique=True)
    url = models.URLField("Website", blank=True)
    address = models.TextField("address")
