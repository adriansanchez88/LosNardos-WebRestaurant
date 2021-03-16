from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic.base import TemplateView
from .models import Cita
from menu.models import Sugerencia, Categoria, Plato
from events.models import Evento
from reservation.forms import ReservationForm
from random import shuffle
from django.core.mail import send_mail
from django.conf import settings

def home(request): 
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

    listado = list(Plato.objects.all())
    platos = []
    for categoria in categorias_menu:
        cont = 0
        for elem in listado:
            if elem.categoria.tituloES == categoria.tituloES:
                platos.append(elem)
                cont+=1
                if cont>=3:
                    break

    eventos = Evento.objects.all()

    form = ReservationForm()
    
    if request.method == 'POST':
        form = ReservationForm(data=request.POST)
        if form.is_valid():
            datos = form.cleaned_data
            nombre = datos.get('nombre')
            email = datos.get('email')
            fecha_y_hora = datos.get('fecha_y_hora')
            mensaje = datos.get('mensaje')
            try:
                send_mail(
                    "Reservación para las {}".format(fecha_y_hora),
                    "De {} <{}>\n\nEscribió:\n\n{}".format(nombre, email, mensaje),
                    settings.EMAIL_HOST_USER,
                    ['losnardoscuba@gmail.com'],
                    fail_silently= False,
                )
                return redirect(reverse('home')+'?ok')                    
            except:
                return redirect(reverse('home')+'?fail')

    return render(request, "core/index.html", {
            'citas': citas,
            'sugerencias': sugerencias,
            'categorias': categorias_menu,
            'categorias_cuatro': categorias_cuatro,
            'platos': platos,
            'eventos': eventos,
            'form' : form,
            'language': 'ES'
    })

        

class MenuPageView(TemplateView):
    template_name = "core/menu_completo.html"

    def get(self, request, *args, **kwargs):

        listado = list(Categoria.objects.all())
        categorias_menu = []        
        for elem in listado:
            if elem.activo:
                categorias_menu.append(elem)

        platos = Plato.objects.all()

        return render(request, self.template_name, {
            
            'categorias': categorias_menu,            
            'platos': platos,
            'language': 'ES'
    })