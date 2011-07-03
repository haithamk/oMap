"""

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

    """ Layers model

    holds information about the supported layers. each layer has a unique name
    which is it's primary key. and a reference to the user who created it.

    Layer has related key called points that retrieves the points of the
    layer.

    class variables:
     * **name**: layer name, string.
     * **owner**: the user who created the layer, User.


    """

    name = models.TextField(primary_key=True, verbose_name="Layer name:")
    owner = models.ForeignKey(User, related_name='layers')

    def  __unicode__(self):
        return self.name




class Point(models.Model):

    """Data holder.

    Point instance holds the data and metadata of 1 report. points has an
    automatic id as primary key.

    Point has 2 related names:
     * User with related_name='points'
     * Layer with related_name='points'

    Class variables:
     * **layer**: the layer of the point. determined by the type of data.And defined
       by a foreign key to a layer model.
     * **user**: the user who added the point. a foreign key to a User model.
     * **point**: a latitude/ longitude point that represent the place of the data
       on the map.
     * **date_added**: date of adding the point to the database. Auto generated\
      field.
     * **report_date**: the date in which the data where collected.
     * **address**: text field, a human readable address.
     * **subject**: the report subject/title (very short, describes the what the\
      report is all about).
     * **description**: a short description of the data (few sentences)
     * **file**: DEPRECATED a path to the data file on the hard disk (not in use\
       currently).
     * **view_count**: counter for how many times the point was viewed.
     * **objects**: used by geodjango. enables geographical queries.

    """

    layer = models.ForeignKey(Layer, related_name='points')
    user = models.ForeignKey(User, related_name='points')
    point = models.PointField()
    date_added = models.DateField(auto_now_add=True)
    report_date = models.DateField()
    address = models.TextField()
    subject = models.TextField()
    description = models.TextField()
    file = models.FilePathField()
    views_count = models.IntegerField()
    objects = models.GeoManager()

     #TODO  add more fields and base methods


class Comment(models.Model):

    """ Represents a comment on some point.

    represents a text entered by a user as a comment on some point.

    Class variables:
     * **created**: date of the comment. auto generated field.
     * **author**: the author of the comment.
     * **body**: the text of the comment.
     * **point**: the point that this comment was made on.

    Comment model is related to the User model with related_name='comments'.
    And related to the point model with related_name='comments'

    .. note::
     All the comments are stored in one table.
     

    """

    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, related_name='comments')
    body = models.TextField()
    point = models.ForeignKey(Point, related_name='comments')

    def __unicode__(self):
        return unicode("%s: %s" % (self.point, self.body[:60]))


class Area(models.Model):
    """used to describe an area of authority

    Currently not in use.

    .. todo::
     Add Area feature.

    """

    multipolygon = models.MultiPolygonField()
