from django.db import models

# Create your models here.
class Product_product(models.Model):
    name = models.CharField('nombre',max_length=120, blank=False, unique=True)
    code = models.IntegerField('codigo', blank=False, unique=True)
    type = models.CharField('tipo', choices=(('product','almacenable'),('consu','consumible'),('service','servicio')),max_length=10, blank=False)
    price_sale = models.FloatField('precio de venta', blank=False)
    qty_available = models.PositiveIntegerField('cantidad avilitada', blank=False)
    model_pic = models.ImageField(verbose_name='Imagen',
    upload_to='product_img/', default='product_img/None/no-img.jpg')
