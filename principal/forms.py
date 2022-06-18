from dataclasses import fields
import email
from email.mime import image
from pyexpat import model
from tkinter import Widget
from django import forms
from .models import producto

from django.contrib.auth.models import User
#from principal.models import  producto 
from principal.models import *




class ProductoForm(forms.ModelForm):
    #nombre = forms.CharField()
    #precio = forms.FloatField()
    #imagen = forms.ImageField()
    #descripcion = forms.CharField(label='', widget=forms.Textarea(attrs={}))
    

    class  Meta:
        model = producto
        fields = ['nombre', 'precio', 'image','Informacion_de_produccion', 'descripcion','categorias']



class PersonasForm(forms.ModelForm):
    
    class Meta:
        model = Personas
        fields = ['nombres','apellidos','telefono','telefono_celular','correo_principal','correo_secundario','codigo_postal','numero_identificacion','fecha_de_expedicion','edad',
        'tipo_persona_idtipo_persona','departamentos_iddepartamentos','cotizacion_idcotizacion','idtipo_de_documento_fk']
        Widgets = {
            "fecha_de_expedicion": forms.SelectDateWidget()
            }


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'username']

class PerfilUpdateForm(forms.ModelForm):
     class Meta:
        model = perfil
        fields = ['image', 'descripcion']

class ProductoUpdateForm(forms.ModelForm):
     class Meta:
        model = producto
        fields = ['nombre', 'precio', 'image', 'descripcion']

             
        