# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('terminal_venta', '0003_auto_20150914_2016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='terminal_order',
            name='date_order',
            field=models.DateField(verbose_name=b'Fecha Pedido'),
        ),
    ]
