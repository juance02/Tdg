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
        fields = ['nombre', 'precio', 'imagen', 'descripcion']



class PerfilForm(forms.ModelForm):
     class Meta:
        model = perfil
        fields = ['image', 'descripcion']


class PersonasForm(forms.ModelForm):
    class Meta:
        model = Personas
        fields = '__all__'
             
        