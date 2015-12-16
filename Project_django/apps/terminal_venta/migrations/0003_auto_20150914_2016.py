# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('terminal_venta', '0002_product_product_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='Terminal_order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=120, verbose_name=b'Nombre')),
                ('date_order', models.DateField(unique=True, verbose_name=b'Fecha Pedido')),
                ('amount_total', models.PositiveIntegerField(verbose_name=b'Monto Total')),
            ],
        ),
        migrations.CreateModel(
            name='Terminal_order_line',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('qty', models.PositiveIntegerField(verbose_name=b'Cantidad')),
                ('price_unit', models.PositiveIntegerField(verbose_name=b'Precio Unitario')),
                ('amount_total', models.PositiveIntegerField(verbose_name=b'Monto Total')),
                ('order_id', models.ForeignKey(to='terminal_venta.Terminal_order')),
            ],
        ),
        migrations.AlterField(
            model_name='product_product',
            name='model_pic',
            field=models.ImageField(default=b'product_img/None/no_foto.png', upload_to=b'product_img/', verbose_name=b'Imagen'),
        ),
        migrations.AddField(
            model_name='terminal_order_line',
            name='product_id',
            field=models.ForeignKey(to='terminal_venta.Product_product'),
        ),
    ]
