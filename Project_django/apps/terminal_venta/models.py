from django.db import models
from django.core.urlresolvers import reverse
from django.db.models import Q

# Create your models here.
class Product_product(models.Model):
    active = models.BooleanField('activo')
    name = models.CharField('nombre',max_length=120, blank=False, unique=True)
    code = models.IntegerField('codigo', blank=False, unique=True)
    type = models.CharField('tipo', choices=(('product','almacenable'),('consu','consumible'),('service','servicio')),max_length=10, blank=False)
    price_sale = models.FloatField('precio de venta', blank=False)
    qty_available = models.PositiveIntegerField('cantidad avilitada', blank=False)
    model_pic = models.ImageField(verbose_name='Imagen',
    upload_to='product_img/', default='product_img/None/no_foto.png')
    

    def get_absolute_url(self):        
        return reverse('product:product_product_list')
    
    def get_product_id(self, code, name):
        prod =self.__class__.objects.get(Q(name=name), Q(code=code))
        return prod
    
class Terminal_order(models.Model):
    name = models.CharField('Nombre', max_length=120, blank=False, unique=True)
    date_order = models.DateField('Fecha Pedido', blank=False)
    amount_total = models.PositiveIntegerField('Monto Total', blank=False)
    
    def crear_pedido(self,data):        
        order= Terminal_order(name=data['name'], date_order=data['date_order'], amount_total=data['amount_total'])
        order.save()
        return order

    def get_total(self,lines):
        amount_total = 0
        for i in lines:
            amount_total += float(i['amount_total'].replace(',','.')) 
        return amount_total

    def get_absolute_url(self):        
        return reverse('product:terminal-orden-edit', kwargs={'pk': self.id})


class Terminal_order_line(models.Model):
    order_id = models.ForeignKey(Terminal_order)
    product_id = models.ForeignKey(Product_product)
    qty = models.PositiveIntegerField('Cantidad', blank=False)
    price_unit = models.PositiveIntegerField('Precio Unitario', blank=False)
    amount_total = models.FloatField('Monto Total', blank=False)
