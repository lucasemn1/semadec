from django.shortcuts import render, redirect
from .forms import ModalidadeForm, EquipeForm
from .models import Modalidade as ModalidadeModel, Equipe as EquipeModel
from account.models import Usuario
from django.db.models import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required

acoes = ('create', 'update')

# Create your views here.
class Dashboard():
    @staticmethod
    @login_required
    def index(request):
        dados={
            'primeiro_nome': str(request.user.nome).split()[0],
            'titulo_pag': 'Página inicial',
            'modalidades': ModalidadeModel.objects.all(),
            'equipes_participantes': EquipeModel.objects.all().exclude(representante=request.user),
            'minhas_equipes': EquipeModel.objects.filter(representante=request.user.matricula),
        }

        return render(request, 'dashboard/index.html', dados)

class Modalidade():
    @staticmethod
    @login_required
    def create(request):
        if request.user.is_superuser:
            if request.method=='POST':
                form = ModalidadeForm(request.POST)

                if form.is_valid():

                    form.save()
                    return redirect("index_dashboard")
            else:
                form = ModalidadeForm()

                dados = {
                    'primeiro_nome': str(request.user.nome).split()[0],
                    'form': form,
                    'titulo_pag': 'Nova modalidade',
                }

                return render(request, 'dashboard/form_modalidade.html', dados)
        else:
            titulo = 'ERRO!'
            mensagem = 'Você não tem permissão para realizar essa ação.'

            return render(request, 'dashboard/info_pag.html', {'mensagem': mensagem, 'titulo': titulo})

    @staticmethod
    @login_required
    def update(request, id):
        if request.user.is_superuser:
            modalidade_obj = ModalidadeModel.objects.get(id=id)

            form = ModalidadeForm(request.POST or None, instance=modalidade_obj)

            if form.is_valid():
                form.save()
                return redirect('index_dashboard')
            else:
                dados = {
                    'primeiro_nome': str(request.user.nome).split()[0],
                    'form': form, 
                    'titulo_pag': 'Editar modalidade',
                    'id': id,
                }

                return render(request, 'dashboard/form_modalidade.html', dados)
        else:
            titulo = 'ERRO!'
            mensagem = 'Você não tem permissão para realizar essa ação.'

            return render(request, 'dashboard/info_pag.html', {'mensagem': mensagem, 'titulo': titulo})

    @staticmethod
    @login_required
    def delete(request, id):
        if request.user.is_superuser:
            modalidade = ModalidadeModel.objects.get(id=id)

            modalidade.delete()

            return redirect('index_dashboard')
        else:
            titulo = 'ERRO!'
            mensagem = 'Você não tem permissão para realizar essa ação.'

            return render(request, 'dashboard/info_pag.html', {'mensagem': mensagem, 'titulo': titulo})

