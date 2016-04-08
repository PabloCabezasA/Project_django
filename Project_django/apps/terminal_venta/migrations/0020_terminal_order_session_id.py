# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('terminal_venta', '0019_remove_terminal_order_session_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='terminal_order',
            name='session_id',
            field=models.ForeignKey(related_name='order_ids', default=1, to='terminal_venta.Terminal_session'),
            preserve_default=False,
        ),
    ]
