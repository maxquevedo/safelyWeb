from django.conf.urls import url
from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.utils import timezone

class Perfil(models.Model):
    CHOICES = (
    ('1', "Administrador"),
    ('2', "Profesional"),
    ('3', "Cliente"),
    )
    id_perfil = models.AutoField(primary_key=True)
    rut = models.CharField(max_length=12)
    telefono = models.BigIntegerField()
    direccion = models.CharField(max_length=200)
    tipo_perf = models.CharField(max_length=1, choices=CHOICES)
    id_auth_user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile',db_column='id_auth_user')

    class Meta:
        managed = False
        db_table = 'perfil'
        default_related_name = 'perfil'

    def __str__(self):
        return self.id_auth_user.first_name + ' ' + self.id_auth_user.last_name

class Cliente(models.Model):
    id_cli = models.AutoField(primary_key=True)
    razon_social = models.CharField(max_length=50, null=True, blank=True)
    id_perfil = models.OneToOneField(Perfil, models.DO_NOTHING, db_column='id_perfil',related_name='client')

    class Meta:
        managed = False
        db_table = 'cliente'

    def __str__(self):
        return self.razon_social

class Profesional(models.Model):
    id_prof = models.AutoField(primary_key=True)
    id_perfil = models.OneToOneField(Perfil, models.DO_NOTHING, db_column='id_perfil',related_name='professional')

    class Meta:
        managed = False
        db_table = 'profesional'

    def __str__(self):
        return self.id_perfil.id_auth_user.username

class Administrador(models.Model):
    id_admin = models.AutoField(primary_key=True)
    id_perfil = models.OneToOneField(Perfil, models.DO_NOTHING, db_column='id_perfil',related_name='administrator')

    class Meta:
        managed = False
        db_table = 'administrador'

    def __str__(self):
        return self.id_perfil.id_auth_user.username

class ActCheck(models.Model):
    id_act_check = models.AutoField(primary_key=True)
    id_prof = models.ForeignKey('Profesional', models.DO_NOTHING, db_column='id_prof', blank=True, null=True)
    id_cli = models.OneToOneField('Cliente', models.DO_NOTHING, db_column='id_cli')

    class Meta:
        managed = False
        db_table = 'act_check'

    def __str__(self):
        return self.id_cli.razon_social

class Actividad(models.Model):

    CHOICES_TYPE = (
    ('1', "Capacitación"),
    ('2', "Asesoría"),
    ('3', "Visita"),
    )

    STATUS_CHOICES = (
        ('1', "Solicitado"),
        ('2', "Pendiente"),
        ('3', "Realizado"),
        ('4', "Cancelado")
    )

    id_actividad = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=250)
    descripcion = models.CharField(max_length=250)
    tipo_act = models.CharField('Tipo de actividad',max_length=1, choices=CHOICES_TYPE)
    act_extra = models.BooleanField()
    fec_creacion = models.DateField(auto_now_add=True, blank=True)
    fec_estimada = models.DateField('Fecha estimada',auto_now=False)
    fec_ida = models.DateField('Fecha ida',auto_now=False,blank=True, null=True)
    estado = models.CharField(max_length=1, choices=STATUS_CHOICES)
    id_cli = models.ForeignKey('Cliente', models.DO_NOTHING, db_column='id_cli')
    id_prof = models.ForeignKey('Profesional', models.DO_NOTHING, db_column='id_prof', blank=True, null=True)
    id_capacitacion = models.ForeignKey('Capacitacion', models.DO_NOTHING, db_column='id_capacitacion', blank=True, null=True)
    id_asesoria = models.ForeignKey('Asesoria', models.DO_NOTHING, db_column='id_asesoria', blank=True, null=True)
    id_visita = models.ForeignKey('Visita', models.DO_NOTHING, db_column='id_visita', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'actividad'

    def __str__(self):
        return self.nombre

class Checklist(models.Model):
    id_check = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=1000)
    verificacion = models.BooleanField()
    fec_creado = models.DateField(auto_now_add=True, blank=True)
    id_act_check = models.ForeignKey(ActCheck, models.DO_NOTHING, db_column='id_act_check')

    class Meta:
        managed = False
        db_table = 'checklist'

    def __str__(self):
        return self.nombre

