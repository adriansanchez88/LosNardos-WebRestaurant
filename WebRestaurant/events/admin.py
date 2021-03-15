from django.contrib import admin
from .models import Evento

class EventoAdmin(admin.ModelAdmin):    
    list_display = ('nombreES', 'nombreEN', 'descripcionES', 'descripcionEN', 'fecha')    
    ordering = ('fecha',)    
    search_fields = ('nombreES', 'nombreEN', 'descripcionES', 'descripcionEN', 'fecha')
    date_hierarchy = ('fecha')

admin.site.register(Evento, EventoAdmin)
