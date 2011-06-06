from django.conf.urls.defaults import *

urlpatterns = patterns('',
#                        (r'^login/$', 'django.contrib.auth.views.login')
                        (r'^login/$',
                        #'django.contrib.auth.views.login',
                        "accounts.views.mylogin"),
                       # {'template_name': 'accounts/login.html',
                       #  'redirect_field_name': 'accounts/profile'}),

                        (r'^signup/$',
                        'accounts.views.signup',
                        {'template_name': 'accounts/signup_form.html',
                         'email_template_name': 'accounts/signup_email.html'}),

                        (r'^signup/done/$',
                        'accounts.views.signup_done',
                        {'template_name': 'accounts/signup_done.html'}),

                       (r'^signup/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$',
                        'accounts.views.signup_confirm'),

                       (r'^signup/complete/$',
                        'accounts.views.signup_complete',
                        {'template_name': 'accounts/signup_complete.html'}),

                       (r'^logout/$',
                        #'django.contrib.auth.views.login',
                        "accounts.views.logout"),





                        (r'^profile/$',
                        'accounts.views.profile')
)