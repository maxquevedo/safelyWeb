# Este es un módulo de modelo de Django generado automáticamente.
# Tendrá que hacer lo siguiente manualmente para limpiar esto:
# * Reorganizar el orden de los modelos
# * Asegúrese de que cada modelo tenga un campo con primary_key = True
# * Asegúrese de que cada ForeignKey y OneToOneField tenga `on_delete` configurado para el comportamiento deseado
# * Elimine las líneas `managed = False` si desea permitir que Django cree, modifique y elimine la tabla
# Siéntase libre de cambiar el nombre de los modelos, pero no cambie el nombre de los valores de db_table o los nombres de los campos.
from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import EmailField


class Actividad(models.Model):
    id_actividad = models.BigIntegerField(primary_key=True)
    nombre = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=250)
    tipo = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'actividad'


class Administrador(models.Model):
    id_perfil = models.OneToOneField('Perfil', on_delete=models.PROTECT, db_column='id_perfil', primary_key=True)
    id_admin = models.BigIntegerField(unique=True)
    nombre = models.CharField(max_length=20)
    apellido_pat = models.CharField(max_length=40)
    apellido_mat = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'administrador'


class Alerta(models.Model):
    id_alerta = models.BigIntegerField(primary_key=True)
    fec_aviso = models.DateField()
    id_cli = models.ForeignKey('Cliente', on_delete=models.PROTECT, db_column='id_cli')
    id_prof = models.ForeignKey('Profesional', on_delete=models.PROTECT, db_column='id_prof')

    class Meta:
        managed = False
        db_table = 'alerta'


class Asesoria(models.Model):
    id_actividad = models.OneToOneField(Actividad, on_delete=models.PROTECT, db_column='id_actividad', primary_key=True)
    id_asesoria = models.BigIntegerField(unique=True)
    descripcion = models.CharField(max_length=250)
    id_tipo_ase = models.ForeignKey('TipoAsesoria', on_delete=models.PROTECT, db_column='id_tipo_ase')

    class Meta:
        managed = False
        db_table = 'asesoria'


class Capacitacion(models.Model):
    id_actividad = models.OneToOneField(Actividad, on_delete=models.PROTECT, db_column='id_actividad', primary_key=True)
    id_capacitacion = models.BigIntegerField(unique=True)
    cant_asistentes = models.CharField(max_length=2)
    materiales = models.CharField(max_length=250)

    class Meta:
        managed = False
        db_table = 'capacitacion'


class Cliente(models.Model):
    id_perfil = models.OneToOneField('Perfil', on_delete=models.PROTECT, db_column='id_perfil', primary_key=True)
    id_cli = models.BigIntegerField(unique=True)
    cli_razon_social = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'cliente'


class ClienteContrato(models.Model):
    id_contrato = models.ForeignKey('Contrato', on_delete=models.PROTECT, db_column='id_contrato')
    id_cli = models.OneToOneField(Cliente, on_delete=models.PROTECT, db_column='id_cli', primary_key=True)

    class Meta:
        managed = False
        db_table = 'cliente_contrato'


class Contrato(models.Model):
    id_contrato = models.BigIntegerField(primary_key=True)
    fec_inicio = models.DateField()
    fec_termino = models.DateField()
    fec_vencimiento = models.DateField()
    fec_pago = models.DateField()
    pago_mensual = models.BigIntegerField()
    pago_extra = models.BigIntegerField()
    total_pago = models.BigIntegerField()
    id_plan = models.ForeignKey('Plan', on_delete=models.PROTECT, db_column='id_plan')

    class Meta:
        managed = False
        db_table = 'contrato'


class Lista(models.Model):
    descripcion = models.CharField(max_length=250)
    is_valid = models.CharField(max_length=1)
    recomendacion = models.CharField(max_length=250)
    id_cli = models.ForeignKey(Cliente, on_delete=models.PROTECT, db_column='id_cli')
    id_prof = models.OneToOneField('Profesional', on_delete=models.PROTECT, db_column='id_prof', primary_key=True)

    class Meta:
        managed = False
        db_table = 'lista'
        unique_together = (('id_prof', 'id_cli'),)


