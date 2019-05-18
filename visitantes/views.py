from django.shortcuts import render

# Create your views here.
class Visitante():

    @staticmethod
    def index(request):
        dados = {
            'titulo': 'Página inicial',
        }

        if request.user.is_authenticated:
            dados['primeiro_nome'] = str(request.user.nome).split()[0]

        return render(request, 'visitantes/index.html', dados)