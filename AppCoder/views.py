from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.contrib.auth.decorators import login_required
from Posts.models import Post




def inicio(request):
    plantilla = loader.get_template('AppCoder/template/padre.html')
    documento = plantilla.render()
    return HttpResponse(documento)


@login_required
def acercaDeNosotros(request):
    return render(request, 'AppCoder/template/acerca_De.html')

@login_required
def blog(request):
    posts = Post.objects.all()
    return render(request , 'AppCoder/template/blog.html' , {'posts':posts})






