from django.conf.urls import  url
from django.conf import settings
from Project_django.apps.terminal_venta import models
from Project_django.apps.terminal_venta import views 
from Project_django.apps.terminal_venta.serializers import ProductSerializerList, ProductSerializerDetail, OrderSerializerList 

urlpatterns = [
    # Examples:
    url(r'^$', 'Project_django.apps.terminal_venta.views.base_view', name='index-view'),
    url(r'^terminal_view/save_data/$', 'Project_django.apps.terminal_venta.views.save_data', name='save-data'),    
    url(r'^product_product_form/$', views.AddProductView.as_view(), name='product-add'),
    url(r'^product_product_list/$', views.ListProductView.as_view(), name='product-list'),
    url(r'^product_product_form/edit/(?P<pk>\d+)/$', views.EditProductView.as_view(), name='product-edit'),
    url(r'^terminal_view/$', 'Project_django.apps.terminal_venta.views.terminal_view', name='terminal-view'),
    url(r'^terminal_orden/$', views.ListTerminalView.as_view(), name='terminal-orden'),   
    url(r'^terminal_orden_form/edit/(?P<pk>\d+)/$', views.UpdateTerminalView.as_view(), name='terminal-orden-edit'),     
    url(r'^snippets/$', ProductSerializerList.as_view()),
    url(r'^snippets/(?P<name>\w+)/(?P<code>\w)/$', ProductSerializerDetail.as_view()),    
    url(r'^snippets/(?P<pk>[0-9]+)/$', ProductSerializerDetail.as_view()),
    url(r'^orderSerializer/$', OrderSerializerList.as_view()),
]

