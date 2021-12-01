from django.contrib import admin
from django.urls import path, include
from profesional.views import *

urlpatterns = [
    path('profesional/', home_professional.as_view(), name='home-prof'),
    path('profesional/datos/', datos_pro, name='datos-prof'),

    path('profesional/asesoria/', lista_ase, name='lista_ase'),
    path('profesional/asesoria/crear', crear_ase, name='crear_ase'),
    path('profesional/asesoria/crear-tipo', crear_tipo_ase, name='crear_tipo_ase'),
    path('profesional/asesoria/ingresar', ingresar_ase, name='ingresar_ase'),
    path('profesional/asesoria/modificar/<int:id_asesoria>/', modificar_ase, name='modificar_ase'),

    path('profesional/capacitaciones/', lista_capa, name='lista_capa'),
    path('profesional/capacitaciones/crear', crear_capa, name='crear_capa'),
    path('profesional/capacitaciones/ingresar', ingresar_capa, name='ingresar_capa'),
    path('profesional/capacitaciones/modificar/<int:id_capacitacion>/', modificar_capa, name='modificar_capa'),

    path('profesional/checklist/', lista_ch, name='lista_ch'),
    path('profesional/checklist/crear', crear_ch, name='crear_ch'),
    path('profesional/checklist/ingresar', ingresar_ch, name='ingresar_ch'),
    path('profesional/checklist/modificar/<int:id_lista>/', modificar_ch, name='modificar_ch'),

    path('profesional/mejoras/', vista_mejoras, name='vista_mejoras'),
    path('profesional/mejoras/crear', crear_me, name='crear_me'),
    path('profesional/mejoras/ingresar', crear_me, name='crear_me'),

    path('profesional/actividad/', vista_actividad, name='vista_actividad'),
    path('profesional/actividad/modificar/<int:id_actividad>/', modificar_actividad, name='modificar_actividad'),
    path('profesional/actividad/estado/<int:id_actividad>/', estado_actividad, name='estado_actividad'),

    path('profesional/visita/', vista_visita, name='vista_visita'),
    path('profesional/visita/crear', crear_visita, name='crear_visita'),
    path('profesional/visita/modificar/<int:id_visita>/', modificar_visita, name='modificar_visita'),
    path('profesional/visita/ingresar/', ingresar_visita, name='ingresar_visita'),
    path('profesional/cliente/asignado/', cliente_asignado, name='cliente_asignado'),

]