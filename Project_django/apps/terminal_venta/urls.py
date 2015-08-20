from django.conf.urls import  url
from django.conf import settings
from Project_django.apps.terminal_venta import models
from Project_django.apps.terminal_venta.views import AddProductView 

urlpatterns = [
    # Examples:
    url(r'^$', 'Project_django.apps.terminal_venta.views.index', name='index-view'),
    url(r'^product_product_form/$', AddProductView.as_view(), name='product-add'),
]

