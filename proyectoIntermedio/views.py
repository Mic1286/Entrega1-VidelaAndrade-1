from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import BusquedaCelulares
from .models import Celulares


class ListadoCelulares(ListView):
    model=Celulares
    template_name = 'celulares/listado_celulares.html'

    def get_queryset(self):
        apodo = self.request.GET.get('marca', '')
        if apodo:
            object_list = self.model.objects.filter(apodo__icontains=apodo)
        else:
            object_list = self.model.objects.all()
        return object_list
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = BusquedaCelulares()
        return context
    
    
class CrearCelulares(CreateView):
    model=Celulares
    template_name = 'celular/crear_celulares.html'
    success_url = '/proyectoIntermedio/celulares'
    fields = ['modelo', 'marca', 'fecha_registro']


class EditarCelulares(LoginRequiredMixin, UpdateView):
    model=Celulares
    template_name = 'celulares/editar_celulares.html'
    success_url = '/proyectoIntermedio/celulares'
    fields = ['modelo', 'marca', 'fecha_registro']


class EliminarCelulares(LoginRequiredMixin, DeleteView):
    model=Celulares
    template_name = 'celulares/eliminar_celulares.html'
    success_url = '/proyectoIntermedio/celulares'


class MostrarCelulares(DetailView):
    model = Celulares
    template_name = 'celulares/mostrar_celulares.html'