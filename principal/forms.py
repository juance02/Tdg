from dataclasses import fields
from tkinter import Widget
from django import forms
from .models import Producto


from principal.models import Personas


#class personas1(forms.ModelForm):
 #   class Meta:
  #      model = Personas
   #     fields ={
     #       'nombres',
    #        'apellidos'
      #      'telefono'
       #     'telefono_celular'
        #    'correo_principal'
         #   'correo_secundario'
          #  'numero_identificacion'
           #  widgets = {'fecha_expedicion': forms.DateInput(attrs={'type': 'date'})}
        #}
       


class ProductoForm(forms.ModelForm):
    class  meta:
        model = Producto
        fields = {
            'nombre',
            'descripcion'
            'precio'
            ' categoria_idcategoria'
        }
class personas1(forms.ModelForm):
    class Meta:
         model = Personas
         fields ='__all__'
         widgets = {'fecha_expedicion': forms.DateInput(attrs={'type': 'date'})}