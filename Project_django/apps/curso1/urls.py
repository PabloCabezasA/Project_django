from django.conf.urls import  url
from django.conf import settings
from Project_django.apps.curso1 import models
from Project_django.apps.curso1.views import AddAuthorView,ListAuthorView,EditAuthorView, DetailAuthorView,DeleteAutorView

urlpatterns = [
    # Examples:
    url(r'^$', 'Project_django.apps.curso1.views.index', name='index'),
#    url(r'^autor_autor_form/$', 'Project_django.apps.curso1.views.autor_autor_form', name='autor_autor_form'),
#    url(r'^autor_autor_form/edit/(?P<autor_id>\d+)/$', 'Project_django.apps.curso1.views.autor_autor_form', name='autor_autor_edit'),
#    url(r'^autor_autor_list/$', 'Project_django.apps.curso1.views.autor_autor_list', name='autor_autor_list'),
    url(r'^autor_autor_form/$', AddAuthorView.as_view(), name='autor-add'),
    url(r'^autor_autor_list/$', ListAuthorView.as_view(), name='autor_autor_list'),
    url(r'^autor_autor_form/edit/(?P<pk>\d+)/$', EditAuthorView.as_view(), name='autor_autor_edit'),
    url(r'^autor_autor_form/detalle/(?P<pk>\d+)/$', DetailAuthorView.as_view(), name='autor_autor_detalle'),
    url(r'^autor_autor_form/borrar/(?P<pk>\d+)/$', DeleteAutorView.as_view(), name='autor_autor_borrar'),

]

