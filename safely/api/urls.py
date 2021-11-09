from django.urls import path,include
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
MejoraLista,MejoraDetalles,MejoraCrear,MejoraModificar,MejoraEliminar,
UserLista,UserDetalles,UserCrear,UserModificar,UserEliminar,

PerfilLista,PerfilDetalles,PerfilCrear,PerfilModificar,PerfilEliminar,
ReporteLista,ReporteDetalles,ReporteCrear,ReporteModificar,ReporteEliminar,
ChatLista,ChatDetalles,ChatCrear,ChatModificar,ChatEliminar,

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

    path('lista/', views.ListaLista, name="ListaLista"),
    path('lista/detalles/<str:pk>/', views.ListaDetalles, name="ListaDetalles"),
    path('lista/crear', views.ListaCrear, name="ListaCrear"),
    path('lista/modificar/<str:pk>/', views.ListaModificar, name="ListaModificar"),
    path('lista/eliminar/<str:pk>/',views.ListaEliminar,name="ListaEliminar"),

    path('visita/', views.VisitaLista, name="VisitaLista"),
    path('visita/detalles/<str:pk>/', views.VisitaDetalles, name="VisitaDetalles"),
    path('visita/crear', views.VisitaCrear, name="VisitaCrear"),
    path('visita/modificar/<str:pk>/', views.VisitaModificar, name="VisitaModificar"),
    path('visita/eliminar/<str:pk>/',views.VisitaEliminar,name="VisitaEliminar"),

    path('alerta/', views.AlertaLista, name="AlertaLista"),
    path('alerta/detalles/<str:pk>/', views.AlertaDetalles, name="AlertaDetalles"),
    path('alerta/crear', views.AlertaCrear, name="AlertaCrear"),
    path('alerta/modificar/<str:pk>/', views.AlertaModificar, name="AlertaModificar"),
    path('alerta/eliminar/<str:pk>/',views.AlertaEliminar,name="AlertaEliminar"),

    path('mejora/', views.MejoraLista, name="MejoraLista"),
    path('mejora/detalles/<str:pk>/', views.MejoraDetalles, name="MejoraDetalles"),
    path('mejora/crear', views.MejoraCrear, name="MejoraCrear"),
    path('mejora/modificar/<str:pk>/', views.MejoraModificar, name="MejoraModificar"),
    path('mejora/eliminar/<str:pk>/',views.MejoraEliminar,name="MejoraEliminar"),

    path('user/', views.UserLista, name="UserLista"),
    path('user/detalles/<str:pk>/', views.UserDetalles, name="UserDetalles"),
    path('user/crear', views.UserCrear, name="UserCrear"),
    path('user/modificar/<str:pk>/', views.UserModificar, name="UserModificar"),
    path('user/eliminar/<str:pk>/',views.UserEliminar,name="UserEliminar"),

    path('perfil/', views.PerfilLista, name="PerfilLista"),
    path('perfil/detalles/<str:pk>/', views.PerfilDetalles, name="PerfilDetalles"),
    path('perfil/crear', views.PerfilCrear, name="PerfilCrear"),
    path('perfil/modificar/<str:pk>/', views.PerfilModificar, name="PerfilModificar"),
    path('perfil/eliminar/<str:pk>/',views.PerfilEliminar,name="PerfilEliminar"),

    path('reporte/', views.ReporteLista, name="ReporteLista"),
    path('reporte/detalles/<str:pk>/', views.ReporteDetalles, name="ReporteDetalles"),
    path('reporte/crear', views.ReporteCrear, name="ReporteCrear"),
    path('reporte/modificar/<str:pk>/', views.ReporteModificar, name="ReporteModificar"),
    path('reporte/eliminar/<str:pk>/',views.ReporteEliminar,name="ReporteEliminar"),

    path('chat/', views.ChatLista, name="ChatLista"),
    path('chat/detalles/<str:pk>/', views.ChatDetalles, name="ChatDetalles"),
    path('chat/crear', views.ChatCrear, name="ChatCrear"),
    path('chat/modificar/<str:pk>/', views.ChatModificar, name="ChatModificar"),
    path('chat/eliminar/<str:pk>/',views.ChatEliminar,name="ChatEliminar"),
]

