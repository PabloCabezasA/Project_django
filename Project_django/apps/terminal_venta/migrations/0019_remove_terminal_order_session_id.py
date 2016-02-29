# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('terminal_venta', '0018_auto_20160212_1926'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='terminal_order',
            name='session_id',
        ),
    ]
