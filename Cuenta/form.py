from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class UserRegisterForm(UserCreationForm):


    email : forms.EmailField()
    password1 = forms.CharField(label= 'Contraseña' , widget = forms.PasswordInput)
    password2 = forms.CharField(label= 'Reperitr la contraseña', widget = forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username' ,'email' ,'password1' ,'password2']

        help_texts = {k:"" for k in fields}



class UserEditForm(UserCreationForm):


    email = forms.EmailField(label = "Modificar E-mail")
    password1 = forms.CharField(label = 'Contraseña', widget = forms.PasswordInput(), required=False)
    password2 = forms.CharField(label=' Repetir contraseña ', widget= forms.PasswordInput(), required=False)
    nombre = forms.CharField(label="Nombre", max_length=20, required=False)
    apellido = forms.CharField(label="Apellido", max_length=20)



    class Meta:
        model = User
        fields = ['email' , 'password1' , 'password2']

        help_text = {k:"" for k in fields}



