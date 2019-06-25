from django.db import models
from account.models import Usuario

class Modalidade(models.Model):
    titulo = models.CharField(max_length=255)
    sexoPermitido = models.CharField(max_length=11)
    quantidadeDeVagas = models.IntegerField(default=100)

    class Meta:
        verbose_name = 'modalidade'
        verbose_name_plural = 'modalidades'

    def __str__(self):
        return str('%s / %s vagas' % (self.titulo, self.quantidadeDeVagas))


class Equipe(models.Model):
    nome = models.CharField(max_length = 255, unique=True)
    representacao = models.CharField(max_length = 50) #Nome da turma ou se é uma equipe de servidores e tal
    modalidade = models.ForeignKey(Modalidade, on_delete=models.CASCADE)
    representante = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='representante', null=True, blank=True)
    participantes = models.ManyToManyField(Usuario, related_name='participantes')
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'equipe'
        verbose_name_plural = 'equipes'

    def __str__(self):
        return str(self.nome)
