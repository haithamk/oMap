from django.conf.urls.defaults import *

urlpatterns = patterns('',
                        (r'^login/$',
                        "accounts.views.mylogin"),

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
                        "accounts.views.logout"),

                        (r'^profile/$',
                        'accounts.views.profile'),

                        (r'^public/(?P<name>[^&]+)/$',
                        'accounts.views.public'),

                        (r'^user-comments/(?P<name>[^&]+)/$',
                        'accounts.views.user_comments'),

                         (r'^user-points/(?P<name>[^&]+)/$',
                        'accounts.views.user_points'),
)