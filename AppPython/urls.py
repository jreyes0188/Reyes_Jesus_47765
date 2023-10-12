from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView 

urlpatterns = [
    path("inicio/", inicio, name = "Inicio"),
    path("odontologia/", odontologia, name = "Odontologo"),
    path("cardiologia/", cardiologia, name = "Cardiologo"),
    path("dermatologia/", dermatologia, name = "Dermatologo"),
    path("oftalmologia/", oftalmologia, name = "Oftalmologo"),
    path("laboratorio/", laboratorio, name = "Laboratorio"),
    path("acercaDeMi/", acerca_de_mi, name="AcercaDeMi"),
    
    #URL DE FUNCION DE BUSQUEDA DE TURNOS DE ODONTOLOGIA
    path("buscarTurno_Odontologia/", buscadorOdontologia, name = "BuscarTurno_Odontologia"),
    path("resultadoTurno_Odontologia/", resultadoBusqueda_Odontologia, name = "ResultadoTurno_Odontologia"),
    
    #URL DE FUNCION DE BUSQUEDA DE TURNOS DE CARDIOLOGIA
    path("buscarTurno_Cardiologia/", buscadorCardiologia, name = "BuscarTurno_Cardiologia"),
    path("resultadoTurno_Cardiologia/", resultadoBusqueda_Cardiologia, name = "ResultadoTurno_Cardiologia"),
    
    #URL DE FUNCION DE BUSQUEDA DE TURNOS DE DERMATOLOGIA
    path("buscarTurno_Dermatologia/", buscadorDermatologia, name = "BuscarTurno_Dermatologia"),
    path("resultadoTurno_Dermatologia/", resultadoBusqueda_Dermatologia, name = "ResultadoTurno_Dermatologia"),
    
    #URL DE FUNCION DE BUSQUEDA DE TURNOS DE OFTAMOLOGIA
    path("buscarTurno_oftalmologia/", buscadorOftalmologia, name = "BuscarTurno_Oftalmologia"),
    path("resultadoTurno_Oftalmologia/", resultadoBusqueda_Oftalmologia, name = "ResultadoTurno_Oftalmologia"),
    
    #URL DE FUNCION DE BUSQUEDA DE TURNOS DE LABORATORIO
    path("buscarTurno_laboratorio/", buscadorLaboratorio, name = "BuscarTurno_Laboratorio"),
    path("resultadoTurno_Laboratorio/", resultadoBusqueda_Laboratorio, name = "ResultadoTurno_Laboratorio"),
    
    
    #URLs CRUD ODONTOLOGIA
    path("odontologia/list/", ListaTurnos.as_view(), name = "MisTurnos"),
    path("odontologia/<int:pk>", DetalleTurno.as_view(), name = "TurnoDetalle"),
    path("odontologia/crear/", CrearTurno.as_view(), name = "TurnoCrear"),
    path("odontologia/editar/<int:pk>", ActualizarTurno.as_view(), name = "TurnoEditar"),
    path("odontologia/borrar/<int:pk>", BorrarTurno.as_view(), name="TurnoBorrar"),
    
    #URLs CRUD CARDIOLOGIA
    path("cardiologia/list/", ListaTurnos_1.as_view(), name = "MisTurnos_1"),
    path("cardiologia/<int:pk>", DetalleTurno_1.as_view(), name = "TurnoDetalle_1"),
    path("cardiologia/crear/", CrearTurno_1.as_view(), name = "TurnoCrear_1"),
    path("cardiologia/editar/<int:pk>", ActualizarTurno_1.as_view(), name = "TurnoEditar_1"),
    path("cardiologia/borrar/<int:pk>", BorrarTurno_1.as_view(), name="TurnoBorrar_1"),
    
    #URLs CRUD DERMATOLOGIA
    path("dermatologia/list/", ListaTurnos_2.as_view(), name = "MisTurnos_2"),
    path("dermatologia/<int:pk>", DetalleTurno_2.as_view(), name = "TurnoDetalle_2"),
    path("dermatologia/crear/", CrearTurno_2.as_view(), name = "TurnoCrear_2"),
    path("dermatologia/editar/<int:pk>", ActualizarTurno_2.as_view(), name = "TurnoEditar_2"),
    path("dermatologia/borrar/<int:pk>", BorrarTurno_2.as_view(), name="TurnoBorrar_2"),
    
    #URLs CRUD OFTALMOLOGIA
    path("oftalmologia/list/", ListaTurnos_3.as_view(), name = "MisTurnos_3"),
    path("oftalmologia/<int:pk>", DetalleTurno_3.as_view(), name = "TurnoDetalle_3"),
    path("oftalmologia/crear/", CrearTurno_3.as_view(), name = "TurnoCrear_3"),
    path("oftalmologia/editar/<int:pk>", ActualizarTurno_3.as_view(), name = "TurnoEditar_3"),
    path("oftalmologia/borrar/<int:pk>", BorrarTurno_3.as_view(), name="TurnoBorrar_3"),
    
    #URLs CRUD LABORATORIO
    path("laboratorio/list/", ListaTurnos_4.as_view(), name = "MisTurnos_4"),
    path("laboratorio/<int:pk>", DetalleTurno_4.as_view(), name = "TurnoDetalle_4"),
    path("laboratorio/crear/", CrearTurno_4.as_view(), name = "TurnoCrear_4"),
    path("laboratorio/editar/<int:pk>", ActualizarTurno_4.as_view(), name = "TurnoEditar_4"),
    path("laboratorio/borrar/<int:pk>", BorrarTurno_4.as_view(), name="TurnoBorrar_4"),
    
    #URL LOGIN
    path("login/", inicioSesion, name="Login"),
    
    #URL REGISTRO
    path("register/", registro, name="SignUp"),
    
    #URL LOGOUT
    path("logout/", LogoutView .as_view(template_name = "AppPython/logout.html"), name="Logout"),
    
    #URL EDITAR USUARO
    path("editar/", editarUsuario, name="EditarUsuario"),
    
    #URL AVATAR
    path("agregar/", agregarAvatar, name="Avatar"),
]