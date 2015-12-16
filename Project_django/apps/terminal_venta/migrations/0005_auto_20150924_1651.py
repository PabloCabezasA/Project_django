# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('terminal_venta', '0004_auto_20150916_1446'),
    ]

    operations = [
        migrations.AlterField(
            model_name='terminal_order_line',
            name='amount_total',
            field=models.FloatField(verbose_name=b'Monto Total'),
        ),
    ]
