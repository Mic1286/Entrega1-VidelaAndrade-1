from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect, render
from .forms import BusquedaCelulares, FormCelulares
from .models import Celulares
from datetime import datetime
from django.contrib.auth.decorators import login_required

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

login_required
def editar_celular(request, id):
    perro = Celulares.objects.get(id=id)
    
    if request.method == 'POST':
        form = FormCelulares(request.POST)
        if form.is_valid():
            Celulares.marca = form.cleaned_data.get('marca')
            Celulares.modelo = form.cleaned_data.get('modelo')
            Celulares.fecha_registro = form.cleaned_data.get('fecha_registro')
            Celulares.save()
    
            return redirect('listado_celulares')
        
        else:
            return render(request, 'celulares/editar_celulares.html', {'form': form, 'celulares': Celulares})
            
    form_perro = FormCelulares(initial={'marca': Celulares.marca, 'modelo': Celulares.modelo, 'fecha_registro': Celulares.fecha_registro})
    
    return render(request, 'celulares/editar_celulares.html', {'form': FormCelulares, 'Celulares': Celulares})

login_required

def eliminar_celulares(request, id):
    Celulares= Celulares.objects.get(id=id)
    Celulares.delete()
    return redirect('listado_celulares')

def mostrar_celulares(request, id):
    Celulares = Celulares.objects.get(id=id)
    return render(request, 'celulares/mostrar_celulares.html', {'celulares': Celulares}) 
   