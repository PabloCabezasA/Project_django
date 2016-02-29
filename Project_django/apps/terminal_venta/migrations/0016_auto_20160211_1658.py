# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('terminal_venta', '0015_auto_20160211_1637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='terminal_order',
            name='session_id',
            field=models.ForeignKey(related_name='order_ids', to='terminal_venta.Terminal_session'),
        ),
    ]
