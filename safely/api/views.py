from django.db.models.query import QuerySet
from rest_framework import viewsets

from django.core.mail import EmailMessage
from django.conf import settings

from app.models import Alerta,Profesional
from django.db.models.signals import post_save
from django.dispatch import receiver


"""
TokenAuthentication:

    Autenticación simple basada en token.

    Los clientes deben autenticarse pasando la clave del token en la "Autorización"
    Encabezado HTTP, precedido de la cadena "Token". Por ejemplo:

        Autorización: Token 401f7ac837da42b97f613d789819ff93537bee6a
"""
from rest_framework.authentication import TokenAuthentication

"""
    IsAuthenticated:

    Permite el acceso solo a usuarios autenticados.
"""
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

#SERIALIZADORES
from api import serializers
from .serializers import AlertaSerializer
#MODELOS
from app import models

# LOGIN TOKEN
class UserLoginApiView(ObtainAuthToken):
    """Crea Tokens de autenticacion de usuario"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


# USER
class UserViewSet(viewsets.ModelViewSet):
    serializer_class= serializers.UserSerializer
    queryset = models.User.objects.all()
    authentication_classes = (TokenAuthentication,)
    #permission_classes = (IsAuthenticated,)


#Actividad
class ActividadViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ActividadSerializer
    queryset =  models.Actividad.objects.all()
    authentication_classes = (TokenAuthentication,)
    #permission_classes = (IsAuthenticated,)

#Administrador
class AdministradorViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.AdministradorSerializer
    queryset =  models.Administrador.objects.all()
    authentication_classes = (TokenAuthentication,)
    #permission_classes = (IsAuthenticated,)



#Alerta
class AlertaViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.AlertaSerializer
    queryset =  models.Alerta.objects.all()
    authentication_classes = (TokenAuthentication,)
    #permission_classes = (IsAuthenticated,)
    def create(self, request, *args, **kwargs):
        if request.method == 'POST':
            descrip = request.POST.get('descripcion')
            profe = request.POST.get('id_prof')

            profesional  = Profesional.objects.get(id_prof=profe)
            email = profesional.id_perfil.id_auth_user.email
            #print(profesional.id_perfil.id_auth_user.email)
            send_email(descrip,email)
        response = super(AlertaViewSet, self).create(request, *args, **kwargs)
        return response

#Envia correo al momento de crearse una alerta 
def send_email(descrip,email):
    email = EmailMessage(
        'Alerta Safely',
        descrip,
        settings.EMAIL_HOST_USER,
        [email],
    )
    #print(email)
    email.send()



#Asesoria
class AsesoriaViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.AsesoriaSerializer
    queryset =  models.Asesoria.objects.all()
    authentication_classes = (TokenAuthentication,)
    #permission_classes = (IsAuthenticated,)

#Boleta
class BoletaViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.BoletaSerializer
    queryset =  models.Boleta.objects.all()
    authentication_classes = (TokenAuthentication,)
    #permission_classes = (IsAuthenticated,)

#Capacitacion
class CapacitacionViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CapacitacionSerializer
    queryset =  models.Capacitacion.objects.all()
    authentication_classes = (TokenAuthentication,)
    #permission_classes = (IsAuthenticated,)

#Chat
class ChatViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ChatSerializer
    queryset =  models.Chat.objects.all()
    authentication_classes = (TokenAuthentication,)
    #permission_classes = (IsAuthenticated,)

#Cliente
class ClienteViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ClienteSerializer
    queryset =  models.Cliente.objects.all()
    authentication_classes = (TokenAuthentication,)
    #permission_classes = (IsAuthenticated,)

#Contrato
class ContratoViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ContratoSerializer
    queryset =  models.Contrato.objects.all()
    authentication_classes = (TokenAuthentication,)
    #permission_classes = (IsAuthenticated,)

#Lista
class ListaViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ListaSerializer
    queryset =  models.Lista.objects.all()
    authentication_classes = (TokenAuthentication,)
    #permission_classes = (IsAuthenticated,)

#Mejora
class MejoraViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.MejoraSerializer
    queryset =  models.Mejora.objects.all()
    authentication_classes = (TokenAuthentication,)
    #permission_classes = (IsAuthenticated,)

#Perfil
class PerfilViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.PerfilSerializer
    queryset =  models.Perfil.objects.all()
    authentication_classes = (TokenAuthentication,)
    #permission_classes = (IsAuthenticated,)

#Plan
class PlanViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.PlanSerializer
    queryset =  models.Plan.objects.all()
    authentication_classes = (TokenAuthentication,)
    #permission_classes = (IsAuthenticated,)

#Profesional
class ProfesionalViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ProfesionalSerializer
    queryset =  models.Profesional.objects.all()
    authentication_classes = (TokenAuthentication,)
    #permission_classes = (IsAuthenticated,)

#Reporte
class ReporteViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ReporteSerializer
    queryset =  models.Reporte.objects.all()
    authentication_classes = (TokenAuthentication,)
    #permission_classes = (IsAuthenticated,)

#Servicio
class ServicioViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ServicioSerializer
    queryset =  models.Servicio.objects.all()
    authentication_classes = (TokenAuthentication,)
    #permission_classes = (IsAuthenticated,)

#TipoAsesoria
class TipoAsesoriaViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.TipoAsesoriaSerializer
    queryset =  models.TipoAsesoria.objects.all()
    authentication_classes = (TokenAuthentication,)
    #permission_classes = (IsAuthenticated,)

#TipoReporte
class TipoReporteViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.TipoReporteSerializer
    queryset =  models.TipoReporte.objects.all()
    authentication_classes = (TokenAuthentication,)
    #permission_classes = (IsAuthenticated,)

#Visita
class VisitaViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.VisitaSerializer
    queryset =  models.Visita.objects.all()
    authentication_classes = (TokenAuthentication,)
    #permission_classes = (IsAuthenticated,)


