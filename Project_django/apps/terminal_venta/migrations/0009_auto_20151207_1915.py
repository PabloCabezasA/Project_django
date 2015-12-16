# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('terminal_venta', '0008_auto_20151116_1515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_product',
            name='qty_available',
            field=models.PositiveIntegerField(verbose_name=b'cantidad habilitada'),
        ),
        migrations.AlterField(
            model_name='terminal_order_line',
            name='order_id',
            field=models.ForeignKey(related_name='lines', to='terminal_venta.Terminal_order'),
        ),
    ]
