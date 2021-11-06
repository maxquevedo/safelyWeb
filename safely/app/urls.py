from django.contrib import admin
from django.urls import path, include

from .views import (maintainer_plan, maintainer_service, maintainer_user, signup_view, home,
home_admin, maintainer, login_view,
UserLista, UserEdit, UserDelete, login_filter, plan_lista,
PlanEdit, PlanDelete, PlanCreate,ServicioCreate,Servicio_lista,ServicioEdit,ServicioDelete,
infoCliente,crear_cliente,infoProfesional,modificar_cliente,crear_profesional,modificar_profesional
)

urlpatterns = [
    path('', home, name="home"),
    path('admin/', admin.site.urls),
    path('administrador/usuario/registro-usuario/', signup_view, name='signup'),
    path('administrador/', home_admin, name='home-adm'),
    path('administrador/mantenedor/', maintainer, name='mantenedor'),
    path('administrador/mantenedor-usuario/', maintainer_user, name='mantenedor-usr'),
    path('administrador/mantenedor-plan/', maintainer_plan, name='mantenedor-plan'),
    path('administrador/mantenedor-servicio/', maintainer_service, name='mantenedor-servicio'),
    path('administrador/mantenedor-cliente/', infoCliente, name='infoCliente'),
    path('administrador/mantenedor-cliente/crear', crear_cliente, name='crear_cliente'),
    path('administrador/mantenedor-cliente/modificar/<int:id_cli>/', modificar_cliente, name='modificar_cliente'),
    path('administrador/mantenedor-profesional/', infoProfesional, name='infoProfesional'),
    path('administrador/mantenedor-profesional/crear', crear_profesional, name='crear_profesional'),
    path('administrador/mantenedor-profesional/modificar/<int:id_prof>/', modificar_profesional, name='modificar_profesional'),

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
    path('administrador/servicios/eliminar-servicio/<int:id>/', ServicioDelete, name='eliminar-servicio')
]