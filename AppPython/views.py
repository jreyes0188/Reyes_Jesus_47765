from django.shortcuts import render, HttpResponse
from .models import *
from .forms import UsuarioRegistro, FormularioEditar, AvatarFormulario

# Authenticate y Login User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate

# CRUD
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# MIXIN
from django.contrib.auth.mixins import LoginRequiredMixin

# DECORADOR
from django.contrib.auth.decorators import login_required


# Views

def inicio(request):
    return render (request, "AppPython/inicio.html")

def odontologia(request):
    return render (request, "AppPython/odontologia.html")

def cardiologia(request):
    return render (request, "AppPython/cardiologia.html")

def dermatologia(request):
    return render (request, "AppPython/dermatologia.html")

def oftalmologia(request):
    return render (request, "AppPython/oftalmologia.html")

def laboratorio(request):
    return render (request, "AppPython/laboratorio.html")

def acerca_de_mi(request):
    return render(request, "AppPython/acerca_de_mi.html")


# FUNCION INICIO DE SESION

def inicioSesion(request):
    
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        
        if form.is_valid():
            usuario = form.cleaned_data.get("username")
            contraseña = form.cleaned_data.get("password")
            
            user = authenticate(username = usuario, password = contraseña)
            
            if user:
                login(request, user)
                return render(request, "AppPython/inicio.html", {"mensaje": f"Bienvenido {usuario}"})
        
        else:
            return render(request, "AppPython/inicio.html", {"mensaje":"Usuario o Contraseña incorrectos"})
    
    else:
        form = AuthenticationForm()
    
    return render(request, "AppPython/login.html", {"formulario":form})


# FUNCION DE REGISTRO

