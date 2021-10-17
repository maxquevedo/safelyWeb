from django.db.models import fields
from .models import (
Rol, Usuario, Perfil, Administrador, Profesional, Cliente,
Servicio, Plan, Contrato, 
Alerta,
Lista,
Pac,Mejoras,
Reporte,TipoReporte,
Actividad, Capacitacion,Asesoria,TipoAsesoria,Visita, User
)
from rest_framework import serializers

# SECCION USUARIO

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = '__all__'

class UsuarioSerializer(serializers.ModelSerializer):
    #nombre_rol = serializers.CharField(read_only=True,source="id_rol.nombre")
    id_rol = RolSerializer(read_only=True) # este campo solo es de lectura 
    rol = serializers.PrimaryKeyRelatedField(queryset=Rol.objects.all().order_by('id_rol'),source="id_rol")
    class Meta:
        model = Usuario
        fields = '__all__'

class PerfilSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Perfil
        fields = '__all__'

class AdministradorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Administrador
        fields = '__all__'

class ProfesionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profesional
        fields = '__all__'

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

#########################################################################
# SECCION CONTRATO
class ServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servicio
        fields = '__all__'

class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = '__all__'

class ContratoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contrato
        fields = '__all__'

#########################################################################
# SECCION ALERTA
class AlertaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alerta
        fields = '__all__'

#########################################################################
#SECCION LISTA
class ListaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lista
        fields = '__all__'
#########################################################################
#SECCION PAC/MEJORAS
class PacSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pac
        fields = '__all__'

class MejorasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mejoras
        fields = '__all__'
#########################################################################
#SECCION REPORTE
class ReporteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reporte
        fields = '__all__'

class TipoReporteSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoReporte
        fields = '__all__'
#########################################################################
#SECCION ACTIVIDAD
class ActividadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actividad
        fields = '__all__'

class CapacitacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Capacitacion
        fields = '__all__'

class AsesoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asesoria
        fields = '__all__'

class TipoAsesoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoAsesoria
        fields = '__all__'


class VisitaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visita
        fields = '__all__'

