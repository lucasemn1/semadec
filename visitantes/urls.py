from django.urls import path, include
from .views import Visitante


urlpatterns = [
    path('', Visitante.index, name='visitante_index'),
]