class Mejoras(models.Model):
    id_mejora = models.BigIntegerField(primary_key=True)
    propuesta = models.CharField(max_length=250)
    aceptacion = models.CharField(max_length=1)
    id_cli = models.ForeignKey('Pac', on_delete=models.PROTECT, db_column='id_cli', related_name='+')
    id_prof = models.ForeignKey('Pac', on_delete=models.PROTECT, db_column='id_prof')

    class Meta:
        managed = False
        db_table = 'mejoras'


class Pac(models.Model):
    fec_estimada = models.DateField()
    fec_ida = models.DateField()
    id_actividad = models.ForeignKey(Actividad, on_delete=models.PROTECT, db_column='id_actividad')
    id_cli = models.OneToOneField(Cliente, on_delete=models.PROTECT, db_column='id_cli', primary_key=True)
    id_prof = models.ForeignKey('Profesional', on_delete=models.PROTECT, db_column='id_prof')

    class Meta:
        managed = False
        db_table = 'pac'
        unique_together = (('id_cli', 'id_prof'),)


class Perfil(models.Model):
    id_perfil = models.BigIntegerField(primary_key=True)
    rut = models.CharField(max_length=12)
    telefono = models.BigIntegerField()
    email = models.CharField(max_length=50)
    direccion = models.CharField(max_length=200)
    fec_registro = models.DateField()
    vigente = models.CharField(max_length=1)
    tipo_perf = models.CharField(max_length=1)
    id_auth_user = models.ForeignKey('User', on_delete=models.PROTECT, db_column='id_auth_user')

    class Meta:
        managed = False
        db_table = 'perfil'


class Plan(models.Model):
    id_plan = models.BigIntegerField(primary_key=True)
    nombre = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=250)
    id_servicio = models.ForeignKey('Servicio', on_delete=models.PROTECT, db_column='id_servicio')

    class Meta:
        managed = False
        db_table = 'plan'


class Profesional(models.Model):
    id_perfil = models.OneToOneField(Perfil, on_delete=models.PROTECT, db_column='id_perfil', primary_key=True)
    id_prof = models.BigIntegerField(unique=True)
    nombre = models.CharField(max_length=20)
    apellido_pat = models.CharField(max_length=40)
    apellido_mat = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'profesional'


class Reporte(models.Model):
    id_reporte = models.BigIntegerField(primary_key=True)
    cant_visita = models.BigIntegerField()
    cant_asesoria = models.BigIntegerField()
    cant_llamadas = models.BigIntegerField()
    cant_visitas = models.BigIntegerField()
    cant_accidentes = models.BigIntegerField()
    cant_multas = models.BigIntegerField()
    id_tipo_reporte = models.ForeignKey('TipoReporte', on_delete=models.PROTECT, db_column='id_tipo_reporte')
    id_cli = models.ForeignKey(Pac, on_delete=models.PROTECT, db_column='id_cli')
    id_prof = models.ForeignKey(Pac, on_delete=models.PROTECT, db_column='id_prof',related_name='+')

    class Meta:
        managed = False
        db_table = 'reporte'


class Rol(models.Model):
    id_rol = models.CharField(primary_key=True, max_length=1)
    nombre = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=250)

    class Meta:
        managed = False
        db_table = 'rol'

    def __str__(self):
        return self.nombre


class Servicio(models.Model):
    id_servicio = models.BigIntegerField(primary_key=True)
    nombre = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=250)

    class Meta:
        managed = False
        db_table = 'servicio'
    
    def __str__(self):
        return self.nombre


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


class Usuario(models.Model):
    id_usuario = models.BigIntegerField(primary_key=True)
    contrasena = models.CharField(max_length=50)
    id_rol = models.ForeignKey(Rol, on_delete=models.PROTECT, db_column='id_rol')

    class Meta:
        managed = False
        db_table = 'usuario'

    def __int__(self):
        return self.id_usuario

class Visita(models.Model):
    id_actividad = models.OneToOneField(Actividad, on_delete=models.PROTECT, db_column='id_actividad', primary_key=True)
    id_visita = models.BigIntegerField(unique=True)
    is_extra = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'visita'


class User(models.Model):
    #id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=150)
    password = models.CharField(max_length=150) 
    first_name = models.CharField(max_length=150) 
    last_name = models.CharField(max_length=150) 
    email = models.CharField(max_length=150) 
    
    class Meta:
        managed = False
        db_table = 'auth_user'

    def __str__(self):
        return self.username