from Project_django.apps.terminal_venta.models import Product_product
from Project_django.apps.curso1 import forms
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.contrib import messages
# Create your views here.

class AddProductView(CreateView):
    template_name = 'product/autor_autor_view.html'
    model = Product_product
    form_class = forms.autor_autor_form


class ListProductView(ListView):
    template_name = 'product/autor_autor_list.html'
    model = Product_product

class EditProductView(UpdateView):
    model = Product_product
    template_name = 'product/autor_autor_view.html'
    form_class = forms.autor_autor_form

    
class DetailProductView(DetailView):
    model = Product_product
    template_name = 'product/autor_autor_detalle.html'
    form_class = forms.autor_autor_form

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