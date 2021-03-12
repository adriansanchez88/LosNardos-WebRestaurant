from django.contrib import admin
from .models import Cita

class CitaAdmin(admin.ModelAdmin):    
    list_display = ('fraseES', 'fraseEN', 'autor')    
    ordering = ('autor',)    
    search_fields = ('fraseES', 'fraseEN', 'autor')    
    
admin.site.register(Cita, CitaAdmin)