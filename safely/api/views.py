from django.db.models.query import QuerySet
from rest_framework import viewsets

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

#MODELOS
from app import models

# LOGIN TOKEN
class UserLoginApiView(ObtainAuthToken):
    """Crea Tokens de autenticacion de usuario"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES



class UserViewSet(viewsets.ModelViewSet):
    serializer_class= serializers.UserSerializer
    queryset = models.User.objects.all()
    authentication_classes = (TokenAuthentication,)
    #permission_classes = (IsAuthenticated,)



class ActividadViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ActividadSerializer
    queryset =  models.Actividad.objects.all()
    authentication_classes = (TokenAuthentication,)