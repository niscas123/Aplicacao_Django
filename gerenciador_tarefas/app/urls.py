from django.urls import *
from .views.tarefa_views import *
from .views.usuario_views import *

urlpatterns = [
    path('listar_tarefas/', listar_tarefas, name='listar_tarefas'),
    path('cadastrar_tarefas/', cadastrar_tarefas, name='cadastrar_tarefas'),
    path('editar_tarefas/<int:id>', editar_tarefas, name='editar_tarefas'),
    path('remover_tarefas/<int:id>', remover_tarefas, name='remover_tarefas'),
    path('cadastrar_usuario/', cadastrar_usuario, name='cadastrar_usuario'),
    path('logar_usuario/', logar_usuario, name='logar_usuario'),
    path('deslogar_usuario/', deslogar_usuario, name='deslogar_usuario'),
]