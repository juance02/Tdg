from django.http import HttpRequest
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .forms import  ProductoForm

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
