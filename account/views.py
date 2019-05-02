from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from .forms import SingUpUserForm

# Create your views here.
class SessaoView():
    @staticmethod
    def singup(request):
        form = SingUpUserForm(request.POST or None)

        if form.is_valid():
            form.save()

            return redirect('login')

        else:
            return render(request, 'registration/registre.html', {'form': form, 'titulo_pag': 'SINGUP'})

    @staticmethod
    def update(request):
        pass
        # form = SingUpUserForm(request.POST or None, instance=request.user)

        # if form.is_valid():
        #     # password1 = form.cleaned_data['password1']
        #     # password2 = form.cleaned_data['password2']

        #     form.save()

        #     return redirect('index_dashboard')
        # else:
        #     return render(request, 'registration/registre.html', {'form': form, 'titulo_pag': })

    @staticmethod
    def login(request):
        form = AuthenticationForm(request.POST or None)

        if form.is_valid():
            matricula = form.cleaned_data['matricula']
            password = form.cleaned_data['password']

            user = authenticate(matricula=matricula, password=password)
            login(request, user)
            return redirect('index_dashboard')
        else:
            return render(request, 'registration/login.html', {'form': form, 'titulo_pag': 'LOGIN'})

    @staticmethod
    def logout(request):
        logout(request)

        return redirect('login')