class Alerta(models.Model):
    id_alerta = models.AutoField(primary_key=True)
    fec_aviso = models.DateField(auto_now_add=True, blank=True)
    descripcion = models.CharField(max_length=300)
    estado = models.BooleanField()
    id_cli = models.ForeignKey('Cliente', models.DO_NOTHING, db_column='id_cli')
    id_prof = models.ForeignKey('Profesional', models.DO_NOTHING, db_column='id_prof')

    class Meta:
        managed = False
        db_table = 'alerta'

    #def calculo(sefl)



class Asesoria(models.Model):
    id_asesoria = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=250)
    estado = models.BooleanField()
    id_tipo_ase = models.ForeignKey('TipoAsesoria', models.DO_NOTHING, db_column='id_tipo_ase')

    class Meta:
        managed = False
        db_table = 'asesoria'

    def __str__(self):
        return self.nombre

class Boleta(models.Model):
    id_boleta = models.AutoField(primary_key=True)
    fec_emision_bol = models.DateField()
    fec_pago = models.DateField()
    fec_corte = models.DateField()
    pago_mensual = models.BigIntegerField()
    pagado = models.BooleanField()
    pago_extra = models.BigIntegerField()
    url = models.URLField(max_length = 200, blank=True, null=True)
    id_contrato = models.ForeignKey('Contrato', models.DO_NOTHING, db_column='id_contrato')

    class Meta:
        managed = False
        db_table = 'boleta'

class Capacitacion(models.Model):
    id_capacitacion = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    cant_asistentes = models.CharField(max_length=2)
    materiales = models.CharField(max_length=250)
    estado = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'capacitacion'

    def __str__(self):
        return self.nombre

class Contrato(models.Model):
    id_contrato = models.AutoField(primary_key=True)
    fec_inicio = models.DateField()
    fec_termino = models.DateField()
    total_pago = models.BigIntegerField()
    estado = models.BooleanField()
    id_plan = models.ForeignKey('Plan', models.DO_NOTHING, db_column='id_plan')
    id_cli = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='id_cli')

    class Meta:
        managed = False
        db_table = 'contrato'

    def __str__(self):
        return self.id_cli.id_perfil.id_auth_user.first_name + ' ' + self.id_cli.id_perfil.id_auth_user.last_name

class Mejora(models.Model):
    id_mejora = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    propuesta = models.CharField(max_length=250)
    aceptacion = models.BooleanField()
    estado = models.BooleanField()
    id_actividad = models.ForeignKey(Actividad, models.DO_NOTHING, db_column='id_actividad')

    class Meta:
        managed = False
        db_table = 'mejora'

    def __str__(self):
        return self.nombre



class Plan(models.Model):
    id_plan = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=250)
    costo = models.BigIntegerField()
    estado = models.BooleanField()
    id_servicio = models.ForeignKey('Servicio', models.DO_NOTHING, db_column='id_servicio')

    class Meta:
        managed = False
        db_table = 'plan'

    def __str__(self):
        return self.nombre

class Reporte(models.Model):
    id_reporte = models.AutoField(primary_key=True)
    cant_asesoria = models.BigIntegerField()
    cant_llamadas = models.BigIntegerField()
    cant_visitas = models.BigIntegerField()
    cant_accidentes = models.BigIntegerField()
    cant_multas = models.BigIntegerField()
    fec_emision = models.DateField()
    id_tipo_reporte = models.ForeignKey('TipoReporte', models.DO_NOTHING, db_column='id_tipo_reporte')
    id_actividad = models.ForeignKey(Actividad, models.DO_NOTHING, db_column='id_actividad')

    class Meta:
        managed = False
        db_table = 'reporte'

class Servicio(models.Model):
    id_servicio = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=250)
    estado = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'servicio'

    def __str__(self):
        return self.nombre

class TipoAsesoria(models.Model):
    id_tipo_ase = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'tipo_asesoria'

    def __str__(self):
        return self.nombre

class TipoReporte(models.Model):
    id_tipo_reporte = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'tipo_reporte'

    def __str__(self):
        return self.nombre

class Visita(models.Model):
    id_visita = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    estado = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'visita'

    def __str__(self):
        return self.nombre