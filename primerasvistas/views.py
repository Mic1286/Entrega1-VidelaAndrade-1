from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect, render

from .forms import BusquedaCelulares, FormCelulares
from .models import Celulares
from datetime import datetime

def prueba(request):
    return render(request, 'prueba.html')

def crear_celular(request):
       
    if request.method == 'POST':
        form = FormCelulares(request.POST)
        
        if form.is_valid():
            data = form.cleaned_data
            
            fecha = data.get('fecha_registro')
            if not fecha:
                fecha = datetime.now() 
            
            celular = Celulares(
                marca=data.get('marca'),
                modelo=data.get('modelo'),
                fecha_registro=fecha
            )
            celular.save()

            return redirect('lista_celulares')
        
        else:
            return render(request, 'crear_celular.html', {'form': form})
            
    
    form_celular = FormCelulares()
    
    return render(request, 'crear_celular.html', {'form': form_celular})


def lista_celulares(request):
                  
    if request.GET:
        
        marcas = request.GET["marca"]
        buscar = Celulares.objects.filter(marca__icontains=marcas)
        
    else:
         
        buscar = ""
         
    return render(request, 'lista_celulares.html', {'lista_celulares': buscar})
    