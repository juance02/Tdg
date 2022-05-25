from django.urls import path
from . import views
from django.contrib import admin
from principal.views import *


urlpatterns = [
    #path('', views.Inicio, name="Inicio"),
    path('Form/', views.Form, name="Form"),
    path('contactar/', views.contactar,name="contactar"),
    #path('Login/', views.Login, name="Login"),
    #path('Registrar/', views.Registrar, name= 'Registrar'),
    #path('Perfil/', views.Perfil, name="Perfil"),
    #path('Categoria/', views.Categoria, name="Categoria"),
    #path('registrarpersona/', views.personasview.index, name="Registrar"),
    #path('guardarregistro/', personasview.procesar_formulario, name='guardarregistro')
    #path('CrearProducto/', views.CrearProducto),
    #path('VistaProducto/', views.VistaProducto),
    path('categoria/', views.ListadoCategoria.as_view(template_name = "categoria/inicio.html"), name='leer'),
 
    # La ruta 'detalles' en donde mostraremos una página con los detalles de un Categoria o registro 
    path('categoria/detalle/<int:pk>', views.CategoriaDetalle.as_view(template_name = "categoria/detalle.html"), name='detalles'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Categoria o registro  
    path('categoria/crear', views.CategoriaCrear.as_view(template_name = "categoria/crear.html"), name='crear'),
 
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un categoriao registro de la Base de Datos 
    path('categoria/editar/<int:pk>', views.CategoriaActualizar.as_view(template_name = "categoria/actualizar.html"), name='actualizar'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un Categoria o registro de la Base de Datos 
    path('categoria/eliminar/<int:pk>', views.CategoriaEliminar.as_view(), name='categoria/eliminar.html'),    
]
    

   



