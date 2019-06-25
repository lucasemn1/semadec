from django.shortcuts import render, redirect, get_object_or_404
from .forms import ModalidadeForm, EquipeForm
from .models import Modalidade, Equipe
from account.models import Usuario
from django.contrib.auth.decorators import login_required

# Create your views here.
class CampeonatoView():
    @staticmethod
    def index(request):
        return render(request, 'visitantes/index.html', {'titulo': 'Teste'})

class ModalidadeView():
    @staticmethod
    @login_required
    def list(request):
        modalidades = Modalidade.objects.all()

        dados = {
            'titulo': 'Modalidades',
            'modalidades': modalidades
        }

        return render(request, 'administracao/modalidades.html', dados)

    @staticmethod
    @login_required
    def create(request):
        form = ModalidadeForm(request.POST or None)

        if form.is_valid():
            form.save()

            return redirect('modalidade_list')
        else:
            dados = {
                'titulo': '',
                'form': form
            }

            return render(request, 'administracao/modalidades_form.html', dados)

    @staticmethod
    @login_required
    def update(request, id):
        modalidade = get_object_or_404(Modalidade, pk=id)

        form = ModalidadeForm(request.POST or None, instance=modalidade)

        if form.is_valid():
            form.save()

            return redirect('modalidade_list')
        else:
            dados = {
                'titulo': '',
                'form': form
            }

            return render(request, 'administracao/modalidades_form.html', dados)

    @staticmethod
    @login_required
    def delete(request, id):
        modalidade = get_object_or_404(Modalidade, pk=id)

        modalidade.delete()

        return redirect('modalidade_list')


class EquipeView():
    @staticmethod
    @login_required
    def list(request):
        equipesParticipantes = []

        for e in Equipe.objects.all():
            if request.user in e.participantes.all() or request.user == e.representante:
                equipesParticipantes.append(e);
        
        equipesRepresentante = []

        for e in Equipe.objects.filter(representante=request.user):
            equipesRepresentante.append({
                'equipe': e,
                'quantidadeDeVagas': EquipeView._getQuantidadeDeVagas(e),
                'participantes': e.participantes.all(),
            })

        dados = {
            'titulo': 'Equipes',
            'equipesParticipantes': equipesParticipantes,
            'equipesRepresentante': equipesRepresentante, 
        }

        return render(request, 'participantes/equipes.html', dados)

    @staticmethod
    @login_required
    def sair(request, id):
        equipe = get_object_or_404(Equipe, pk=id)

        equipe.participantes.remove(request.user.matricula)

        return redirect('equipe_list')

    @staticmethod
    @login_required
    def form_add_participante(request, id_equipe):
        equipe = get_object_or_404(Equipe, pk=id_equipe)
        if equipe.representante == request.user:

            dados = {
                'titulo': 'Adicionar participante na equipe', 
                'equipe': equipe,
            }

            return render(request, 'participantes/add_participante_form.html', dados)
        else:
            return render(request, '404.html', {'titulo': 'ERRO'})

    @staticmethod
    @login_required
    def addParticipante(request, id_equipe):
        equipe = get_object_or_404(Equipe, pk=id_equipe)
        if equipe.representante == request.user:
            try:
                matricula = str(request.POST.get('matricula'))
                usuario = Usuario.objects.get(matricula=matricula)

                if not (usuario == request.user):
                    equipe.participantes.add(usuario)

                    return redirect('equipe_list')
                else:
                    titulo = 'ERRO!'
                    mensagem = 'Você é o lider da equipe, não há necessidade de se registrar na mesma.'

                    return render(request, 'info_pag.html', {'mensagem': mensagem, 'titulo': titulo})

            except Exception as e:
                titulo = 'ERRO!'
                mensagem = 'A matrícula ou a equipe é inválida.' + '\n' + 'Possíveis problemas: <ol><li>A matrícula do usuário não está cadastrada no site.</li><li>A equipe informada é inválida</li></ol>' + 'Por favor, em caso de dúvida entre em contato com os organizadores do evento'

                return render(request, 'info_pag.html', {'mensagem': mensagem, 'titulo': titulo})
        else:
            return render(request, '404.html', {'titulo': 'ERRO'})
    
    @staticmethod
    @login_required
    def remover(request, id_equipe, matricula_user):
        equipe = get_object_or_404(Equipe, pk=id_equipe)

        if equipe.representante == request.user:
            usuario = get_object_or_404(Usuario, pk=matricula_user)
            equipe.participantes.remove(usuario)

            return redirect('equipe_list')
        else:
            return render(request, '404.html', {'titulo': 'ERRO'})

    @staticmethod
    @login_required
    def create(request):
        form = EquipeForm(request.POST or None)

        if form.is_valid():
            equipe = form.save()
            equipe.representante = request.user
            equipe.save()

            return redirect('equipe_list')
        else:
            dados = {
                'titulo': 'Nova equipe',
                'form': form,
            }

            return render(request, 'participantes/equipe_form.html', dados)

    @staticmethod
    @login_required
    def update(request, id):
        equipe = get_object_or_404(Equipe, pk=id)

        if equipe.representante == request.user:
            form = EquipeForm(request.POST or None, instance=equipe)

            if form.is_valid():
                equipe = form.save()

                return redirect('equipe_list')
            else:
                dados = {
                    'titulo': 'Editar equipe',
                    'form': form,
                }

                return render(request, 'participantes/equipe_form.html', dados)
        
        else:
            return render(request, '404.html', {'titulo': 'ERRO'})

    @staticmethod
    @login_required
    def delete(request, id):
        equipe = get_object_or_404(Equipe, pk=id)

        if equipe.representante == request.user:
            equipe.delete()

            return redirect('equipe_list')
        else:
            return render(request, '404.html', {'titulo': 'ERRO'})

    def _getQuantidadeDeVagas(equipe):
        return int( equipe.modalidade.quantidadeDeVagas - equipe.participantes.count() - 1 )