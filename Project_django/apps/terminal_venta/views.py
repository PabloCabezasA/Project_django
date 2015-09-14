from Project_django.apps.terminal_venta.models import Product_product,Terminal_order,Terminal_order_line
from Project_django.apps.terminal_venta import forms
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.contrib import messages
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.db.models import Q
from django.http import HttpResponse
import json
import simplejson
import random
import datetime
# Create your views here.

def base_view(request):
    return render_to_response('product/base.html', context_instance=RequestContext(request))

def save_data(request):
    values = {}
    terminal_obj = Terminal_order()
    if request.is_ajax():
        lists = request.GET.get('list')
        jd = json.dumps(lists)
        list = eval(json.loads(jd))
        if list:
            id = terminal_obj.crear_pedido({'name':random.randrange(100000,999999,1),
                                       'date_order': datetime.date.today().strftime('%Y-%m-%d'),
                                       'amount_total' : terminal_obj.get_total(list)
                                       })
        for i in list:
            print i
    return HttpResponse({'hola':'mundo'}, content_type='application/json')


def terminal_view(request):
    values = {}
    if request.is_ajax():        
        filter = request.GET['filter'] if request.GET else False
        response_data = create_json_response(filter)
        return HttpResponse(response_data, content_type='application/json')    
    else:
        list_product = Product_product.objects.filter(active = True, qty_available__gt = 0).order_by('name')
    values['products'] = list_product
    return render_to_response('product/terminal_venta.html', values, context_instance=RequestContext(request))

def create_json_response(filter):
    to_json = []    
    if not filter:
        list_product = Product_product.objects.filter(Q(active = True) , Q(qty_available__gt = 0)).order_by('name')
    else:
        list_product = Product_product.objects.filter(Q(active = True) , Q(qty_available__gt = 0) , Q( name__icontains = filter)  ).order_by('name')
    for product in list_product:
        dict = {
                'id' : product.id,
                'name' : product.name,
                'code' : product.code,
                'model_pic' : str(product.model_pic),
                'price_sale' : product.price_sale, 
                }
        to_json.append(dict)
    return simplejson.dumps(to_json)

    

class AddProductView(CreateView):
    template_name = 'product/product_product_view.html'
    model = Product_product
    form_class = forms.product_product_form


class ListProductView(ListView):
    template_name = 'product/product_product_list.html'
    model = Product_product

    def get_queryset(self):
        return Product_product.objects.all()


class EditProductView(UpdateView):
    model = Product_product
    template_name = 'product/autor_autor_view.html'
    form_class = forms.product_product_form

    
class DetailProductView(DetailView):
    model = Product_product
    template_name = 'product/autor_autor_detalle.html'
    form_class = forms.product_product_form

    def get_context_data(self, **kwargs):
        ctx = super(DetailProductView, self).get_context_data(**kwargs)
        ctx['lista_videos'] = Product_product.objects.filter(autor_id = self.object.id)
        return ctx
    
class DeleteProductView(DeleteView):
    model = Product_product
    template_name = 'product/autor_autor_list.html'
    success_url='/product/autor_autor_list'

    def get_success_url(self):
        res = super(DeleteProductView, self).get_success_url()
        """
        Redirect to the page listing all of the proxy urls
        """
        return res

    def get(self, *args, **kwargs):
        """
        This has been overriden because by default
        DeleteView doesn't work with GET requests
        """
        return self.delete(*args, **kwargs)    