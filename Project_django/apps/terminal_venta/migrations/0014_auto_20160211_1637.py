# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('terminal_venta', '0013_terminal_order_session_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='terminal_session',
            name='amount_total',
            field=models.FloatField(default=0, max_length=10, verbose_name=b'Monto Total'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='terminal_session',
            name='qty_total',
            field=models.PositiveIntegerField(default=0, max_length=8, verbose_name=b'Cantidad de boletas'),
            preserve_default=False,
        ),
    ]
