# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('terminal_venta', '0017_auto_20160211_1828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='terminal_session',
            name='name',
            field=models.CharField(unique=True, max_length=60, verbose_name=b'Nombre'),
        ),
    ]
