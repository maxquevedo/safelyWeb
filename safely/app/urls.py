from django.contrib import admin
from django.urls import path
from app import views
from app import contrato
from app import boleta
from app import correo
from .reporte import ReporteClienteListView,ReporteHome,ReporteGlobal,ReporteCliente_render_pdf_view,ReporteGlobal_pdf_view

urlpatterns = [
    path('filtro/',views.user_filter,name="user_filter"),
    path('', views.home, name="home"),
    path('admin/', admin.site.urls),
    path('administrador/usuario/registro-usuario/', views.signup_view, name='signup'),
    path('administrador/', views.home_admin, name='home-adm'),
    path('administrador/crear-grupo/', views.crear_grupo, name='crear-grupo'),
    path('administrador/mantenedor/', views.maintainer, name='mantenedor'),
    path('administrador/mantenedor-usuario/', views.maintainer_user, name='mantenedor-usr'),
    path('administrador/mantenedor-plan/', views.maintainer_plan, name='mantenedor-plan'),
    path('administrador/mantenedor-servicio/', views.maintainer_service, name='mantenedor-servicio'),
    path('administrador/mantenedor-cliente/', views.infoCliente, name='infoCliente'),
    path('administrador/mantenedor-cliente/crear', views.crear_cliente, name='crear_cliente'),
    path('administrador/mantenedor-cliente/modificar/<int:id_cli>/', views.modificar_cliente, name='modificar_cliente'),
    path('administrador/mantenedor-profesional/', views.infoProfesional, name='infoProfesional'),
    path('administrador/mantenedor-profesional/crear', views.crear_profesional, name='crear_profesional'),
    path('administrador/mantenedor-profesional/modificar/<int:id_prof>/', views.modificar_profesional, name='modificar_profesional'),

    path('administrador/mantenedor-perfil/', views.infoPerfil, name='infoPerfil'),
    path('administrador/mantenedor-perfil/crear', views.crear_perfil, name='crear_perfil'),
    path('administrador/mantenedor-perfil/modificar/<int:id_perfil>/', views.modificar_perfil, name='modificar_perfil'),

    path('administrador/actividades/lista/', views.actividades, name='actividades'),
    path('administrador/actividades/crear/', views.crear_actividad, name='crear-activ'),
    path('administrador/actividades/actualizar/<int:id_actividad>/', views.actualizar_actividad, name='actualizar_actividad'),
    
    path('login/', views.login_view, name='login'),
    path('administrador/usuario/lista-usuarios/', views.UserLista, name='listar'),
    path('administrador/usuario/editar/<int:id>/' ,views.UserEdit, name='editar'),
    path('desactivar/<int:id>/' ,views.UserDelete, name='eliminar'),
    path('activar/<int:id>/' ,views.UserActivate, name='activar'),
    path('login-filter', views.login_filter, name='login-filter'),

    path('administrador/plan/agregar-plan/', views.PlanCreate, name='agregar-plan'),
    path('administrador/plan/planlista-planes/',views. plan_lista, name='lista-plan'),
    path('administrador/plan/planeditar-plan/<int:id_plan>/', views.PlanEdit, name='editar-plan'),
    path('administrador/plan/desactivar-plan/<int:id>/', views.PlanDelete, name='desactivar-plan'),
    path('administrador/plan/activar-plan/<int:id>/', views.PlanActivate, name='activar-plan'),

    path('administrador/servicios/agregar-servicio/', views.ServicioCreate, name='agregar-servicio'),
    path('administrador/servicios/lista-servicios/', views.Servicio_lista, name='lista-servicios'),
    path('administrador/servicios/editar-servicio/<int:id_servicio>/', views.ServicioEdit, name='editar-servicio'),
    path('administrador/servicios/desactivar-servicio/<int:id>/', views.ServicioDelete, name='desactivar-servicio'),
    path('administrador/servicios/activar-servicio/<int:id>/', views.ServicioActivate, name='activar-servicio'),

    path('administrador/contrato/crear',contrato.contratoCliente, name='contratoCliente'),
    path('administrador/contrato/lista',contrato.listaContrato, name='listaContrato'),
    path('administrador/contrato/editar/<int:id_contrato>/',contrato.editarContrato, name='editarContrato'),

    path('administrador/boleta/crear/',boleta.creaBoleta, name='creaBoleta'),
    path('administrador/boleta/lista/',boleta.listaBoletas, name='listaBoletas'),
    path('administrador/boleta/editar/<int:id_boleta>/',boleta.editarBoleta, name='editarBoleta'),

    path('administrador/correo/',correo.correo, name='correo'),
    path('administrador/correo/test/<int:id_boleta>/',boleta.datosBoleta, name='datosBoleta'),

    path('administrador/reportes/home',ReporteHome.as_view(),name='reporte-lista'),
    path('administrador/reportes/reporte-cliente-Home',ReporteClienteListView.as_view(),name='reporte-cliente-home'),
    path('administrador/reportes/reporte-global-home',ReporteGlobal,name='reporte-global-home'),
    path('administrador/reportes/reporte-cliente/<id_cli>',ReporteCliente_render_pdf_view,name='reporteCliente'),
    path('administrador/reportes/reporte-global/<mes>',ReporteGlobal_pdf_view,name='reporteGlobal'),
]

