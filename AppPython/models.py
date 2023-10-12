from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Modelos

class Odontologia(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    dni = models.IntegerField()
    email = models.EmailField()
    especialidad = models.CharField(max_length=20, default="")
    fecha_turno = models.DateTimeField(default=timezone.now)

class Cardiologia(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    dni = models.IntegerField()
    email = models.EmailField()
    especialidad = models.CharField(max_length=20, default="")
    fecha_turno = models.DateTimeField(default=timezone.now)

class Dermatologia(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    dni = models.IntegerField()
    email = models.EmailField()
    especialidad = models.CharField(max_length=20, default="")
    fecha_turno = models.DateTimeField(default=timezone.now)

class Oftalmologia(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    dni = models.IntegerField()
    email = models.EmailField()
    especialidad = models.CharField(max_length=20, default="")
    fecha_turno = models.DateTimeField(default=timezone.now)

class Laboratorio(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    dni = models.IntegerField()
    email = models.EmailField()
    especialidad = models.CharField(max_length=20, default="")
    fecha_turno = models.DateTimeField(default=timezone.now)

class Avatar(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="avatares", null=True, blank=True)
