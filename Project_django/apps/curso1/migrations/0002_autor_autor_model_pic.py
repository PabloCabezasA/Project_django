# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('curso1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='autor_autor',
            name='model_pic',
            field=models.ImageField(default=b'pic_folder/None/no-img.jpg', upload_to=b'autor_imagen/', verbose_name=b'Imagen'),
        ),
    ]
