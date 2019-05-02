from django.shortcuts import render

# Create your views here.
class Visitante():

    @staticmethod
    def index(request):
        return render(request, 'visitantes/index.html', {'titulo': 'Página inicial'})