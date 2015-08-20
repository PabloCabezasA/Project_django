# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('curso1', '0002_autor_autor_model_pic'),
    ]

    operations = [
        migrations.CreateModel(
            name='autor_autor_obras',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name=b'Nombre')),
                ('link', models.CharField(max_length=250, verbose_name=b'ruta')),
            ],
        ),
        migrations.CreateModel(
            name='autor_obras_rel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.AlterField(
            model_name='autor_autor',
            name='model_pic',
            field=models.ImageField(default=b'autor_imagen/None/no-img.jpg', upload_to=b'autor_imagen/', verbose_name=b'Imagen'),
        ),
        migrations.AddField(
            model_name='autor_obras_rel',
            name='autor_id',
            field=models.ForeignKey(to='curso1.autor_autor'),
        ),
        migrations.AddField(
            model_name='autor_obras_rel',
            name='obra_id',
            field=models.ForeignKey(to='curso1.autor_autor_obras'),
        ),
    ]
