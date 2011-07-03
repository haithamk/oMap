from django.shortcuts import render_to_response, redirect, HttpResponseRedirect
from map.map_info.models import Point, Layer, Comment
from map.map_info.forms import AddPointForm, CommentForm
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.conf import settings
import os

def main(request):
    """ returns home page rendered html.

    renderer the index.html page according to the context of the request and\
    returns it to the user.

    """

    all_points = list(Point.objects.all())
    most_recent = list(Point.objects.all().order_by('-date_added')[0:3])
    hot_topics = list(Point.objects.all().order_by('-views_count')[0:3])
    if request.user.is_authenticated():
        user = request.user
    else:
        user = None
    dict = {'user': user, 'points': all_points, 'most_recent': most_recent, 'hot_topics' : hot_topics}
    return render_to_response('site/index.html',  RequestContext(request,dict))


def add_point(request):
    """ handles new data addition.

    only logged in user that have the permissions to add a point can add points
    anonymous user and logged in user with no permissions will be redirected to
    error page with a explanation message.

    for GET request the method will render add_point.html page and return it.
    for POST request the method will check if the data is valid. and if
    valid it will add the new data to the data base. otherwise the
    add_point.html will be returned to the user with error message.

    POST requests includes a data file. the file will be saved to the hard disk
    in the following path: media/data/<point.id>/<file>. the file is written
    using handle_uploaded_file method.
    
    if the new data is added successfully the user will be redirected to the
    home page.
    
    """

    user = request.user
    if(not request.user.is_authenticated()):
        title = "Error"
        msg = "You are not logged in!"
        return render_to_response('site/msg.html', {'title' : title,'msg': msg, 'user' : request.user,})
    if(not request.user.has_perm('map_info.add_point')):
        title = "Error"
        msg = "You don't have permissions to access this page"
        return render_to_response('site/msg.html', {'title' : title,'msg': msg, 'user' : request.user,})
    if request.method == 'POST':
        form = AddPointForm(request.POST, request.FILES)
        if(form.is_valid()):
            point_ = form.cleaned_data['point']
            date_ = form.cleaned_data['report_date']
            layer_= form.cleaned_data['layer']
            subject_ = form.cleaned_data['subject']
            description_ = form.cleaned_data['description']
            #file_ = form.cleaned_data['file']
            file_ = "00"
            data = Point(user = request.user, layer = layer_, point = point_, subject = subject_, description= description_, file =file_, report_date = date_, views_count = 0)
            data.save()
            id = data.id

            file_name = request.FILES['file'].name
            handle_uploaded_file(request.FILES['file'], id, file_name)
            
            return redirect('/map/', request)
        return render_to_response('site/add_point.html', RequestContext(request,{'form': form,}))
    else:
        form = AddPointForm()
        return render_to_response('site/add_point.html', RequestContext(request, {'form': form, 'user' : request.user,}))

def handle_uploaded_file(f, id, file_name):
    """Saves a file to the disk.


    :param f: file.
    :param id: id of the point for the file.
    :param file_name: the file name.

    The method creates a new directory under media/data with the id as a name\
    and saves the file (f) to the new directory with the name: file_name.

    """

    data_root = os.path.join(settings.DATA_ROOT, str(id))
    if not os.path.exists(data_root):
        os.makedirs(data_root)
    file_dest= data_root +"/" +  file_name
    destination = open(file_dest, 'wb+')
    for chunk in f.chunks():
        destination.write(chunk)
    destination.close()

def view_detailed(request, point_id):
    """ views the full details of a point.

    :param point_id: a point id to view.

    returns a rendered page of site/details.html for the received point id.
    the point details are retrieved from the data base and the  data file path
    is be built and returned.
 
    """
    point = Point.objects.get(id = point_id)
    point.views_count = point.views_count + 1
    point.save()
    title = point.point
    comments = point.comments.all()
    path = settings.MEDIA_ROOT + "/data/" + str(point_id)
    dirList=os.listdir(path)
   # file = "data/" + str(point_id) + ".pdf"
    file = "data/" + str(point_id) + "/" + dirList[0]
    dict = {'point': point, 'title': title, 'comments' : comments, 'form' : CommentForm(), 'file': file}
    return render_to_response('site/details.html',  RequestContext(request,dict))

def add_comment(request, point_id):
    """ add new comment.

    :param point_id: the id of the point to the the comment to.

    handles POST requests. the request is to add a new comment. the request
    specifies the comment text. the comment is added to the data base and will
    be linked to the point with id= point_id. the author of the comment is the
    the user who sent the request.    

    """

    p = request.POST

    if p.has_key("body") and p["body"]:
        author_ = request.user
        body_ =   p["body"]
        point_ = Point.objects.get(id = point_id)
        comment = Comment(author = author_, body = body_, point = point_)
        comment.save()

    return HttpResponseRedirect(reverse("map_info.views.view_detailed", args=[point_id]))


def get_file(request, file):
    """ returns static files

    :param file: relative file path, relative to the media dir.
    
    """
    
    return redirect('/media/data/' + file, request)
