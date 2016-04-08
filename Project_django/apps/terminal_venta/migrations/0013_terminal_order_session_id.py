# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('terminal_venta', '0012_auto_20160107_1322'),
    ]

    operations = [
        migrations.AddField(
            model_name='terminal_order',
            name='session_id',
            field=models.ForeignKey(default=2, to='terminal_venta.Terminal_session'),
            preserve_default=False,
        ),
    ]
