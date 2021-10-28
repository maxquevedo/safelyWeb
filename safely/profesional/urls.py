from django.contrib import admin
from django.urls import path, include
from profesional.views import *

urlpatterns = [
    path('profesional/', home_professional, name='home-prof'),
    path('profesional/datos/', datos_pro, name='datos-prof'),

    path('profesional/asesoria/', vista_asesorias, name='vista_asesorias'),
    path('profesional/asesoria/crear', crear_ase, name='crear_ase'),
    path('profesional/asesoria/crear-tipo', crear_tipo_ase, name='crear_tipo_ase'),
    path('profesional/asesoria/ingresar', ingresar_ase, name='ingresar_ase'),
    path('profesional/asesoria/modificar', modificar_ase, name='modificar_ase'),
    path('profesional/asesoria/lista', lista_ase, name='lista_ase'),

    path('profesional/capacitaciones/', vista_capacitacion, name='vista_capacitacion'),
    path('profesional/capacitaciones/crear', crear_capa, name='crear_capa'),
    path('profesional/capacitaciones/ingresar', ingresar_capa, name='ingresar_capa'),
    path('profesional/capacitaciones/modificar', modificar_capa, name='modificar_capa'),

    path('profesional/checklist/', vista_checklist, name='vista_checklist'),
    path('profesional/checklist/crear', crear_ch, name='crear_ch'),
    path('profesional/checklist/ingresar', ingresar_ch, name='ingresar_ch'),
    path('profesional/checklist/modificar', modificar_ch, name='modificar_ch'),

    path('profesional/mejoras/', vista_mejoras, name='vista_mejoras'),
    path('profesional/mejoras/crear', revisar_me, name='revisar_me'),
    path('profesional/mejoras/ingresar', ingresar_me, name='ingresar_me'),

]