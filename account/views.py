from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, logout
from .forms import SingUpUserForm 
from django.contrib.auth import login as auth_login

# Create your views here.
class SessaoView():
    @staticmethod
    def singup(request):
        if request.user.is_authenticated:
            form = SingUpUserForm(request.POST or None)

            if form.is_valid():
                form.save()

                return redirect('login')
            else:
                return render(request, 'registration/registre.html', {'form': form, 'titulo_pag': 'SINGUP'})
        else:
            return redirect('index')

    @staticmethod
    def update(request):
        form = SingUpUserForm(request.POST or None, instance=request.user)

        if form.is_valid():
            # password1 = form.cleaned_data['password1']
            # password2 = form.cleaned_data['password2']

            form.save()

            return redirect('index_user')
        else:
            return render(request, 'registration/update.html', {'form': form, 'titulo_pag': 'A'})

    """
    @staticmethod
    def login(request):

        form =  (request.POST or None)
        # matricula = form.cleaned_data['matricula']
        # password = form.cleaned_data['password']
        # user = authenticate(matricula=matricula, password=password)
        print(f)

        # if SessaoView._isLoginValido(matricula, password):
        #     user = authenticate(matricula=matricula, password=password)
        #     retorno = auth_login(request, user)
        #     print(retorno)
        #     return redirect('index')
        
        # else:
        return render(request, 'registration/login.html', {'form': form, 'titulo_pag': 'LOGIN'})
    """
    @staticmethod
    def logout(request):
        logout(request)

        return redirect('login')

    @staticmethod
    def _isLoginValido(matricula, senha):
        palavras_de_risco_sql = ['INSERT', 'UPDATE', 'DELETE', 'TRUNCATE', 'SELECT', 'FROM', 'WHERE']
        matricula_detalhada = str(matricula).split()
        senha_detalhada = str(matricula).split()

        for palavra in matricula_detalhada:
            for palavra_de_risco in palavras_de_risco_sql:
                if palavra_de_risco == palavra:
                    return False

        for palavra in senha_detalhada:
            for palavra_de_risco in palavras_de_risco_sql:
                if palavra_de_risco == palavra:
                    return False

        return True