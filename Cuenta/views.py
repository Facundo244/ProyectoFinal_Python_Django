from django.shortcuts import  render
from django.contrib.auth import login , authenticate
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from Cuenta.models import *
from Cuenta.form import *



from Cuenta.form import User_Edit_Form , UserRegisterForm



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
        formulario = User_Edit_Form(request.POST , instance=usuario)

        if formulario.is_valid():

            informacion = formulario.cleaned_data
            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']
            usuario.save()

            return render(request , 'AppCoder/template/inicio.html', {'mensaje':'Datos cambiados exitosamente'})
    else:
        formulario = User_Edit_Form(instance=usuario)
        return render(request , 'Cuenta/template/editarPerfil.html' , {'formulario':formulario , 'usuario':usuario.username})




