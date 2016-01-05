from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls import patterns



urlpatterns = [
    # Examples:
#para ejemplos     url(r'^$', 'Project_django.views.index', name='index'),
     url(r'^$', 'Project_django.views.user_login', name='login'),
     url(r'^logout/$', 'Project_django.views.user_logout', name='logout'),     
     url(r'^curso1/', include('Project_django.apps.curso1.urls' , namespace="curso1")),
     url(r'^terminal/', include('Project_django.apps.terminal_venta.urls' , namespace="terminal")),
     url(r'^media/(?P<path>.*)$','django.views.static.serve',
	       {'document_root':settings.MEDIA_ROOT,}
	),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
                       
if settings.DEBUG:
    urlpatterns += patterns('',                            
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes':True}),
)