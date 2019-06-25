from django.urls import path
from campeonato.views import ModalidadeView, CampeonatoView, EquipeView

urlpatterns = [
    # Modalidades
    path('modalidades/', ModalidadeView.list, name='modalidade_list'),
    path('modalidades/criar', ModalidadeView.create, name='modalidade_create'),
    path('modalidades/update/<int:id>', ModalidadeView.update, name='modalidade_update'),
    path('modalidades/delete/<int:id>', ModalidadeView.delete, name='modalidade_delete'),

    # Equipes
    path('equipes/', EquipeView.list, name='equipe_list'),
    path('equipes/sair/<int:id>', EquipeView.sair, name='equipe_sair'),
    path('equipes/form_participar/<int:id_equipe>', EquipeView.form_add_participante, name='equipe_participar_form'),
    path('equipes/participar/<int:id_equipe>', EquipeView.addParticipante, name='equipe_participar'),
    path('equipes/remover/<int:id_equipe>/<str:matricula_user>', EquipeView.remover, name='equipe_remover'),
    path('equipes/criar', EquipeView.create, name='equipe_create'),
    path('equipes/update/<int:id>', EquipeView.update, name='equipe_update'),
    path('equipes/delete/<int:id>', EquipeView.delete, name='equipe_delete'),
    # path('modalidades/criar', ModalidadeView.create, name='modalidade_create'),
    # path('modalidades/update/<int:id>', ModalidadeView.update, name='modalidade_update'),
    # path('modalidades/delete/<int:id>', ModalidadeView.delete, name='modalidade_delete'),
]