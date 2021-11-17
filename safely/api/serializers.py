from django.db import models
from rest_framework import fields, serializers
from django.contrib.auth.models import User

# Import Modelos
from app import models

"""
    ModelSerializer:

    Un `ModelSerializer` es solo un` Serializer` normal, excepto que:

    * Un conjunto de campos predeterminados se completa automáticamente.
    * Un conjunto de validadores predeterminados se completa automáticamente.
    * Se proporcionan implementaciones predeterminadas `.create ()` y `.update ()`.

    El proceso de determinar automáticamente un conjunto de campos de serializador.
    basado en los campos del modelo es razonablemente complejo, pero es casi seguro que
    no es necesario profundizar en la implementación.

    Si la clase `ModelSerializer` * no * genera el conjunto de campos que
    necesita, debe declarar los campos adicionales / diferentes explícitamente en
    la clase serializador, o simplemente use una clase `Serializador`.
"""

# User Model
class UserSerializer(serializers.ModelSerializer):
    """ Serializa objeto de User"""
    class Meta:
        model = models.User
        #fields = ('id', 'username','password')
        fields = '__all__'
        extra_kwargs = {
            'password':{
                'write_only':True,
                'style': {'input_type':'password'}
            }
        }
        
#Model actividad
class ActividadSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Actividad
        fields = '__all__'

#Model Administrador
class AdministradorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Administrador
        fields = '__all__'

#Model Alerta
class AlertaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Alerta
        fields = '__all__'

#Model Asesoria
class AsesoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Asesoria
        fields = '__all__'

#Model Boleta
class BoletaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Boleta
        fields = '__all__'

#Model Capacitacion
class CapacitacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Capacitacion
        fields = '__all__'


#Model Chat
class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Chat
        fields = '__all__'

#Model Cliente
class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Cliente
        fields = '__all__'

#Model Contrato
class ContratoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Contrato
        fields = '__all__'


#Model Lista
class ListaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Lista
        fields = '__all__'

#Model Mejora
class MejoraSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Mejora
        fields = '__all__'

#Model Perfil
class PerfilSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Perfil
        fields = '__all__'

#Model Plan
class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Plan
        fields = '__all__'


#Model Profesional
class ProfesionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Profesional
        fields = '__all__'


#Model Reporte
class ReporteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Reporte
        fields = '__all__'


#Model Servicio
class ServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Servicio
        fields = '__all__'


#Model TipoAsesoria
class TipoAsesoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TipoAsesoria
        fields = '__all__'

#Model TipoReporte
class TipoReporteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TipoReporte
        fields = '__all__'

#Model Visita
class VisitaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Visita
        fields = '__all__'

