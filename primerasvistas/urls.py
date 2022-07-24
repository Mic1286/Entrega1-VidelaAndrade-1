from django.urls import path
from .views import prueba, crear_celular, lista_celulares,editar_celular, eliminar_celular, mostrar_celular

urlpatterns = [
    path('', prueba, name = 'index'),
    path('celulares/', lista_celulares, name = 'lista_celulares'),
    path('crear-celular/', crear_celular, name = 'crear_celular'),
    path('editar-celular/<int:id>/', editar_celular, name='editar_celular'),
    path('eliminar-celulares/<int:id>/', eliminar_celular, name='eliminar_celular'),
    path('mostrar-celulares/<int:id>/', mostrar_celular, name='mostrar_celular'),
]