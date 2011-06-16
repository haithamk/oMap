from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from django.contrib.auth import logout, login

from django.template import RequestContext

from django.core.urlresolvers import reverse

from accounts.forms import UserCreationForm

from django.http import HttpResponseRedirect

from django.utils.http import base36_to_int

from django.conf import settings

from map_info.models import Point




def mylogin(request):
    if request.method=='GET':
       # return views.login(request, 'accounts/login.html', '/map')
        return render_to_response('accounts/login.html')
    else:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('/map', request)
            else:
                 return render_to_response('accounts/login.html', {'msg' : 'Unactivated account'})
        else:
            return render_to_response('accounts/login.html', {'msg' : 'Invalid login'})
    return redirect('/map',RequestContext( request))

def add_user(request):
    user = User.objects.create_user('haitham', 'lennon@thebeatles.com', '12345')
    user.save()

 #   if request.POST:
 #       username = request.POST['username']
 #       password = request.POST['password']
 #       user = authenticate(username=username, password=password)
 #       if user is not None:
 #           login(request, user)
 #           return render_to_response('accounts/login_success.html')
 #       else:
 #           return render_to_response('accounts/login_fail.html')
 #   else:
 #       #return render_to_response('accounts/login_fail.html')
 #       return render_to_response('accounts/login.html', {'title': ('Log in')})


def signup(request, template_name='registration/signup.html',
           email_template_name='registration/signup_email.html',
           signup_form=UserCreationForm,
           token_generator=default_token_generator,
           post_signup_redirect=None):
    if post_signup_redirect is None:
        post_signup_redirect = reverse('accounts.views.signup_done')
    if request.method == "POST":
        form = signup_form(request.POST)
        if form.is_valid():
            opts = {}
            opts['use_https'] = request.is_secure()
            opts['token_generator'] = token_generator
            opts['email_template_name'] = email_template_name
            if not Site._meta.installed:
                opts['domain_override'] = RequestSite(request).domain
            form.save(**opts)
            return HttpResponseRedirect(post_signup_redirect)
    else:
        form = signup_form()
    return render_to_response(template_name, {'form': form,},
                              context_instance=RequestContext(request))

def signup_done(request, template_name='registration/signup_done.html'):
    return render_to_response(template_name,
                              context_instance=RequestContext(request))

def signup_confirm(request, uidb36=None, token=None,
                   token_generator=default_token_generator,
                   post_signup_redirect=None):
    assert uidb36 is not None and token is not None #checked par url
    if post_signup_redirect is None:
        post_signup_redirect = reverse('accounts.views.signup_complete')
    try:
        uid_int = base36_to_int(uidb36)
    except ValueError:
        raise Http404

    user = get_object_or_404(User, id=uid_int)
    context_instance = RequestContext(request)

    if token_generator.check_token(user, token):
        context_instance['validlink'] = True
        user.is_active = True
        user.save()
    else:
        context_instance['validlink'] = False
    return HttpResponseRedirect(post_signup_redirect)

def signup_complete(request, template_name='registration/signup_complete.html'):
    return render_to_response(template_name,
                              context_instance=RequestContext(request,
                                                              {'login_url': settings.LOGIN_URL}))

def logout(request):
    views.logout(request)
    return redirect('/map', request)


@login_required
def profile(request):
    return render_to_response('accounts/profile.html',context_instance=RequestContext(request))

@login_required
def public(request, name):
    try:
        user = User.objects.get(username = name)
    except:
        title = "Error"
        msg = "User doesn't exist"
        return render_to_response('site/msg.html', {'title' : title,'msg': msg, 'user' : request.user,})
    context_instance=RequestContext(request, {'name': name})
    return render_to_response('accounts/public_profile.html', context_instance)