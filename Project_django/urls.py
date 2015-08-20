from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls import patterns

urlpatterns = [
    # Examples:
     url(r'^$', 'Project_django.views.index', name='index'),
     url(r'^login/$', 'Project_django.apps.curso1.views.login', name='login'),
     url(r'^curso1/', include('Project_django.apps.curso1.urls' , namespace="curso1")),
     url(r'^media/(?P<path>.*)$','django.views.static.serve',
	       {'document_root':settings.MEDIA_ROOT,}
	),
]
if settings.DEBUG:
    urlpatterns += patterns('',                            
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes':True}),
)