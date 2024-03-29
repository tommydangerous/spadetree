from django.conf.urls import patterns, url

urlpatterns = patterns('users.views',
    url(r'^pick/$', 'pick'),
    url(r'^pick(?P<format>.json)/$', 'pick'),
    url(r'^read-tutorial.json/$', 'read_tutorial'),
    url(r'^title-count.json/$', 'title_count'),
    url(r'^tutorial/', 'tutorial'),

    url(r'^(?P<slug>[-\w]+)/choose/$', 'choose'),
    url(r'^(?P<slug>[-\w]+)/choose(?P<format>.json)/$', 'choose'),
    url(r'^(?P<slug>[-\w]+)/$', 'detail'),
    url(r'^(?P<slug>[-\w]+)(?P<format>.json)/$', 'detail'),
    url(r'^(?P<slug>[-\w]+)/edit/$', 'edit'),
    url(r'^(?P<slug>[-\w]+)/edit(?P<format>.json)/$', 'edit'),
    url(r'^(?P<slug>[-\w]+)/friends-tutored/$', 'friends_tutored'),
    url(r'^(?P<slug>[-\w]+)/friends-tutored(?P<format>.json)/$', 
        'friends_tutored'),
    url(r'^(?P<slug>[-\w]+)/reviews/new/$', 'new_review'),
    url(r'^(?P<slug>[-\w]+)/reviews/new(?P<format>.(js|json))/$', 'new_review'),
    url(r'^(?P<slug>[-\w]+)/reviews.json/$', 'reviews'),
)