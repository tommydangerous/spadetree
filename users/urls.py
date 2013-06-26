from django.conf.urls import patterns, url

urlpatterns = patterns('users.views',
    url(r'^pick/$', 'pick'),

    url(r'^(?P<slug>[-\w]+)/choose/$', 'choose'),
    url(r'^(?P<slug>[-\w]+)/$', 'detail'),
    url(r'^(?P<slug>[-\w]+)/edit/$', 'edit'),
    url(r'^(?P<slug>[-\w]+)/reviews/new/$', 'new_review'),
    url(r'^(?P<slug>[-\w]+)/reviews/new(?P<format>.(js|json))/$', 'new_review'),
)