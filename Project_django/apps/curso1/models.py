# -*- coding: utf-8 -*-
from django.db import models
from django.core.urlresolvers import reverse
from django.core.exceptions import ValidationError
import datetime


class autor_autor(models.Model):
    name = models.CharField(verbose_name='Nombre', max_length=50, null=False, unique=True)
    apellidos = models.CharField(verbose_name='Apellido', max_length=100,
    null=False)
    nacionalidad = models.CharField(verbose_name='Nacionalidad', max_length=50,
    null=True)
    fecha_nac = models.DateField(verbose_name='Fecha Nacimiento',
    auto_now=False)
    fecha_fin = models.DateField(verbose_name='Fecha Muerte', auto_now=False)
    model_pic = models.ImageField(verbose_name='Imagen',
    upload_to='autor_imagen/', default='autor_imagen/None/no-img.jpg')

    def get_absolute_url(self):
        irrrr = reverse('curso1:autor_autor_edit', kwargs={'pk': self.id})
        return irrrr
    
    def clean(self):
        if self.fecha_nac >= self.fecha_fin:
            raise ValidationError('Fecha de Nacimiento, no puede ser menor que la fecha de muerte.')
        elif self.fecha_nac > datetime.date.today():
            raise ValidationError('Fecha de Nacimiento, no puede ser mayor que la fecha de actual.')
        elif self.fecha_fin <= self.fecha_nac:
            raise ValidationError('Fecha de Muerte, no puede ser mayor que la fecha de Nacimiento.')
        res = super(autor_autor, self).clean()
        return res
    
    def clean_fields(self, exclude=None):
        self.name = self.name.strip()
        self.apellidos = self.apellidos.strip()
        self.nacionalidad = self.nacionalidad.strip()
        res = super(autor_autor, self).clean_fields(exclude)
        return res

class autor_autor_obras(models.Model):
    name = models.CharField(verbose_name="Nombre", max_length=50, null=False)
    link = models.URLField(verbose_name="ruta", max_length=250, null=False)
    autor_id = models.ForeignKey(autor_autor)   
    
    class Meta: 
        unique_together = ("name", "link")
    
    def clean_fields(self, exclude=None):
        res = super(autor_autor_obras, self).clean_fields(exclude)
        return res