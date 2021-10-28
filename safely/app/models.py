# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import User


class Actividad(models.Model):
    MY_CHOICES = (
        ('1', 'ASESORIA'),
        ('2', 'CAPACITACIÓN'),
        ('3', 'VISITA'),
    )
    id_actividad = models.BigIntegerField(primary_key=True)
    nombre = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=250)
    tipo_actividad = models.CharField(max_length=1,choices=MY_CHOICES)
    capacitacion_id_capacitacion = models.ForeignKey('Capacitacion', models.DO_NOTHING, db_column='capacitacion_id_capacitacion', blank=True, null=True)
    asesoria_id_asesoria = models.ForeignKey('Asesoria', models.DO_NOTHING, db_column='asesoria_id_asesoria', blank=True, null=True)
    visita_id_visita = models.ForeignKey('Visita', models.DO_NOTHING, db_column='visita_id_visita', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'actividad'
        
    def __str__(self):
        return self.nombre

class Administrador(models.Model):
    id_admin = models.BigIntegerField(primary_key=True)
    perfil_id_perfil = models.ForeignKey('Perfil', models.DO_NOTHING, db_column='perfil_id_perfil')

    class Meta:
        managed = False
        db_table = 'administrador'


class Alerta(models.Model):
    id_alerta = models.BigIntegerField(primary_key=True)
    fec_aviso = models.DateField()
    cliente_id_cli = models.ForeignKey('Cliente', models.DO_NOTHING, db_column='cliente_id_cli')
    profesional_id_prof = models.ForeignKey('Profesional', models.DO_NOTHING, db_column='profesional_id_prof')

    class Meta:
        managed = False
        db_table = 'alerta'


class Asesoria(models.Model):
    id_asesoria = models.BigIntegerField(primary_key=True)
    descripcion = models.CharField(max_length=250)
    tipo_asesoria_id_tipo_ase = models.ForeignKey('TipoAsesoria', models.DO_NOTHING, db_column='tipo_asesoria_id_tipo_ase')

    class Meta:
        managed = False
        db_table = 'asesoria'


class Capacitacion(models.Model):
    id_capacitacion = models.BigIntegerField(primary_key=True)
    cant_asistentes = models.CharField(max_length=2)
    materiales = models.CharField(max_length=250)

    class Meta:
        managed = False
        db_table = 'capacitacion'


class Cliente(models.Model):
    id_cli = models.BigIntegerField(primary_key=True)
    razon_social = models.CharField(max_length=50)
    perfil_id_perfil = models.ForeignKey('Perfil', models.DO_NOTHING, db_column='perfil_id_perfil')

    class Meta:
        managed = False
        db_table = 'cliente'


class ClienteContrato(models.Model):
    id = models.BigIntegerField(primary_key=True)
    contrato_id_contrato = models.ForeignKey('Contrato', models.DO_NOTHING, db_column='contrato_id_contrato')
    cliente_id_cli = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='cliente_id_cli')

    class Meta:
        managed = False
        db_table = 'cliente_contrato'


class Contrato(models.Model):
    id_contrato = models.BigIntegerField(primary_key=True)
    fec_inicio = models.DateField()
    fec_termino = models.DateField()
    fec_corte = models.DateField()
    fec_pago = models.DateField()
    pago_mensual = models.BigIntegerField()
    pago_extra = models.BigIntegerField()
    total_pago = models.BigIntegerField()
    plan_id_plan = models.ForeignKey('Plan', models.DO_NOTHING, db_column='plan_id_plan')

    class Meta:
        managed = False
        db_table = 'contrato'


class Lista(models.Model):
    id_lista = models.BigIntegerField(primary_key=True)
    descripcion = models.CharField(max_length=250)
    is_valid = models.FloatField()
    recomendacion = models.CharField(max_length=250)
    cliente_id_cli = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='cliente_id_cli')
    profesional_id_prof = models.ForeignKey('Profesional', models.DO_NOTHING, db_column='profesional_id_prof')

    class Meta:
        managed = False
        db_table = 'lista'


class Mejoras(models.Model):
    id_mejora = models.BigIntegerField(primary_key=True)
    propuesta = models.CharField(max_length=250)
    aceptacion = models.FloatField()
    pac = models.ForeignKey('Pac', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'mejoras'


class Pac(models.Model):
    id = models.BigIntegerField(primary_key=True)
    fec_estimada = models.DateField()
    fec_ida = models.DateField()
    actividad_id_actividad = models.ForeignKey(Actividad, models.DO_NOTHING, db_column='actividad_id_actividad')
    cliente_id_cli = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='cliente_id_cli')
    profesional_id_prof = models.ForeignKey('Profesional', models.DO_NOTHING, db_column='profesional_id_prof')

    class Meta:
        managed = False
        db_table = 'pac'


class Perfil(models.Model):
    id_perfil = models.BigIntegerField(primary_key=True)
    rut = models.CharField(max_length=12)
    telefono = models.BigIntegerField()
    direccion = models.CharField(max_length=200)
    tipo_perf = models.CharField(max_length=1)
    id_auth_user = models.ForeignKey('User', on_delete=models.PROTECT, db_column='id_auth_user')

    class Meta:
        managed = False
        db_table = 'perfil'


class Plan(models.Model):
    id_plan = models.BigIntegerField(primary_key=True)
    nombre = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=250)
    costo = models.BigIntegerField()
    id_servicio = models.ForeignKey('Servicio', models.DO_NOTHING, db_column='servicio_id_servicio')

    class Meta:
        managed = False
        db_table = 'plan'


class Profesional(models.Model):
    id_prof = models.BigIntegerField(primary_key=True)
    perfil_id_perfil = models.ForeignKey(Perfil, models.DO_NOTHING, db_column='perfil_id_perfil')

    class Meta:
        managed = False
        db_table = 'profesional'


class Reporte(models.Model):
    id_reporte = models.BigIntegerField(primary_key=True)
    cant_asesoria = models.BigIntegerField()
    cant_llamadas = models.BigIntegerField()
    cant_visitas = models.BigIntegerField()
    cant_accidentes = models.BigIntegerField()
    cant_multas = models.BigIntegerField()
    tipo_reporte_id_tipo_reporte = models.ForeignKey('TipoReporte', models.DO_NOTHING, db_column='tipo_reporte_id_tipo_reporte')
    pac = models.ForeignKey(Pac, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'reporte'


class Servicio(models.Model):
    id_servicio = models.BigIntegerField(primary_key=True)
    nombre = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=250)

    class Meta:
        managed = False
        db_table = 'servicio'


class TipoAsesoria(models.Model):
    id_tipo_ase = models.CharField(primary_key=True, max_length=1)
    nombre = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'tipo_asesoria'


class TipoReporte(models.Model):
    id_tipo_reporte = models.BigIntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'tipo_reporte'


class User(models.Model):
    #id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=150)
    password = models.CharField(max_length=150) 
    first_name = models.CharField(max_length=150) 
    last_name = models.CharField(max_length=150) 
    email = models.CharField(max_length=150) 
    is_active = models.BooleanField
    class Meta:
        managed = False
        db_table = 'auth_user'

    def str(self):
        return self.username


class Visita(models.Model):
    id_visita = models.BigIntegerField(primary_key=True)
    is_extra = models.FloatField()

    class Meta:
        managed = False
        db_table = 'visita'
