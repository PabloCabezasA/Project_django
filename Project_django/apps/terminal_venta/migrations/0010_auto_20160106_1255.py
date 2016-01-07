# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('terminal_venta', '0009_auto_20151207_1915'),
    ]

    operations = [
        migrations.CreateModel(
            name='Terminal_session',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=60, verbose_name=b'Nombre')),
                ('date_start', models.DateField(verbose_name=b'Fecha Inicio')),
                ('date_close', models.DateField(verbose_name=b'Fecha Cierre', blank=True)),
                ('state', models.CharField(max_length=5, verbose_name=b'Estado', choices=[(b'start', b'Inicio'), (b'close', b'Cerrado')])),
                ('user_id', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
