from django.urls import path
from . import views


urlpatterns = [
    path('', views.Inicio, name="Inicio"),
    path('Form/', views.Form, name="Form"),
    path('contactar/', views.contactar,name="contactar"),
    path('Login/', views.Login, name="Login"),
    path('Registrar/', views.Registrar, name= 'Registrar'),
    path('Perfil/', views.Perfil, name="Perfil"),
    #path('registrarpersona/', views.personasview.index, name="Registrar"),
    #path('guardarregistro/', personasview.procesar_formulario, name='guardarregistro')
    path('CrearProducto/', views.CrearProducto),
   



]