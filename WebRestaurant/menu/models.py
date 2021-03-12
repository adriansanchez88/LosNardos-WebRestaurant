from django.db import models

def upload_to_sugerencias(instance, filename):    
    if Sugerencia.objects.filter(pk=instance.pk).exists():
        old_instance = Sugerencia.objects.get(pk=instance.pk)
        old_instance.imagen.delete()
    return 'sugerencias/' + filename

def upload_to_categorias_iconoBlanco(instance, filename):    
    if Categoria.objects.filter(pk=instance.pk).exists():
        old_instance = Categoria.objects.get(pk=instance.pk)
        old_instance.iconoBlanco.delete()
    return 'sugerencias/' + filename

def upload_to_categorias_iconoNegro(instance, filename):    
    if Categoria.objects.filter(pk=instance.pk).exists():
        old_instance = Categoria.objects.get(pk=instance.pk)
        old_instance.iconoNegro.delete()
    return 'sugerencias/' + filename

class Sugerencia(models.Model):
    nombreES = models.CharField(max_length=150, verbose_name = 'Nombre del plato en español')
    nombreEN = models.CharField(max_length=150, verbose_name = 'Nombre del plato en inglés')
    descripcionES = models.TextField(max_length=200, verbose_name = 'Descripción en español')
    descripcionEN = models.TextField(max_length=200, verbose_name = 'Descripción en inglés')
    precio = models.DecimalField(verbose_name = 'Precio', max_digits=6, decimal_places=2)
    imagen = models.ImageField(verbose_name='Imagen', upload_to=upload_to_sugerencias, null=True, blank=True)
    orden = models.SmallIntegerField(verbose_name="Orden", default=0)
    activo = models.BooleanField(verbose_name = 'Activo', default=True)

    class Meta:
        verbose_name = 'sugerencia del cheff'        
        verbose_name_plural = 'sugerencias del cheff'
        ordering = ['-orden','precio']
    
    def __str__(self):
        return self.nombreES

class Categoria(models.Model):
    tituloES = models.CharField(max_length=150, verbose_name = 'Título en español')
    tituloEN = models.CharField(max_length=150, verbose_name = 'Título en inglés')
    descripcionES = models.TextField(max_length=200, verbose_name = 'Descripción en español')
    descripcionEN = models.TextField(max_length=200, verbose_name = 'Descripción en inglés')
    iconoBlanco = models.ImageField(verbose_name='Icono Blanco', upload_to=upload_to_categorias_iconoBlanco, default='static/core/images/0103-served-plate_64.png')
    iconoNegro = models.ImageField(verbose_name='Icono Negro', upload_to=upload_to_categorias_iconoNegro, default='static/core/images/0103-served-plate_64.png')
    orden = models.SmallIntegerField(verbose_name="Orden", default=0)
    activo = models.BooleanField(verbose_name = 'Activo', default=True)

    class Meta:
        verbose_name = 'categoría'        
        verbose_name_plural = 'categorías'        
        ordering = ['-orden']
    
    def __str__(self):
        return self.tituloES

class Plato(models.Model):
    nombreES = models.CharField(max_length=150, verbose_name = 'Nombre del plato en español')
    nombreEN = models.CharField(max_length=150, verbose_name = 'Nombre del plato en inglés')
    descripcionES = models.TextField(max_length=200, verbose_name = 'Descripción en español')
    descripcionEN = models.TextField(max_length=200, verbose_name = 'Descripción en inglés')
    precio = models.DecimalField(verbose_name = 'Precio', max_digits=6, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='platos')
    activo = models.BooleanField(verbose_name = 'Activo', default=True)

    class Meta:
        verbose_name = 'plato'        
        verbose_name_plural = 'platos'        
        ordering = ['categoria','precio', 'nombreES']