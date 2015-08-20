# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('curso1', '0005_auto_20150731_1809'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='autor_autor_obras',
            unique_together=set([('name', 'link')]),
        ),
    ]
