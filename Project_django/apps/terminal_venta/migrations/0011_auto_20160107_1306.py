# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('terminal_venta', '0010_auto_20160106_1255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='terminal_session',
            name='state',
            field=models.CharField(blank=True, max_length=5, verbose_name=b'Estado', choices=[(b'start', b'Inicio'), (b'close', b'Cerrado')]),
        ),
        migrations.AlterModelTable(
            name='terminal_session',
            table='terminal_session',
        ),
    ]
