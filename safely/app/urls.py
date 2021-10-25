from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .viewsets import (
RolViewset,UsuarioViewset,PerfilViewset,
AdministradorViewset,ProfesionalViewset,ClienteViewset,
ServicioViewset,PlanlViewset,ContratoViewset,
AlertaViewset, ListaViewset, PacViewset,
MejorasViewset, ReporteViewset, TipoReporteViewset,
ActividadViewset, CapacitacionViewset, AsesoriaViewset,
VisitaViewset, UserViewset
)

router = routers.DefaultRouter()
router.register('rol',RolViewset)
router.register('usuario',UsuarioViewset)
router.register('perfil',PerfilViewset)
router.register('administrador',AdministradorViewset)
router.register('profesional',ProfesionalViewset)
router.register('cliente',ClienteViewset)
router.register('servicio',ServicioViewset)
router.register('plan',PlanlViewset)
router.register('contrato',ContratoViewset)
router.register('alerta',AlertaViewset)
router.register('lista',ListaViewset)
router.register('pac',PacViewset)
router.register('listamejoras',MejorasViewset)
router.register('reporte',ReporteViewset)
router.register('tiporeporte',TipoReporteViewset)
router.register('actividad',ActividadViewset)
router.register('capacitacion',CapacitacionViewset)
router.register('asesoria',AsesoriaViewset)
router.register('visita',VisitaViewset)
router.register('user',UserViewset)

from .views import (main, signup_view, home, home_professional, 
home_admin, maintainer, login_view,
UserLista, UserEdit, UserDelete, login_filter, plan_lista,
PlanEdit, PlanDelete, PlanCreate,ServicioCreate,Servicio_lista,ServicioEdit,ServicioDelete,planes,test,mod_plan)

urlpatterns = [
    path('main/', main, name="main"),
    path('', home, name="home"),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
    path('administrador/usuario/registro-usuario/', signup_view, name='signup'),
    path('profesional/', home_professional, name='home-prof'),
    path('administrador/', home_admin, name='home-adm'),
    path('administrador/mantenedor/', maintainer, name='mantenedor'),
    path('login/', login_view, name='login'),
    path('administrador/usuario/lista-usuarios/', UserLista, name='listar'),
    path('administrador/usuario/editar/<int:id>/' ,UserEdit, name='editar'),
    path('eliminar/<int:id>/' ,UserDelete, name='eliminar'),
    path('login-filter', login_filter, name='login-filter'),

    path('administrador/plan/agregar-plan/', PlanCreate, name='agregar-plan'),
    path('administrador/plan/planlista-planes/', plan_lista, name='lista-plan'),
    path('administrador/plan/planeditar-plan/<int:id_plan>/', PlanEdit, name='editar-plan'),
    path('administrador/plan/eliminar-plan/<int:id>/', PlanDelete, name='eliminar-plan'),

    path('administrador/servicios/agregar-servicio/', ServicioCreate, name='agregar-servicio'),
    path('administrador/servicios/lista-servicios/', Servicio_lista, name='lista-servicios'),
    path('administrador/servicios/editar-servicio/<int:id_servicio>/', ServicioEdit, name='editar-servicio'),
    path('administrador/servicios/eliminar-servicio/<int:id>/', ServicioDelete, name='eliminar-servicio'),

    path('administrador/plan/listarplanes/', planes, name='listarplanes'),
    path('administrador/plan/test/', test, name='test'),
    path('administrador/plan/modplan/', mod_plan, name='mod_plan')
]