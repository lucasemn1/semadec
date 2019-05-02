from django import forms
from .models import Modalidade, Equipe

class ModalidadeForm(forms.ModelForm):
    nome = forms.CharField(label="Modalidade", max_length=255)
    sexo_permitido = forms.ChoiceField(label="Sexo permitido", choices=[
        (0, 'Masculino'),
        (1, 'Feminino'),
        (2, 'Ambos')
    ])

    class Meta:
        model = Modalidade
        fields = ['nome', 'sexo_permitido']

class EquipeForm(forms.ModelForm):
    nome = forms.CharField(label="Nome da equipe", max_length=255)
    nome_turma = forms.CharField(label='Nome da turma', max_length=40)
    modalidade = forms.ModelChoiceField(queryset=Modalidade.objects.all())

    class Meta:
        model = Equipe
        fields = ['nome', 'nome_turma', 'modalidade']
