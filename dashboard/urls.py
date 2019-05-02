from django.urls import path
from .views import Dashboard, Modalidade, Equipe

urlpatterns = [
    path('', Dashboard.index, name='index_dashboard'),

    #Modalidade
    path('modalidade/create', Modalidade.create, name='modalidade_create'),
    path('modalidade/update/<int:id>', Modalidade.update, name='modalidade_update'),
    path('modalidade/delete/<int:id>', Modalidade.delete, name='modalidade_delete'),

    #Equipe
    path('equipe/create', Equipe.create, name='equipe_create'),
    path('equipe/update/<int:id>', Equipe.update, name='equipe_update'),
    path('equipe/delete/<int:id>', Equipe.delete, name='equipe_delete'),
    path('equipe/form_participar/<int:id_equipe>', Equipe.form_add_participante, name="form_add_participante"), #Form add
    path('equipe/remover_usuario/<int:id_equipe>/<str:matricula>', Equipe.deleteParticipante, name="equipe_remover_participante"),
    path('equipe/sair/<int:id_equipe>', Equipe.sairDeEquipe, name='equipe_sair'),

    #Usuários
    path('equipe/participar_in/<int:id_equipe>', Equipe.addParticipante, name="equipe_participar"),
]