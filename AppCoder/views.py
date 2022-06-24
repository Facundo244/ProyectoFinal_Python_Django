from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader



def inicio(request):
    plantilla = loader.get_template('AppCoder/template/padre.html')
    documento = plantilla.render()
    return HttpResponse(documento)


def acercaDeNosotros(request):
    plantilla = loader.get_template('AppCoder/template/acerca_De.html')
    documento = plantilla.render()
    return HttpResponse(documento)






