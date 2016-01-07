# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('terminal_venta', '0011_auto_20160107_1306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='terminal_session',
            name='date_close',
            field=models.DateField(null=True, verbose_name=b'Fecha Cierre', blank=True),
        ),
    ]
