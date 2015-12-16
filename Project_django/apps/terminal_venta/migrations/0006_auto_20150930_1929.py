# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('terminal_venta', '0005_auto_20150924_1651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='terminal_order',
            name='amount_total',
            field=models.FloatField(verbose_name=b'Monto Total'),
        ),
        migrations.AlterField(
            model_name='terminal_order_line',
            name='price_unit',
            field=models.FloatField(verbose_name=b'Precio Unitario'),
        ),
    ]
