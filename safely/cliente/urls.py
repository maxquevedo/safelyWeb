from django.contrib import admin
from django.urls import path, include
from cliente import views

urlpatterns = [
    path('cliente/', views.home_cliente, name="home-cliente"),
    path('cliente/actividades/', views.actividades, name="actividades-cliente"),
    path('cliente/boleta/', views.boleta, name="boleta-cliente"),
    path('cliente/lista/', views.lista, name="lista-cliente"),
    path('cliente/perfil/', views.datosUser, name="perfil-cliente"),

]