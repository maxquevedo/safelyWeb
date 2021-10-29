from django.urls import path
from .views import (ActividadLista,ActividadDetalles,ActividadCrear,ActividadModificar,ActividadEliminar,
CapacitacionLista,CapacitacionDetalles,CapacitacionCrear,CapacitacionModificar,CapacitacionEliminar,
ClienteLista,ClienteDetalles,
ProfesionalLista,ProfesionalDetalles,
AsesoriaLista,AsesoriaDetalles,AsesoriaCrear,AsesoriaModificar,AsesoriaEliminar,
TipoAsesoriaLista,TipoAsesoriaDetalles,TipoAsesoriaCrear,TipoAsesoriaModificar,TipoAsesoriaEliminar

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
]