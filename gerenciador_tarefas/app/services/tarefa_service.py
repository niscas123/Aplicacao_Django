from ..models import Tarefa

def cadastrar_tarefas(tarefa):
    Tarefa.objects.create(titulo=tarefa.titulo, descricao=tarefa.descricao, data_expiracao=tarefa.data_expiracao,
                          prioridade=tarefa.prioridade, usuario=tarefa.usuario)

def listar_tarefa(usuario):
    return Tarefa.objects.filter(usuario=usuario).all()
"""SELECT * FROM app_tarefa;"""
def listar_tarefa_id(id):
    return Tarefa.objects.get(id=id)

def editar_tarefas(tarefa_bd, tarefa_nova):
    tarefa_bd.titulo = tarefa_nova.titulo
    tarefa_bd.descricao = tarefa_nova.descricao
    tarefa_bd.data_expiracao = tarefa_nova.data_expiracao
    tarefa_bd.prioridade = tarefa_nova.prioridade
    tarefa_bd.save(force_update=True)

def remover_tarefas(tarefa_bd):
    tarefa_bd.delete()