from urllib import request
from django.shortcuts import redirect, render
from django.contrib.auth import login , authenticate
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from Cuenta.models import *
from Cuenta.form import *

from Cuenta.form import  UserEditForm, UserRegisterForm



def login_request(request):

    if request.method == 'POST':  
        form = AuthenticationForm(request, data=request.POST)


        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)

            if user is not  None:
                login(request, user)
                
                return render(request, 'AppCoder/template/inicio.html', {'mensaje':f'Bienvenido {username}!'})
            else:
                return render(request, 'Cuenta/template/login.html', {"mensaje":"Error, datos incorrectos"})

        else:
            return render(request, 'Cuenta/template/login.html', {'mensaje':'Erro, formulario erroneo'})

    else:

        form = AuthenticationForm()

        return render(request, 'Cuenta/template/login.html', {'form':form})



def register(request):


    if request.method == 'POST':

        form = UserRegisterForm(request.POST)

        if form.is_valid():

            username = form.cleaned_data['username']
            form.save()
            return render(request, "AppCoder/template/inicio.html" , {'mensaje': f"Usuario {username} Creado :)"})
        else:
            return render(request , 'AppCoder/template/inicio.html' , {'mensaje': 'Error , no se pudo crear el usuario'})

    else:


            form = UserRegisterForm()

    return render(request, "Cuenta/template/registro.html" , {"form":form}) 


@login_required
def perfil(request):

    return render(request , "Cuenta/template/profile.html")


@login_required
def editarPerfil(request):


    usuario = request.user


    if request.method == 'POST':

        miFormulario = UserEditForm(request.POST)
        if miFormulario.is_valid():


            informacion = miFormulario.cleaned_data
            usuario.username = informacion['username']
            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']
            usuario.nombre = informacion['nombre']
            usuario.apellido = informacion['apellido']
            usuario.save()

            return redirect("Inicio")
    
        else:

            miFormulario = UserEditForm(initial={'email':usuario.email , 'username':usuario.username})
            return render(request, "Cuenta/template/editarPerfil.html")

    else:
        miFormulario = UserEditForm(initial ={'email':usuario.email , 'username':usuario.username})
        return render(request, "Cuenta/template/editarPerfil.html", {"miFormulario":miFormulario, "usuario":usuario})  


