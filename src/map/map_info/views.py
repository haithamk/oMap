from django.shortcuts import render_to_response, redirect, HttpResponseRedirect
from map_info.models import Point, Layer, Comment
from map_info.forms import AddPointForm, CommentForm
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.conf import settings

def main(request):
    all_points = list(Point.objects.all())
    # TODO check what is the type of the user and redirect to the suitable home page

    if request.user.is_authenticated():
        dict = {'user': request.user, 'points': all_points}
    else:
        dict = {'user': None, 'points': all_points}
    return render_to_response('site/index.html',  RequestContext(request,dict))


def add_point(request):
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
            #TODO save the new data. figure out how to deal with layers and points
            point_ = "POINT (12.0722656215841013 -10.3149192839854464)"
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
            handle_uploaded_file(request.FILES['file'], id)
            
            return redirect('/map/', request)
        return render_to_response('site/add_point.html', {'form': form,})
    else:
        form = AddPointForm()
        return render_to_response('site/add_point.html', RequestContext(request, {'form': form, 'user' : request.user,}))

def handle_uploaded_file(f, name):
   # file_dest = os.path.join(DATA_ROOT, 'test');
    data_root = settings.DATA_ROOT
    file_dest= data_root +"/" + str(name) + ".pdf"
    destination = open(file_dest, 'wb+')
    for chunk in f.chunks():
        destination.write(chunk)
    destination.close()

def view_detailed(request, point_id):
    point = Point.objects.get(id = point_id)
    title = point.point
    comments = point.comments.all()
    file = "/data/" + str(point_id) + ".pdf"
    dict = {'point': point, 'title': title, 'comments' : comments, 'form' : CommentForm(), 'file': file}
    return render_to_response('site/details.html',  RequestContext(request,dict))



def add_comment(request, point_id):
    """Add a new comment."""
    p = request.POST

    if p.has_key("body") and p["body"]:
        author_ = request.user
        body_ =   p["body"]
        point_ = Point.objects.get(id = point_id)
        comment = Comment(author = author_, body = body_, point = point_)
        comment.save()

    return HttpResponseRedirect(reverse("map_info.views.view_detailed", args=[point_id]))


def get_file(request, file):
    return redirect('/media/data/' + file, request)