class Equipe():
    @staticmethod
    @login_required
    def create(request):
        if request.method == 'POST':
            form = EquipeForm(request.POST)

            if form.is_valid:
                nome_equipe = form['nome'].value() 

                for e in EquipeModel.objects.all():
                    if nome_equipe == e.nome:
                        titulo = 'ERRO!'
                        mensagem = 'Já existe uma equipe com o nome informado!'

                        return render(request, 'dashboard/info_pag.html', {'titulo': titulo, 'mensagem': mensagem})
                        
                
                equipe = form.save(commit=False)
                equipe.representante = request.user
                equipe.save()

            return redirect('index_dashboard')
        else:
            form = EquipeForm()

            dados = {
                'primeiro_nome': str(request.user.nome).split()[0],
                'form': form,
                'titulo_pag': 'Nova equipe',
            }

            return render(request, 'dashboard/form_equipe.html', dados)

    @staticmethod
    @login_required
    def update(request, id):
        # equipe = get_object_or_404(EquipeModel, pk=id)
        equipe = EquipeModel.objects.get(id=id)
        form = EquipeForm(request.POST or None, instance=equipe)

        if form.is_valid():
            form.save()

            return redirect('index_dashboard')
        else:
            dados = {
                'primeiro_nome': str(request.user.nome).split()[0],
                'form': form, 
                'titulo_pag': 'Editar equipe', 
                'id': id,
            }

            return render(request, 'dashboard/form_equipe.html', dados)

    @staticmethod
    @login_required
    def delete(request, id):
        equipe = EquipeModel.objects.get(id=id)

        equipe.delete()
        
        return redirect('index_dashboard')

    @staticmethod
    @login_required
    def form_add_participante(request, id_equipe):
        if Equipe._is_representante(request.user, id_equipe):
            dados = {
                'primeiro_nome': str(request.user.nome).split()[0],
                'titulo_pag': 'Adicionar participante na equipe', 
                'id_equipe': id_equipe,
            }

            return render(request, 'dashboard/form_novo_participante.html', dados)
        else:
            titulo = 'ERRO!'
            mensagem = 'Você não tem permissão para acessar essa página'

            return render(request, 'dashboard/info_pag.html', {'titulo': titulo, 'mensagem': mensagem})
   
    @staticmethod
    @login_required
    def addParticipante(request, id_equipe):
        if Equipe._is_representante(request.user, id_equipe):
            try:
                matricula = str(request.POST.get('matricula'))
                usuario = Usuario.objects.get(matricula=matricula)

                if not (usuario == request.user):
                    Equipe._addParticipanteNaEquipe(usuario, id_equipe)
                    return redirect('index_dashboard')
                else:
                    titulo = 'ERRO!'
                    mensagem = 'Você é o lider da equipe, não há necessidade de se registrar na mesma.'

                    return render(request, 'dashboard/info_pag.html', {'mensagem': mensagem, 'titulo': titulo})

            except Exception as e:
                titulo = 'ERRO!'
                mensagem = 'A matrícula ou a equipe é inválida.' + '\n' + 'Possíveis problemas: <ol><li>A matrícula do usuário não está cadastrada no site.</li><li>A equipe informada é inválida</li></ol>' + 'Por favor, em caso de dúvida entre em contato com os organizadores do evento'

                return render(request, 'dashboard/info_pag.html', {'mensagem': mensagem, 'titulo': titulo})
        else:
            titulo = 'ERRO!'
            mensagem = 'Você não tem permissão para acessar essa página'

            return render(request, 'dashboard/info_pag.html', {'titulo': titulo, 'mensagem': mensagem})
    
    @staticmethod
    @login_required
    def deleteParticipante(request, id_equipe, matricula):
        if Equipe._is_representante(request.user, id_equipe):

            try:                
                usuario = Usuario.objects.get(matricula=matricula)

                Equipe._removerParticipanteNaEquipe(usuario, id_equipe)

                return redirect('index_dashboard')
            except Exception as e:
                titulo = 'ERRO!'
                mensagem = 'A matrícula ou a equipe é inválida.' + '\n' + 'Possíveis problemas: <ol><li>A matrícula do usuário não está cadastrada no site.</li><li>A equipe informada é inválida</li></ol>' + 'Por favor, em caso de dúvida entre em contato com os organizadores do evento'

                return render(request, 'dashboard/info_pag.html', {'mensagem': mensagem, 'titulo': titulo})
        else:
            titulo = 'ERRO!'
            mensagem = 'Você não tem permissão para acessar essa página'

            return render(request, 'dashboard/info_pag.html', {'titulo': titulo, 'mensagem': mensagem})

    @staticmethod
    @login_required
    def sairDeEquipe(request, id_equipe):
        equipe = EquipeModel.objects.get(id=id_equipe)
        equipe.participantes.remove(request.user)

        return redirect('index_dashboard')

    #MÉTODOS UTILITÁRIOS

    @staticmethod
    def _is_representante(user, id_equipe):
        if user.matricula == EquipeModel.objects.get(id=id_equipe).representante.matricula:    
            return True
        else:
            return False

    @staticmethod
    def _addParticipanteNaEquipe(user, id_equipe):
        equipe = EquipeModel.objects.get(id=id_equipe)

        equipe.participantes.add(user)

    @staticmethod
    def _removerParticipanteNaEquipe(user, id_equipe):
        equipe = EquipeModel.objects.get(id=id_equipe)

        equipe.participantes.remove(user)