def registro(request):
    
    if request.method == "POST":
        form = UsuarioRegistro(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data["username"]
            form.save()
            return render(request, "AppPython/inicio.html", {"mensaje":"Usuario creado con exito."})
    
    else:
        form = UsuarioRegistro()
    
    return render(request, "AppPython/registro.html", {"formulario":form})


# FUNCION DE EDITAR USUARIO

@login_required
def editarUsuario(request):
    usuario = request.user
    
    if request.method == "POST":
        form = FormularioEditar(request.POST)
        
        if form.is_valid():
            info = form.cleaned_data
            
            usuario.email = info["email"]
            usuario.set_password(info["password1"])
            usuario.firt_name = info["first_name"]
            usuario.last_name = info["last_name"]
            
            usuario.save()
            
            return render(request, "AppPython/inicio.html")
    
    else:
        form = FormularioEditar(initial={
            "email": usuario.email,
            "first_name": usuario.first_name,
            "last_name": usuario.last_name,
        })
    
    return render(request, "AppPython/editarPerfil.html", {"formulario":form, "usuario":usuario})


# AVATAR

@login_required
def agregarAvatar(request):
    
    if request.method == "POST":
        form = AvatarFormulario(request.POST, request.FILES)
        
        if form.is_valid():
            usuarioActual = User.objects.get(username=request.user)
            avatar = Avatar(usuario=usuarioActual, imagen=form.cleaned_data.get("imagen")) 
            avatar.save()
            return render(request, "AppPython/inicio.html")
    else:
        form = AvatarFormulario()
    return render(request, "AppPython/agregarAvatar.html", {"formulario": form})



# BUSCADOR DE TURNOS DE ODONTOLOGIA
def buscadorOdontologia(request):
    return render (request, "AppPython/odontologia_list.html")

# RESULTADO DE LA BUSQUEDA DE TURNOS DE ODONTOLOGIA
def resultadoBusqueda_Odontologia(request):
    if 'especialidad' in request.GET:
        especialidad = request.GET['especialidad']
        odontologias = Odontologia.objects.filter(especialidad__icontains=especialidad)
        return render(request, "AppPython/odontologia_list.html", {"odontologia": odontologias, "especialidad": especialidad})
    else:
        respuesta = "No realizaste tu consulta"
        return render(request, "AppPython/odontologia_list.html", {"respuesta": respuesta})


# RESULTADO DE LA BUSQUEDA DE TURNOS DE CARDIOLOGIA
def buscadorCardiologia(request):
    return render (request, "AppPython/cardiologia_list.html")

# RESULTADO DE LA BUSQUEDA DE TURNOS DE CARDIOLGIA
def resultadoBusqueda_Cardiologia(request):
    if 'especialidad' in request.GET:
        especialidad = request.GET['especialidad']
        cardiologias = Cardiologia.objects.filter(especialidad__icontains=especialidad)
        return render(request, "AppPython/cardiologia_list.html", {"cardiologia": cardiologias, "especialidad": especialidad})
    else:
        respuesta = "No realizaste tu consulta"
        return render(request, "AppPython/cardiologia_list.html", {"respuesta": respuesta})


# RESULTADO DE LA BUSQUEDA DE TURNOS DE DERMATOLOGIA
def buscadorDermatologia(request):
    return render (request, "AppPython/dermatologia_list.html")

# RESULTADO DE LA BUSQUEDA DE TURNOS DE DERMATOLOGIA
def resultadoBusqueda_Dermatologia(request):
    if 'especialidad' in request.GET:
        especialidad = request.GET['especialidad']
        dermatologias = Dermatologia.objects.filter(especialidad__icontains=especialidad)
        return render(request, "AppPython/dermatologia_list.html", {"dermatologia": dermatologias, "especialidad": especialidad})
    else:
        respuesta = "No realizaste tu consulta"
        return render(request, "AppPython/dermatologia_list.html", {"respuesta": respuesta})


# RESULTADO DE LA BUSQUEDA DE TURNOS DE OFTALMOLOGIA
def buscadorOftalmologia(request):
    return render (request, "AppPython/oftalmologia_list.html")

# RESULTADO DE LA BUSQUEDA DE TURNOS DE OFTALMOLOGIA
def resultadoBusqueda_Oftalmologia(request):
    if 'especialidad' in request.GET:
        especialidad = request.GET['especialidad']
        oftalmologias = Oftalmologia.objects.filter(especialidad__icontains=especialidad)
        return render(request, "AppPython/oftalmologia_list.html", {"oftalmologia": oftalmologias, "especialidad": especialidad})
    else:
        respuesta = "No realizaste tu consulta"
        return render(request, "AppPython/oftalmologia_list.html", {"respuesta": respuesta})


# RESULTADO DE LA BUSQUEDA DE TURNOS DE LABORATORIO
def buscadorLaboratorio(request):
    return render (request, "AppPython/laboratorio_list.html")

# RESULTADO DE LA BUSQUEDA DE TURNOS DE LABORATORIO
def resultadoBusqueda_Laboratorio(request):
    if 'especialidad' in request.GET:
        especialidad = request.GET['especialidad']
        laboratorios = Laboratorio.objects.filter(especialidad__icontains=especialidad)
        return render(request, "AppPython/laboratorio_list.html", {"laboratorio": laboratorios, "especialidad": especialidad})
    else:
        respuesta = "No realizaste tu consulta"
        return render(request, "AppPython/laboratorio_list.html", {"respuesta": respuesta})


# LISTAS DE ODONTOLOGIA

class ListaTurnos(LoginRequiredMixin, ListView):
    model = Odontologia

class DetalleTurno(LoginRequiredMixin, DetailView):
    model = Odontologia

class CrearTurno(LoginRequiredMixin, CreateView):
    model = Odontologia
    success_url = "/AppPython/odontologia/list"
    fields = ['nombre', 'apellido', 'dni', 'email', 'especialidad', 'fecha_turno']

class ActualizarTurno(LoginRequiredMixin, UpdateView):
    model = Odontologia
    success_url = "/AppPython/odontologia/list"
    fields = ['nombre', 'apellido', 'dni', 'email', 'especialidad', 'fecha_turno']

class BorrarTurno(LoginRequiredMixin, DeleteView):
    model = Odontologia
    success_url = "/AppPython/odontologia/list"


# LISTAS DE CARDIOLOGIA

class ListaTurnos_1(LoginRequiredMixin, ListView):
    model = Cardiologia

class DetalleTurno_1(LoginRequiredMixin, DetailView):
    model = Cardiologia

class CrearTurno_1(LoginRequiredMixin, CreateView):
    model = Cardiologia
    success_url = "/AppPython/cardiologia/list"
    fields = ['nombre', 'apellido', 'dni', 'email', 'especialidad', 'fecha_turno']

class ActualizarTurno_1(LoginRequiredMixin, UpdateView):
    model = Cardiologia
    success_url = "/AppPython/cardiologia/list"
    fields = ['nombre', 'apellido', 'dni', 'email', 'especialidad', 'fecha_turno']

class BorrarTurno_1(LoginRequiredMixin, DeleteView):
    model = Cardiologia
    success_url = "/AppPython/cardiologia/list"


# LISTAS DE DERMATOLOGIA

class ListaTurnos_2(LoginRequiredMixin, ListView):
    model = Dermatologia

class DetalleTurno_2(LoginRequiredMixin, DetailView):
    model = Dermatologia

class CrearTurno_2(LoginRequiredMixin, CreateView):
    model = Dermatologia
    success_url = "/AppPython/dermatologia/list"
    fields = ['nombre', 'apellido', 'dni', 'email', 'especialidad', 'fecha_turno']

class ActualizarTurno_2(LoginRequiredMixin, UpdateView):
    model = Dermatologia
    success_url = "/AppPython/dermatologia/list"
    fields = ['nombre', 'apellido', 'dni', 'email', 'especialidad', 'fecha_turno']

class BorrarTurno_2(LoginRequiredMixin, DeleteView):
    model = Dermatologia
    success_url = "/AppPython/dermatologia/list"


# LISTAS DE OFTALMOLOGIA

class ListaTurnos_3(LoginRequiredMixin, ListView):
    model = Oftalmologia

class DetalleTurno_3(LoginRequiredMixin, DetailView):
    model = Oftalmologia

class CrearTurno_3(LoginRequiredMixin, CreateView):
    model = Oftalmologia
    success_url = "/AppPython/oftalmologia/list"
    fields = ['nombre', 'apellido', 'dni', 'email', 'especialidad', 'fecha_turno']

class ActualizarTurno_3(LoginRequiredMixin, UpdateView):
    model = Oftalmologia
    success_url = "/AppPython/oftalmologia/list"
    fields = ['nombre', 'apellido', 'dni', 'email', 'especialidad', 'fecha_turno']

class BorrarTurno_3(LoginRequiredMixin, DeleteView):
    model = Oftalmologia
    success_url = "/AppPython/oftalmologia/list"


# LISTAS DE LABORATORIO

class ListaTurnos_4(LoginRequiredMixin, ListView):
    model = Laboratorio

class DetalleTurno_4(LoginRequiredMixin, DetailView):
    model = Laboratorio

class CrearTurno_4(LoginRequiredMixin, CreateView):
    model = Laboratorio
    success_url = "/AppPython/laboratorio/list"
    fields = ['nombre', 'apellido', 'dni', 'email', 'especialidad', 'fecha_turno']

class ActualizarTurno_4(LoginRequiredMixin, UpdateView):
    model = Laboratorio
    success_url = "/AppPython/laboratorio/list"
    fields = ['nombre', 'apellido', 'dni', 'email', 'especialidad', 'fecha_turno']

class BorrarTurno_4(LoginRequiredMixin, DeleteView):
    model = Laboratorio
    success_url = "/AppPython/laboratorio/list"
