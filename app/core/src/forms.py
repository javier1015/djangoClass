from django import forms
from .pqrsf import pqrsf

#creamos las clases con los formularios

class contactForm(forms.Form):
    # Atributos del formulario de contacto
    tipoMensaje = forms.ChoiceField(label = "Tipo de peticion", required=True, choices=pqrsf, widget=forms.Select(attrs={'class':'form-control'}))
    usuario = forms.CharField(label = "Tu nombre", required=True, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Escribe tu nombre completo'}))
    correo = forms.EmailField(label = "Correo electronico", required=True, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Escribe tu correo electronico'}))
    mensaje = forms.CharField(label = "Mensaje", required=True, widget=forms.Textarea(attrs={'class':'form-control', 'rows':'6', 'placeholder':'Escribe tu mensaje'}))