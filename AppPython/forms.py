from django import forms
from django.utils import timezone

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from AppPython.models import Avatar

class Odontologia_Form(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=20)
    dni = forms.IntegerField()
    email = forms.EmailField()
    especialidad = forms.CharField(max_length=20)
    fecha_turno = forms.DateTimeField(initial=timezone.now)

class Cardiologia_Form(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=20)
    dni = forms.IntegerField()
    email = forms.EmailField()
    especialidad = forms.CharField(max_length=20)
    fecha_turno = forms.DateTimeField(initial=timezone.now)

class Dermatologia_Form(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=20)
    dni = forms.IntegerField()
    email = forms.EmailField()
    especialidad = forms.CharField(max_length=20)
    fecha_turno = forms.DateTimeField(initial=timezone.now)

class Oftalmologia_Form(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=20)
    dni = forms.IntegerField()
    email = forms.EmailField()
    especialidad = forms.CharField(max_length=20)
    fecha_turno = forms.DateTimeField(initial=timezone.now)

class Laboratorio_Form(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=20)
    dni = forms.IntegerField()
    email = forms.EmailField()
    especialidad = forms.CharField(max_length=20)
    fecha_turno = forms.DateTimeField(initial=timezone.now)


# USUARIO REGISTRO
class UsuarioRegistro(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label = "Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label = "Repetir Contraseña", widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name", "password1", "password2"]


# EDITAR USUARIO
class FormularioEditar(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label = "Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label = "Repetir Contraseña", widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ["email", "first_name", "last_name", "password1", "password2"]


# AVATAR
class AvatarFormulario(forms.ModelForm):
    
    class Meta:
        model = Avatar
        fields = ["imagen"]