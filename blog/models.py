from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Entrada(models.Model):
    titulo = models.CharField(max_length=100)
    contenido = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.titulo


class Comentario(models.Model):

    fechaCreacion = models.DateTimeField(auto_now_add=True)
    autor = models.CharField(max_length=100)
    mensaje = models.TextField()
    idEntrada = models.ForeignKey('Entrada')

    def __str__(self):
        return unicode("%s %s" % (self.idEntrada, self.mensaje[:60]))

