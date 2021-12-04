from django.urls import path,include
from rest_framework import routers
from rest_framework.routers import DefaultRouter
from api import views



router= DefaultRouter()
router.register('user', views.UserViewSet, basename='user')
router.register('activiad',views.ActividadViewSet)
router.register('administrador',views.AdministradorViewSet)
router.register('alerta',views.AlertaViewSet)
router.register('asesoria',views.AsesoriaViewSet)
router.register('boleta',views.BoletaViewSet)
router.register('capacitacion',views.CapacitacionViewSet)
router.register('cliente',views.ClienteViewSet)
router.register('contrato',views.ContratoViewSet)
router.register('mejora',views.MejoraViewSet)
router.register('perfil',views.PerfilViewSet)
router.register('plan',views.PlanViewSet)
router.register('profesional',views.ProfesionalViewSet)
router.register('reporte',views.ReporteViewSet)
router.register('servicio',views.ServicioViewSet)
router.register('tipoasesoria',views.TipoAsesoriaViewSet)
router.register('tiporeporte',views.TipoReporteViewSet)
router.register('visita',views.VisitaViewSet)
router.register('checklist',views.ChecklistViewSet)
router.register('checkact',views.ActCheckViewSet)


urlpatterns = [
    path('api/', include(router.urls)),
    path('inicio/', views.UserLoginApiView.as_view()),

]


