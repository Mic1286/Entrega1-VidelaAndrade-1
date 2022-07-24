from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class FormCelulares(forms.Form):
    marca = forms.CharField(max_length=20)
    modelo = forms.CharField(max_length=50)
    fecha_registro = forms.DateField(required=False)
    
    
class BusquedaCelulares(forms.Form):
    nombre = forms.CharField(max_length=30, required=False)