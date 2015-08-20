# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='autor_autor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name=b'Nombre')),
                ('apellidos', models.CharField(max_length=100, verbose_name=b'Apellido')),
                ('nacionalidad', models.CharField(max_length=50, null=True, verbose_name=b'Nacionalidad')),
                ('fecha_nac', models.DateField(verbose_name=b'Fecha Nacimiento')),
                ('fecha_fin', models.DateField(verbose_name=b'Fecha Muerte')),
            ],
        ),
    ]
