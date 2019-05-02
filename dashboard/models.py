from django.db import models
from account.models import Usuario
from semadec import settings
# from django.contrib.auth import get_user_model

class Modalidade(models.Model):
    nome = models.CharField(max_length=255)
    sexo_permitido = models.CharField(max_length=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome

class Equipe(models.Model):
    nome = models.CharField(max_length=255)
    nome_turma = models.CharField(max_length=40)
    modalidade = models.ForeignKey(Modalidade, on_delete=models.CASCADE)
    representante = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='representante')
    participantes = models.ManyToManyField(Usuario, related_name='participantes')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome