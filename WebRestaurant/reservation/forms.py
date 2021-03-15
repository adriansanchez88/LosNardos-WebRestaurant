from django import forms

class ReservationForm(forms.Form):
    nombre = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder':'Nombre'}
    ), min_length=3, max_length=100)
    email = forms.EmailField(required=True, widget=forms.EmailInput(
        attrs={'class':'form-control', 'placeholder':'Email'}
    ), min_length=3, max_length=100)
    fecha_y_hora = forms.DateTimeField(input_formats=('%m/%d/%Y %I:%M %p',),required=True, widget=forms.DateTimeInput(        
        attrs={'class':'form-control', 'placeholder':'Fecha y Hora', 'id':'date'}
    ))
    mensaje = forms.CharField(required=True, widget=forms.Textarea(
        attrs={'class':'form-control', 'rows': 3, 'placeholder':'Mensaje'}
    ), min_length=10, max_length=1000)