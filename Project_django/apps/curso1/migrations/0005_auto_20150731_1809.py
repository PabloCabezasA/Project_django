# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('curso1', '0004_autor_autor_obras_autor_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='autor_obras_rel',
            name='autor_id',
        ),
        migrations.RemoveField(
            model_name='autor_obras_rel',
            name='obra_id',
        ),
        migrations.AlterField(
            model_name='autor_autor',
            name='name',
            field=models.CharField(unique=True, max_length=50, verbose_name=b'Nombre'),
        ),
        migrations.AlterField(
            model_name='autor_autor_obras',
            name='link',
            field=models.URLField(max_length=250, verbose_name=b'ruta'),
        ),
        migrations.DeleteModel(
            name='autor_obras_rel',
        ),
    ]
