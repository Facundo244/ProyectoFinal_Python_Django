from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):

    username = forms.CharField(label="Usuario", max_length=20)
    email : forms.EmailField(label="Email")
    password1 = forms.CharField(label= 'Contraseña' , widget = forms.PasswordInput)
    password2 = forms.CharField(label= 'Reperitr la contraseña', widget = forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username','email' ,'password1' ,'password2',]

        help_texts = {k:"" for k in fields}


class User_Edit_Form(UserCreationForm):

    username = forms.CharField(label="Usuario", max_length=20)
    email : forms.EmailField(label="Email")
    password1 = forms.CharField(label= ' Modificar Contraseña' , widget = forms.PasswordInput)
    password2 = forms.CharField(label= 'Confirmar contraseña', widget = forms.PasswordInput)

    last_name = forms.CharField(label='Modificar el apellido')
    first_name = forms.CharField(label='Modificar el nombre')

    class Meta:
        model = User
        fields = ['username','email','password1','password2','first_name','last_name']

        help_texts = {k:"" for k in fields}


