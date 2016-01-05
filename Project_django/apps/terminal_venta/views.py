from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.contrib import messages
from django.shortcuts import render_to_response, redirect
from django.template.context import RequestContext
from django.db.models import Q
from django.http import HttpResponse
from Project_django.apps.terminal_venta.models import Product_product, Terminal_order, Terminal_order_line
from Project_django.apps.terminal_venta import forms

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
    product = Product_product()
    if request.is_ajax():
        lists = request.GET.get('list')
        jd = json.dumps(lists)
        j_list = eval(json.loads(jd))
        if j_list:
            order_id= terminal_obj.crear_pedido({'name':random.randrange(100000,999999,1),
                                                 'date_order': datetime.date.today().strftime('%Y-%m-%d'),
                                                 'amount_total' : terminal_obj.get_total(j_list)
                                                 })        
        for line in j_list:
            termial_line = Terminal_order_line(  
                            order_id=order_id,
                            product_id= product.get_product_id(line['code'],line['name']),
                            qty= line['qty'],
                            price_unit= float(line['price_unit'].replace(',','.')),
                            amount_total = float(line['amount_total'].replace(',','.'))
                            )
            termial_line.save()
    return HttpResponse(simplejson.dumps({'exito':'Orden Creada Correctamente'}), content_type='application/json')

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


# vistas basadas en clases de modelo Producto     

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
    template_name = 'product/product_product_view.html'
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

# vistas basadas en clases de modelo Terminal Orden
class ListTerminalView(ListView):
    model = Terminal_order
    template_name = 'terminal_orden/terminal_orden_list.html'
    paginate_by = 10

    def get_queryset(self):
        return Terminal_order.objects.all()      
    
class UpdateTerminalView(UpdateView):
    model = Terminal_order
    template_name = 'terminal_orden/terminal_orden_form.html'
    form_class = forms.Terminal_orden_form
    
    def get_context_data(self, **kwargs):
        ctx = super(UpdateTerminalView, self).get_context_data(**kwargs)
        if self.request.POST:
            ctx['form'] = forms.Terminal_orden_form(self.request.POST, instance=self.object)
            ctx['inlines'] = forms.Terminal_order_line_formset(self.request.POST,instance=self.object)        
        else:
            ctx['form'] = forms.Terminal_orden_form(instance=self.object)
            ctx['inlines'] = forms.Terminal_order_line_formset(instance=self.object)
        return ctx

    def form_valid(self, form):
        context = self.get_context_data()
        form = context['form']
        formset = context['inlines']
        if form.is_valid():
            self.object = form.save()
            formset.instance = self.object
            if formset.is_valid():
                formset.save()
            messages.add_message(self.request, messages.SUCCESS, 'Orden editada con exito')
            return redirect(self.object.get_absolute_url())  # assuming your model has ``get_absolute_url`` defined.
        else:
            return self.render_to_response(self.get_context_data(form=form))
