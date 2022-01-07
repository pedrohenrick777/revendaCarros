from django.urls import path

from core.views import *

urlpatterns = [
    path('', listar_carros, name='carro_list'),
    path('cadastrar_carros', cadastrar_carros, name='cadastrar_carros'),
    path('editar_carro/<int:pk>', editar_carro, name='editar_carro'),
    path('remover_carro/<int:pk>', delete_carro, name='remover_carro'),
]