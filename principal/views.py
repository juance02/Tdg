from ast import Return
from email import message
from multiprocessing import context
from multiprocessing.dummy import current_process
from webbrowser import get
from wsgiref.util import request_uri
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages 
from http.client import REQUEST_TIMEOUT
#from itertools import product
from urllib.request import Request
from django.urls import reverse
#from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail
from django.conf import settings
#from principal.models import Producto
#from principal.models import Perfil
#from principal.models import Producto
from .forms import *
from django.contrib.auth.models import  User
from django.contrib.auth.decorators import  login_required

#from django.views.generic import ListView, DetailView 
#from django.views.generic.edit import CreateView, UpdateView, DeleteView
#importo el modelo de la base de datos de models.py
#from .models import *
# Habilitamos el uso de mensajes en Django

 
# Habilitamos los mensajes para class-based views 
#from django.contrib.messages.views import SuccessMessageMixin 
 
# Habilitamos los formularios en Django
#from django import forms



#from principal.forms import personas1
#from principal.forms import  Userform, ProductoForm 
# Create your views here.

def Inicio(request):
    product = producto.objects.all()

    context = { 'product': product}
    return render(request, "index.html", context)

def  plantilla(request):
     product = producto.objects.all()

     context = { 'product': product}
     return render(request,"plantillas.html", context)
def  indexp(request):
    
     return render(request,"indexp.html")

#def contactar(request):
    #if request.method == "POST":
     #   asunto = request.POST["txtAsunto"]
      #  descripcion = request.POST["textmsg"] + "/ Email: " + request.POST["txtEmail"]
       # email_desde = settings.EMAIL_HOST_USER
        #email_para = ["didiervalenciarodriguez@gmail.com"]
        #send_mail(asunto,descripcion,email_desde,email_para,  fail_silently=False)
     #   return render(request,"contactoExitoso.html")
    #return render(request,"Form.html")
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user) 
            messages.success(request, f'Usuario {username} creado')         
            return redirect('Form')
            
    else:
        form = UserCreationForm()

    return render(request, 'registration/register.html', {"form": form} )

@login_required
def agregar_Producto(request):
    current_user = get_object_or_404(User, pk=request.user.pk)

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            producto = formulario.save(commit=False)
            producto.user = current_user
            producto.save()
            messages.success(request, 'producto cargado')
            return redirect ('perfil')

    else:
        formulario = ProductoForm()

    return render(request, 'app/producto/agregarproducto.html', {'formulario' : formulario})
@login_required
def listar_productos(request):
    productos = producto.objects.all()
    data ={
        'productos': productos
    }
    return render(request, 'app/producto/listar.html', data)
@login_required
def modificar_producto(request,pk):
    
    Producto = get_object_or_404(producto, pk=pk)

    data = {
        'form': ProductoForm(instance=Producto)
    }
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=Producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="listar_productos")
        data["form"] = formulario    
    return render(request, 'app/producto/modificar.html', data)

def eliminar_producto(request, pk):
    Producto = get_object_or_404(producto, pk=pk)
    Producto.delete()
    return redirect(to="listar_productos")


def editar_Perfil(request):
    if request.method == 'POST':
        u_formulario = UserUpdateForm(request.POST, instance=request.user)
        p_formulario = PerfilUpdateForm(request.POST, request.FILES, instance=request.user.perfil)
        if u_formulario.is_valid() and p_formulario.is_valid():
            u_formulario.save()
            p_formulario.save()
            return redirect('perfil')
            

    else:
        u_formulario = UserUpdateForm(instance=request.user)
        p_formulario = PerfilUpdateForm()
    context= {'u_formulario' : u_formulario, 'p_formulario':p_formulario}
    return render(request, 'app/perfil/crearPerfil.html', context)
    

def Categoria(request):
    return render(request, "Categoria.html")


def perfil(request, username=None):

    current_user = request.user
    if username and username !=current_user.username:
        user = User.objects.get(username=username)
        product = user.product.all()

    else:
        product = current_user.product.all()
        user = current_user
    return render(request, 'app/perfil/perfil.html', {'user':user, 'product':product})

def perfilusu(request, username=None):

    current_user = request.user
    if username and username !=current_user.username:
        user = User.objects.get(username=username)
        product = user.product.all()

    else:
        product = current_user.product.all()
        user = current_user
    return render(request, 'app/perfil/perfilusuarios.html', {'user':user, 'product':product})
@login_required
def agregar_personas(request):
    current_user = get_object_or_404(User, pk=request.user.pk)

    if request.method == 'POST':
        formulario = PersonasForm(data=request.POST)
        if formulario.is_valid():
            Personas = formulario.save(commit=False)
            Personas.user = current_user
            Personas.save()
            messages.success(request, 'Formulario de contacto cargado')
            return redirect ('contacto')

    else:
        formulario = PersonasForm()

    return render(request, 'app/personas/personas.html', {'formulario' : formulario})

@login_required
def contacto(request, username=None):
    current_user = request.user
    if username and username !=current_user.username:
        user = User.objects.get(username=username)
        contact1 = user.contact1.all()

    else:
        contact1 = current_user.contact1.all()
        user = current_user
    return render(request, 'contacto/contacto.html', {'user':user, 'contact1':contact1})


def  verProducto(request, username=None):
    current_user = request.user
    if username and username !=current_user.username:
        user = User.objects.get(username=username)
        product = user.product.all()

    else:
        product = current_user.product.all()
        user = current_user
    return render(request, 'app/producto/product-single.html',{'user':user, 'product':product})

def  verProductoo(request, pk):
    productos = producto.objects.filter(pk=pk)
    data ={
        'productos': productos
    } 
    return render(request, 'vistas12.html', data)
    

def editar_Producto(request,pk):
    current_user = get_object_or_404(User, pk=request.user.pk)

    
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            producto.formulario.save(commit=False)
            producto.user = current_user
            return redirect(to="listar_productos")
           
    return render(request, 'app/producto/editarproducto.html', )

     
def cart(request):
    return render (request,"cart.html") 


def contact(request):
    if request.method == "POST":
        asunto = request.POST["txtAsunto"]
        descripcion = request.POST["textmsg"] + "/ Email: " + request.POST["txtEmail"]
        email_desde = settings.EMAIL_HOST_USER
        email_para = ["didiervalenciarodriguez@gmail.com"]
        send_mail(asunto,descripcion,email_desde,email_para,  fail_silently=False)
        return render(request,"contact.html")

        
  
   

