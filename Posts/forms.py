from django import forms
from django.core.exceptions import ValidationError



class FormularioPost(forms.Form):

    titulo = forms.Charfield(max_lenght=20)
    subtitulo = forms.CharField(max_lenght=50)
    text = forms.CharField(max_lenght=50)
    autor = forms.CharField(max_length=50)
    imagen_post = forms.ImageField(required = False )


class BuscarPost(forms.Form):

    autor = forms.CharField(max_length=25)