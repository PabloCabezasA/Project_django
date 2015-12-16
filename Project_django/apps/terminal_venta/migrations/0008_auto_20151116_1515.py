# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('terminal_venta', '0007_auto_20151022_2017'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='terminal_order',
            options={'ordering': ['-date_order']},
        ),
    ]
