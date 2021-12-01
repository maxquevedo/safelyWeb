from django.contrib import admin
from django.urls import path, include
from cliente.views import *

urlpatterns = [
    path('cliente/', home_cliente.as_view(), name="home-cliente"),
    path('cliente/actividades/', actividades, name="actividades-cliente"),
    path('cliente/boleta/', boleta, name="boleta-cliente"),
    path('cliente/lista/', lista, name="lista-cliente"),
    path('cliente/perfil/', datosUser, name="perfil-cliente"),

]