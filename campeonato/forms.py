from django import forms
from .models import Modalidade, Equipe

class ModalidadeForm(forms.ModelForm):
    campos = [
        ('feminino', 'Feminino'),
        ('masculino', 'Masculino'),
        ('ambos', 'Ambos')
    ]

    titulo = forms.CharField(label='Título')
    sexoPermitido = forms.ChoiceField(choices=campos, label='Sexo permitido')
    quantidadeDeVagas = forms.IntegerField(label='Quantidade de vagas', initial=100)

    class Meta:
        model = Modalidade
        fields = ('titulo', 'sexoPermitido')

class EquipeForm(forms.ModelForm):
    nome = forms.CharField(max_length = 255, label="Nome da equipe")
    representacao = forms.CharField(max_length = 50, label='Representando... (Nome da turma ou setor representante)') #Nome da turma ou se é uma equipe de servidores e tal
    modalidade = forms.ModelChoiceField(queryset=Modalidade.objects.all())

    class Meta:
        model = Equipe
        fields = ('nome', 'representacao', 'modalidade')