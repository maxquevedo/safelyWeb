from django.contrib import admin
from django.urls import path, include
from cliente import views

urlpatterns = [
    path('cliente/', views.home_cliente, name="home-cliente"),
    path('cliente/accidentes/', views.accidentes, name="accidentes-cliente"),
    path('cliente/actividades/', views.actividades, name="actividades-cliente"),
    path('cliente/boleta/', views.boleta, name="boleta-cliente"),
    path('cliente/contrato/', views.contrato, name="contrato-cliente"),
    path('cliente/lista/', views.lista, name="lista-cliente"),
    path('cliente/perfil/', views.perfil, name="perfil-cliente"),


]