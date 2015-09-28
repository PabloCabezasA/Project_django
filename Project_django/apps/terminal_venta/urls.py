from django.conf.urls import  url
from django.conf import settings
from Project_django.apps.terminal_venta import models
from Project_django.apps.terminal_venta import views 

urlpatterns = [
    # Examples:
    url(r'^$', 'Project_django.apps.terminal_venta.views.base_view', name='index-view'),
    url(r'^terminal_view/save_data/$', 'Project_django.apps.terminal_venta.views.save_data', name='save-data'),    
    url(r'^product_product_form/$', views.AddProductView.as_view(), name='product-add'),
    url(r'^product_product_list/$', views.ListProductView.as_view(), name='product-list'),
    url(r'^terminal_view/$', 'Project_django.apps.terminal_venta.views.terminal_view', name='terminal-view'),
    url(r'^terminal_orden/$', views.ListTerminalView.as_view(), name='terminal-orden'),   
    url(r'^terminal_orden_form/edit/(?P<pk>\d+)/$', views.UpdateTerminalView.as_view(), name='terminal-orden-edit'),     
]

