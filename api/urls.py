from django.urls import path
from .views import (ActividadLista,ActividadDetalles,ActividadCrear,ActividadModificar,ActividadEliminar,
CapacitacionLista,CapacitacionDetalles,CapacitacionCrear,CapacitacionModificar,CapacitacionEliminar,
ClienteLista,ClienteDetalles,
ProfesionalLista,ProfesionalDetalles,
AsesoriaLista,AsesoriaDetalles,AsesoriaCrear,AsesoriaModificar,AsesoriaEliminar,
TipoAsesoriaLista,TipoAsesoriaDetalles,TipoAsesoriaCrear,TipoAsesoriaModificar,TipoAsesoriaEliminar,
ContratoLista,ContratoDetalles,
ListaLista,ListaDetalles,ListaCrear,ListaModificar,ListaEliminar,
VisitaLista,VisitaDetalles,VisitaCrear,VisitaModificar,VisitaEliminar,
AlertaLista,AlertaDetalles,AlertaCrear,AlertaModificar,AlertaEliminar,
MejorasLista,MejorasDetalles,MejorasCrear,MejorasModificar,MejorasEliminar,
PacLista,PacDetalles,PacCrear,PacModificar,PacEliminar,
UserLista,UserDetalles,UserCrear,UserModificar,UserEliminar

)

from . import views
urlpatterns = [
    path('actividad/', views.ActividadLista, name="ActividadLista"),
    path('actividad/detalles/<str:pk>/', views.ActividadDetalles, name="ActividadDetalles"),
    path('actividad/crear', views.ActividadCrear, name="ActividadCrear"),
    path('actividad/modificar/<str:pk>/', views.ActividadModificar, name="ActividadModificar"),
    path('actividad/eliminar/<str:pk>/',views.ActividadEliminar,name="ActividadEliminar"),

    path('capacitacion/', views.CapacitacionLista, name="CapacitacionLista"),
    path('capacitacion/detalles/<str:pk>/', views.CapacitacionDetalles, name="CapacitacionDetalles"),
    path('capacitacion/crear', views.CapacitacionCrear, name="CapacitacionCrear"),
    path('capacitacion/modificar/<str:pk>/', views.CapacitacionModificar, name="CapacitacionModificar"),
    path('capacitacion/eliminar/<str:pk>/',views.CapacitacionEliminar,name="CapacitacionEliminar"),

    path('cliente/', views.ClienteLista, name="ClienteLista"),
    path('cliente/detalles/<str:pk>/', views.ClienteDetalles, name="ClienteDetalles"),

    path('Contrato/', views.ContratoLista, name="ContratoLista"),
    path('Contrato/detalles/<str:pk>/', views.ContratoDetalles, name="ContratoDetalles"),


    path('profesional/', views.ProfesionalLista, name="ProfesionalLista"),
    path('profesional/detalles/<str:pk>/', views.ProfesionalDetalles, name="ProfesionalDetalles"),

    path('asesoria/', views.AsesoriaLista, name="AsesoriaLista"),
    path('asesoria/detalles/<str:pk>/', views.AsesoriaDetalles, name="AsesoriaDetalles"),
    path('asesoria/crear', views.AsesoriaCrear, name="AsesoriaCrear"),
    path('asesoria/modificar/<str:pk>/', views.AsesoriaModificar, name="AsesoriaModificar"),
    path('asesoria/eliminar/<str:pk>/',views.AsesoriaEliminar,name="AsesoriaEliminar"),

    path('tipoasesoria/', views.TipoAsesoriaLista, name="TipoAsesoriaLista"),
    path('tipoasesoria/detalles/<str:pk>/', views.TipoAsesoriaDetalles, name="TipoAsesoriaDetalles"),
    path('tipoasesoria/crear', views.TipoAsesoriaCrear, name="TipoAsesoriaCrear"),
    path('tipoasesoria/modificar/<str:pk>/', views.TipoAsesoriaModificar, name="TipoAsesoriaModificar"),
    path('tipoasesoria/eliminar/<str:pk>/',views.TipoAsesoriaEliminar,name="TipoAsesoriaEliminar"),

    path('Lista/', views.ListaLista, name="ListaLista"),
    path('Lista/detalles/<str:pk>/', views.ListaDetalles, name="ListaDetalles"),
    path('Lista/crear', views.ListaCrear, name="ListaCrear"),
    path('Lista/modificar/<str:pk>/', views.ListaModificar, name="ListaModificar"),
    path('Lista/eliminar/<str:pk>/',views.ListaEliminar,name="ListaEliminar"),

    path('Visita/', views.VisitaLista, name="VisitaLista"),
    path('Visita/detalles/<str:pk>/', views.VisitaDetalles, name="VisitaDetalles"),
    path('Visita/crear', views.VisitaCrear, name="VisitaCrear"),
    path('Visita/modificar/<str:pk>/', views.VisitaModificar, name="VisitaModificar"),
    path('Visita/eliminar/<str:pk>/',views.VisitaEliminar,name="VisitaEliminar"),

    path('Alerta/', views.AlertaLista, name="AlertaLista"),
    path('Alerta/detalles/<str:pk>/', views.AlertaDetalles, name="AlertaDetalles"),
    path('Alerta/crear', views.AlertaCrear, name="AlertaCrear"),
    path('Alerta/modificar/<str:pk>/', views.AlertaModificar, name="AlertaModificar"),
    path('Alerta/eliminar/<str:pk>/',views.AlertaEliminar,name="AlertaEliminar"),

    path('Mejoras/', views.MejorasLista, name="MejorasLista"),
    path('Mejoras/detalles/<str:pk>/', views.MejorasDetalles, name="MejorasDetalles"),
    path('Mejoras/crear', views.MejorasCrear, name="MejorasCrear"),
    path('Mejoras/modificar/<str:pk>/', views.MejorasModificar, name="MejorasModificar"),
    path('Mejoras/eliminar/<str:pk>/',views.MejorasEliminar,name="MejorasEliminar"),

    path('Pac/', views.PacLista, name="PacLista"),
    path('Pac/detalles/<str:pk>/', views.PacDetalles, name="PacDetalles"),
    path('Pac/crear', views.PacCrear, name="PacCrear"),
    path('Pac/modificar/<str:pk>/', views.PacModificar, name="PacModificar"),
    path('Pac/eliminar/<str:pk>/',views.PacEliminar,name="PacEliminar"),

    path('User/', views.UserLista, name="UserLista"),
    path('User/detalles/<str:pk>/', views.UserDetalles, name="UserDetalles"),
    path('User/crear', views.UserCrear, name="UserCrear"),
    path('User/modificar/<str:pk>/', views.UserModificar, name="UserModificar"),
    path('User/eliminar/<str:pk>/',views.UserEliminar,name="UserEliminar"),
]