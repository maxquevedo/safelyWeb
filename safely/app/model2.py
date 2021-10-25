# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Actividad(models.Model):
    id_actividad = models.BigIntegerField(primary_key=True)
    nombre = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=250)
    tipo = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'actividad'


class Administrador(models.Model):
    id_perfil = models.OneToOneField('Perfil', models.DO_NOTHING, db_column='id_perfil', primary_key=True)
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
    id_cli = models.ForeignKey('Cliente', models.DO_NOTHING, db_column='id_cli')
    id_prof = models.ForeignKey('Profesional', models.DO_NOTHING, db_column='id_prof')

    class Meta:
        managed = False
        db_table = 'alerta'


class Asesoria(models.Model):
    id_actividad = models.OneToOneField(Actividad, models.DO_NOTHING, db_column='id_actividad', primary_key=True)
    id_asesoria = models.BigIntegerField(unique=True)
    descripcion = models.CharField(max_length=250)
    id_tipo_ase = models.ForeignKey('TipoAsesoria', models.DO_NOTHING, db_column='id_tipo_ase')

    class Meta:
        managed = False
        db_table = 'asesoria'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128, blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150, blank=True, null=True)
    first_name = models.CharField(max_length=150, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    email = models.CharField(max_length=254, blank=True, null=True)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Capacitacion(models.Model):
    id_actividad = models.OneToOneField(Actividad, models.DO_NOTHING, db_column='id_actividad', primary_key=True)
    id_capacitacion = models.BigIntegerField(unique=True)
    cant_asistentes = models.CharField(max_length=2)
    materiales = models.CharField(max_length=250)

    class Meta:
        managed = False
        db_table = 'capacitacion'


class Cliente(models.Model):
    id_perfil = models.OneToOneField('Perfil', models.DO_NOTHING, db_column='id_perfil', primary_key=True)
    id_cli = models.BigIntegerField(unique=True)
    cli_razon_social = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'cliente'


class ClienteContrato(models.Model):
    id_contrato = models.ForeignKey('Contrato', models.DO_NOTHING, db_column='id_contrato')
    id_cli = models.OneToOneField(Cliente, models.DO_NOTHING, db_column='id_cli', primary_key=True)

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
    id_plan = models.ForeignKey('Plan', models.DO_NOTHING, db_column='id_plan')

    class Meta:
        managed = False
        db_table = 'contrato'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200, blank=True, null=True)
    action_flag = models.IntegerField()
    change_message = models.TextField(blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100, blank=True, null=True)
    model = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField(blank=True, null=True)
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Lista(models.Model):
    descripcion = models.CharField(max_length=250)
    is_valid = models.CharField(max_length=1)
    recomendacion = models.CharField(max_length=250)
    id_cli = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='id_cli')
    id_prof = models.OneToOneField('Profesional', models.DO_NOTHING, db_column='id_prof', primary_key=True)

    class Meta:
        managed = False
        db_table = 'lista'
        unique_together = (('id_prof', 'id_cli'),)


class Mejoras(models.Model):
    id_mejora = models.BigIntegerField(primary_key=True)
    propuesta = models.CharField(max_length=250)
    aceptacion = models.CharField(max_length=1)
    id_cli = models.ForeignKey('Pac', models.DO_NOTHING, db_column='id_cli')
    id_prof = models.ForeignKey('Pac', models.DO_NOTHING, db_column='id_prof')

    class Meta:
        managed = False
        db_table = 'mejoras'


class Pac(models.Model):
    fec_estimada = models.DateField()
    fec_ida = models.DateField()
    id_actividad = models.ForeignKey(Actividad, models.DO_NOTHING, db_column='id_actividad')
    id_cli = models.OneToOneField(Cliente, models.DO_NOTHING, db_column='id_cli', primary_key=True)
    id_prof = models.ForeignKey('Profesional', models.DO_NOTHING, db_column='id_prof')

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
    id_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='id_usuario')

    class Meta:
        managed = False
        db_table = 'perfil'


class Plan(models.Model):
    id_plan = models.BigIntegerField(primary_key=True)
    nombre = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=250)
    id_servicio = models.ForeignKey('Servicio', models.DO_NOTHING, db_column='id_servicio')

    class Meta:
        managed = False
        db_table = 'plan'


class Profesional(models.Model):
    id_perfil = models.OneToOneField(Perfil, models.DO_NOTHING, db_column='id_perfil', primary_key=True)
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
    id_tipo_reporte = models.ForeignKey('TipoReporte', models.DO_NOTHING, db_column='id_tipo_reporte')
    id_cli = models.ForeignKey(Pac, models.DO_NOTHING, db_column='id_cli')
    id_prof = models.ForeignKey(Pac, models.DO_NOTHING, db_column='id_prof')

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


class Usuario(models.Model):
    id_usuario = models.BigIntegerField(primary_key=True)
    contrasena = models.CharField(max_length=50)
    id_rol = models.ForeignKey(Rol, models.DO_NOTHING, db_column='id_rol')

    class Meta:
        managed = False
        db_table = 'usuario'


class Visita(models.Model):
    id_actividad = models.OneToOneField(Actividad, models.DO_NOTHING, db_column='id_actividad', primary_key=True)
    id_visita = models.BigIntegerField(unique=True)
    is_extra = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'visita'
