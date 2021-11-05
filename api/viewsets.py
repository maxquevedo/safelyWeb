from .serializers import (PerfilSerializer,
AdministradorSerializer,ProfesionalSerializer,ClienteSerializer,
ServicioSerializer,PlanSerializer,ContratoSerializer,
AlertaSerializer,
ListaSerializer,
PacSerializer,MejorasSerializer,
ReporteSerializer,TipoReporteSerializer,
ActividadSerializer,CapacitacionSerializer,
AsesoriaSerializer,VisitaSerializer, UserSerializer,
ClienteContratoSerializer
    
)
from django.contrib.auth.models import User
from rest_framework import viewsets
from app.models import *

class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer

# SECCION USUARIO

class PerfilViewset(viewsets.ModelViewSet):
    queryset = Perfil.objects.all()
    serializer_class = PerfilSerializer

class AdministradorViewset(viewsets.ModelViewSet):
    queryset = Administrador.objects.all()
    serializer_class = AdministradorSerializer

class ProfesionalViewset(viewsets.ModelViewSet):
    queryset = Profesional.objects.all()
    serializer_class = ProfesionalSerializer

class ClienteViewset(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class ClienteContratoViewset(viewsets.ModelViewSet):
    queryset = ClienteContrato.objects.all()
    serializer_class = ClienteContratoSerializer

#########################################################################
# SECCION CONTRATO
class ServicioViewset(viewsets.ModelViewSet):
    queryset = Servicio.objects.all()
    serializer_class = ServicioSerializer

class PlanlViewset(viewsets.ModelViewSet):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer

class ContratoViewset(viewsets.ModelViewSet):
    queryset = Contrato.objects.all()
    serializer_class = ContratoSerializer

#########################################################################
# SECCION ALERTA
class AlertaViewset(viewsets.ModelViewSet):
    queryset = Alerta.objects.all()
    serializer_class = AlertaSerializer
#########################################################################
#SECCION LISTA
class ListaViewset(viewsets.ModelViewSet):
    queryset = Lista.objects.all()
    serializer_class = ListaSerializer
#########################################################################
#SECCION PAC/MEJORAS
class PacViewset(viewsets.ModelViewSet):
    queryset = Pac.objects.all()
    serializer_class = PacSerializer

class MejorasViewset(viewsets.ModelViewSet):
    queryset = Mejoras.objects.all()
    serializer_class = MejorasSerializer
#########################################################################
#SECCION REPORTE
class ReporteViewset(viewsets.ModelViewSet):
    queryset = Reporte.objects.all()
    serializer_class = ReporteSerializer

class TipoReporteViewset(viewsets.ModelViewSet):
    queryset = TipoReporte.objects.all()
    serializer_class = TipoReporteSerializer
#########################################################################
#SECCION ACTIVIDAD
class ActividadViewset(viewsets.ModelViewSet):
    queryset = Actividad.objects.all()
    serializer_class = ActividadSerializer

class CapacitacionViewset(viewsets.ModelViewSet):
    queryset = Capacitacion.objects.all()
    serializer_class = CapacitacionSerializer

class AsesoriaViewset(viewsets.ModelViewSet):
    queryset = Asesoria.objects.all()
    serializer_class = AsesoriaSerializer

class VisitaViewset(viewsets.ModelViewSet):
    queryset = Visita.objects.all()
    serializer_class = VisitaSerializer
