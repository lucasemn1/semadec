from django.urls import path
from .views import SessaoView

urlpatterns = [
    # path('login/', SessaoView.login, name='login_user'),
    path('logout/', SessaoView.logout, name='logout_user'),
    path('usuario/create', SessaoView.singup, name='usuario_create')
]
