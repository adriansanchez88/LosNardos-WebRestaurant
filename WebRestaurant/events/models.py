from django.db import models

# Create your models here.
class Evento(models.Model):
    nombreES = models.CharField(max_length=150, verbose_name = 'Nombre del evento en español')
    nombreEN = models.CharField(max_length=150, verbose_name = 'Nombre del evento en inglés')
    descripcionES = models.TextField(max_length=200, verbose_name = 'Descripción en español')
    descripcionEN = models.TextField(max_length=200, verbose_name = 'Descripción en inglés')
    fecha = models.DateField(verbose_name="Fecha")    
    activo = models.BooleanField(verbose_name = 'Activo', default=True)
