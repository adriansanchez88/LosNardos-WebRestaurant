from django.contrib import admin
from .models import Sugerencia, Categoria, Plato

class SugerenciaAdmin(admin.ModelAdmin):    
    list_display = ('nombreES', 'nombreEN', 'descripcionES', 'descripcionEN', 'precio', 'orden')    
    ordering = ('orden','nombreES')    
    search_fields = ('nombreES', 'nombreEN', 'descripcionES', 'descripcionEN', 'precio')   

class CategoriaAdmin(admin.ModelAdmin):    
    list_display = ('tituloES', 'tituloEN', 'descripcionES', 'descripcionEN', 'orden')    
    ordering = ('orden',)    
    search_fields = ('tituloES', 'tituloEN', 'descripcionES', 'descripcionEN') 

class PlatoAdmin(admin.ModelAdmin):    
    list_display = ('nombreES', 'nombreEN', 'descripcionES', 'descripcionEN', 'precio')    
    ordering = ('categoria','precio', 'nombreES')    
    search_fields = ('nombreES', 'nombreEN', 'descripcionES', 'descripcionEN', 'precio')  
    
admin.site.register(Sugerencia, SugerenciaAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Plato, PlatoAdmin)