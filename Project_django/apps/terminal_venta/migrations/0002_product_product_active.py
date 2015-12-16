# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('terminal_venta', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product_product',
            name='active',
            field=models.BooleanField(default=True, verbose_name=b'activo'),
            preserve_default=False,
        ),
    ]
