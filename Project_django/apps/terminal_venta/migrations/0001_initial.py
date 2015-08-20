# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product_product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=120, verbose_name=b'nombre')),
                ('code', models.IntegerField(unique=True, verbose_name=b'codigo')),
                ('type', models.CharField(max_length=10, verbose_name=b'tipo', choices=[(b'product', b'almacenable'), (b'consu', b'consumible'), (b'service', b'servicio')])),
                ('price_sale', models.FloatField(verbose_name=b'precio de venta')),
                ('qty_available', models.PositiveIntegerField(verbose_name=b'cantidad avilitada')),
                ('model_pic', models.ImageField(default=b'product_img/None/no-img.jpg', upload_to=b'product_img/', verbose_name=b'Imagen')),
            ],
        ),
    ]
