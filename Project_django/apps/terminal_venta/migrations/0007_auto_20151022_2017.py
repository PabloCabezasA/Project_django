# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('terminal_venta', '0006_auto_20150930_1929'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='product_product',
            table='product_product',
        ),
        migrations.AlterModelTable(
            name='terminal_order',
            table='terminal_order',
        ),
        migrations.AlterModelTable(
            name='terminal_order_line',
            table='terminal_order_line',
        ),
    ]
