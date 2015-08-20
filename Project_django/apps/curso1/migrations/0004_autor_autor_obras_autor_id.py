# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('curso1', '0003_auto_20150604_2118'),
    ]

    operations = [
        migrations.AddField(
            model_name='autor_autor_obras',
            name='autor_id',
            field=models.ForeignKey(default=None, to='curso1.autor_autor'),
            preserve_default=False,
        ),
    ]
