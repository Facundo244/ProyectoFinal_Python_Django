from django import forms
from django.core.exceptions import ValidationError



class FormularioPost(forms.Form):
    
    titulo = forms.CharField(max_length=20)
    subtitulo = forms.CharField(max_length=50)
    texto = forms.CharField(widget=forms.Textarea)
    autor = forms.CharField(max_length=50)


class BuscarPost(forms.Form):
    titulo = forms.CharField(max_length=25)