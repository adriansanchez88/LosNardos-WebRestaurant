from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import Cita
from menu.models import Sugerencia, Categoria, Plato
from random import shuffle

class HomePageView(TemplateView):
    template_name = "core/index.html"

    def get(self, request, *args, **kwargs):

        listado = list(Cita.objects.all())
        citas = listado
        
        listado = list(Sugerencia.objects.all())    
        sugerencias = []
        for elem in listado:
            if elem.activo:
                sugerencias.append(elem)

        listado = list(Categoria.objects.all())

        categorias_menu = []
        for elem in listado:
            if elem.activo:
                categorias_menu.append(elem)

        categorias_cuatro = []
        shuffle(listado)
        for elem in listado:
            if (elem.activo or elem.tituloES=='Del Mar' or elem.tituloES=='Pollo' or elem.tituloES=='Carnes') and elem.tituloES!='Platos Principales':
                categorias_cuatro.append(elem)
                if len(categorias_cuatro)==4:
                    break

        

        platos = Plato.objects.all()
       
        


        return render(request, self.template_name, {
            'citas': citas,
            'sugerencias': sugerencias,
            'categorias': categorias_menu,
            'categorias_cuatro': categorias_cuatro,
            'platos': platos
            })