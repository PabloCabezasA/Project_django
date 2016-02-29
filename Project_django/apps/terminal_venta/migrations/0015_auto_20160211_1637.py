# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('terminal_venta', '0014_auto_20160211_1637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='terminal_session',
            name='amount_total',
            field=models.FloatField(max_length=10, verbose_name=b'Monto Total', blank=True),
        ),
        migrations.AlterField(
            model_name='terminal_session',
            name='qty_total',
            field=models.PositiveIntegerField(max_length=8, verbose_name=b'Cantidad de boletas', blank=True),
        ),
    ]
