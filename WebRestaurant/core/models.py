from django.db import models

# Create your models here.
class Cita(models.Model):
    fraseES = models.TextField(max_length=200, verbose_name = 'Frase en español')
    fraseEN = models.TextField(max_length=200, verbose_name = 'Frase en inglés')
    autor = models.CharField(max_length=100, verbose_name = 'Autor')

    class Meta:
        verbose_name = 'cita'        
        verbose_name_plural = 'Citas'        
        ordering = ['autor']
    
    def __str__(self):
        return self.autor