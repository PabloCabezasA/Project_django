from django.db import models
from django.core.urlresolvers import reverse
from django.db.models import Q
from django.core.exceptions import ValidationError
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.
class Product_product(models.Model):
    active = models.BooleanField('activo')
    name = models.CharField('nombre',max_length=120, blank=False, unique=True)
    code = models.IntegerField('codigo', blank=False, unique=True)
    type = models.CharField('tipo', choices=(('product','almacenable'),('consu','consumible'),('service','servicio')),max_length=10, blank=False)
    price_sale = models.FloatField('precio de venta', blank=False)
    qty_available = models.PositiveIntegerField('cantidad habilitada', blank=False)
    model_pic = models.ImageField(verbose_name='Imagen',
    upload_to='product_img/', default='product_img/None/no_foto.png')
    
    def __str__(self):
        return self.name+' '+ str(self.code)
        
    class Meta:
        db_table = 'product_product'
    
    def get_absolute_url(self):        
        return reverse('terminal:product-list')
    
    def get_product_id(self, code, name):
        prod =self.__class__.objects.get(Q(name=name), Q(code=code))
        return prod

    
class Terminal_order(models.Model):
    name = models.CharField('Nombre', max_length=120, blank=False, unique=True)
    date_order = models.DateField('Fecha Pedido', blank=False)
    amount_total = models.FloatField('Monto Total', blank=False)
    session_id = models.ForeignKey('Terminal_session')
    class Meta:
        db_table = 'terminal_order'
        ordering = ['-date_order']
    
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
        return reverse('terminal:terminal-orden-edit', kwargs={'pk': self.id})

    def clean(self):
        if str(self.date_order) < datetime.today().strftime('%Y-%m-%d'):
            raise ValidationError('Fecha no puede ser inferior a hoy')
        res = super(Terminal_order, self).clean()
        return res
    
    def clean_fields(self, exclude=None):
        res = super(Terminal_order, self).clean_fields(exclude)
        return res
    
    
class Terminal_order_line(models.Model):
    order_id = models.ForeignKey(Terminal_order, related_name='lines')
    product_id = models.ForeignKey(Product_product)
    qty = models.PositiveIntegerField('Cantidad', blank=False)
    price_unit = models.FloatField('Precio Unitario', blank=False)
    amount_total = models.FloatField('Monto Total', blank=False)

    class Meta:
        db_table = 'terminal_order_line'

    def clean_fields(self, exclude=None):
        res = super(Terminal_order_line, self).clean_fields(exclude)
        return res


class Terminal_session(models.Model):
    name = models.CharField('Nombre', max_length=60)
    user_id = models.ForeignKey(User)
    date_start = models.DateField('Fecha Inicio')
    date_close = models.DateField('Fecha Cierre', blank=True, null=True)
    state = models.CharField('Estado', choices=(('start','Inicio'),('close','Cerrado')), max_length=5, blank=True)
    class Meta:
        db_table = 'terminal_session'

    def get_absolute_url(self):
        return reverse('terminal:session-edit', kwargs={'pk': self.id})
