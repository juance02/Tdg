from django.http import HttpRequest
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .forms import  ProductoForm
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
#importo el modelo de la base de datos de models.py
from .models import *
# Habilitamos el uso de mensajes en Django
from django.contrib import messages 
 
# Habilitamos los mensajes para class-based views 
from django.contrib.messages.views import SuccessMessageMixin 
 
# Habilitamos los formularios en Django
from django import forms



from principal.forms import personas1

# Create your views here.

def Inicio(request):
    return render(request, "index.html")

def  Form(request):
     return render(request,"Form.html")

def contactar(request):
    if request.method == "POST":
        asunto = request.POST["txtAsunto"]
        descripcion = request.POST["textmsg"] + "/ Email: " + request.POST["txtEmail"]
        email_desde = settings.EMAIL_HOST_USER
        email_para = ["didiervalenciarodriguez@gmail.com"]
        send_mail(asunto,descripcion,email_desde,email_para,  fail_silently=False)
        return render(request,"contactoExitoso.html")
    return render(request,"Form.html")


def CrearProducto(request):
    if request.method == "POST":
        form = ProductoForm(request.POST)
        if form.is_valid():
             form.save() 
             return redirect("index.html")
    else:
        form = ProductoForm()
    return render (request, "CrearProducto.html",{'form':form})



def Login(request):
    return render(request,"Login.html")

def Registrar(request):
    return render(request,"Registrar.html")  


def Perfil(request):
    return render(request, "Perfil.html")

def Categoria(request):
    return render(request, "Categoria.html")



class personasview(HttpRequest):
     
     def index(request):
       Personas = personas1 ()  
       return render(request, "Registrar.html", {"form":Personas})



     def procesar_formulario(request):
         Personas = personas1(request.POST)

         if Personas.is_valid():
             Personas.save()
             Personas = personas1()

         return render(request, "Registrar.html", {"form":Personas, "mensaje": 'ok'})  

         
          
def VistaProducto(request):
   return render(request, "VistaProducto.html")



class ListadoCategoria(ListView):
    model = Categoria
    
    
class CategoriaCrear(SuccessMessageMixin, CreateView):
    model =Categoria
    form = Categoria
    fields = "__all__"
    success_message ='Categoria creada correctamente'
     
    def get_success_url(self):        
        return reverse('leer') # Redireccionamos a la vista principal 'leer'

class CategoriaDetalle (DetailView):
    model =Categoria

class  CategoriaActualizar(SuccessMessageMixin,UpdateView):
    model =  Categoria
    form = Categoria
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Categoria Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 

    def get_success_url(self):               
        return reverse('leer') # Redireccionamos a la vista principal 'leer'
class CategoriaEliminar(SuccessMessageMixin, DeleteView): 
    model = Categoria 
    form = Categoria
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Categoria Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('leer') # Redireccionamos a la vista principal 'leer'
 
   

