from django.db.models import fields
from app.models import (Actividad,Administrador,Alerta,Asesoria,Capacitacion,Cliente,Contrato,Lista,
Mejoras,Pac,Perfil,Plan,Profesional,Reporte,Servicio,TipoAsesoria,TipoReporte,User,Visita
)
from rest_framework import serializers
from django.contrib.auth.models import User
# SECCION USUARIO

class ActividadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actividad
        fields = '__all__'

class AdministradorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Administrador
        fields = '__all__'

class AlertaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alerta
        fields = '__all__'

class AsesoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asesoria
        fields = '__all__'

class CapacitacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Capacitacion
        fields = '__all__'

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

class ContratoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contrato
        fields = '__all__'

class ListaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lista
        fields = '__all__'

class MejorasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mejoras
        fields = '__all__'

class PacSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pac
        fields = '__all__'

class PerfilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Perfil
        fields = '__all__'

class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = '__all__'

class ProfesionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profesional
        fields = '__all__'

class ReporteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reporte
        fields = '__all__'

class ServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servicio
        fields = '__all__'

class TipoAsesoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoAsesoria
        fields = '__all__'

class TipoReporteSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoReporte
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class VisitaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visita
        fields = '__all__'

