from django.shortcuts import render
from django.contrib.auth import login , logout, authenticate
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm , UserCreationForm
from django.contrib.auth.decorators import login_required


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

        form = UserCreationForm(request.POST)

        if form.is_valid():

            username = form.cleaned_data['username']
            form.save()
            return render(request, "AppCoder/template/inicio.html" , {'mensaje': f"Usuario {username} Creado :)"})
        else:
            return render(request , 'AppCoder/template/inicio.html' , {'mensaje': 'Error , no se pudo crear el usuario'})

    else:


            form = UserCreationForm()

    return render(request, "Cuenta/template/registro.html" , {"form":form})        
            
