from django import forms
from .models import Usuario
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario

class SingUpUserForm(UserCreationForm):
    matricula = forms.CharField(label="Matrícula", max_length=14)
    nome = forms.CharField(label='Nome', max_length=255)
    email = forms.EmailField(label='Email', max_length=255)
    cpf = forms.CharField(label='CPF', max_length=11)

    class Meta:
        model = Usuario
        fields = ['matricula', 'nome', 'email', 'cpf', 'password1', 'password2']

    