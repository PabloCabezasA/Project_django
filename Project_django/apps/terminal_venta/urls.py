from django.conf.urls import  url
from django.conf import settings
from django.contrib.auth.decorators import login_required
from Project_django.apps.terminal_venta import models
from Project_django.apps.terminal_venta import views 
from Project_django.apps.terminal_venta.serializers import ProductSerializerList, ProductSerializerDetail, OrderSerializerList

urlpatterns = [
    # Examples:
    url(r'^$', 'Project_django.apps.terminal_venta.views.base_view', name='index-view'),
    url(r'^terminal_view/save_data/$', 'Project_django.apps.terminal_venta.views.save_data', name='save-data'),    
#Products URLS
    url(r'^product_product_form/$', views.AddProductView.as_view(), name='product-add'),
    url(r'^product_product_list/$', views.ListProductView.as_view(), name='product-list'),
    url(r'^product_product_list/filter/$', views.ListProductView.as_view(), name='product-list-filter'),
    url(r'^product_product_form/edit/(?P<pk>\d+)/$', views.EditProductView.as_view(), name='product-edit'),
#Terminal URLS
    url(r'^terminal_view/$', 'Project_django.apps.terminal_venta.views.terminal_view', name='terminal-view'),
    url(r'^terminal_orden/$', login_required(views.ListTerminalView.as_view()), name='terminal-orden'),   
    url(r'^terminal_orden_form/edit/(?P<pk>\d+)/$', views.UpdateTerminalView.as_view(), name='terminal-orden-edit'),     
#Serializer URLS
    url(r'^snippets/$', ProductSerializerList.as_view()),
    url(r'^snippets/(?P<name>\w+)/$', ProductSerializerDetail.as_view()),    
    url(r'^snippets/(?P<name>\w+)/(?P<code>\w)/$', ProductSerializerDetail.as_view()),    
    url(r'^snippets/(?P<pk>[0-9]+)/$', ProductSerializerDetail.as_view()),
    url(r'^orderSerializer/$', OrderSerializerList.as_view()),
#sessions URLS
    url(r'^session/add/$', views.AddSession.as_view(), name='session-add'),
    url(r'^session/list/$', views.SessionList.as_view(), name='session-list'),
    url(r'^session/edit/(?P<pk>\d+)/$', views.UpdateSessionView.as_view(), name='session-edit'),
    url(r'^session/close/session/(?P<pk>\d+)/$', views.close_session, name="session-close")
]