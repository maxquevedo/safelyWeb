from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Permission, User, Group
from django.core.exceptions import ValidationError
from django.db.models import fields
from django.forms import widgets
from django.forms.widgets import DateTimeInput
from datetime import date
from .models import Administrador, Boleta, CliCheckPro, Cliente, Contrato, Mejora, Perfil, Plan, Profesional, Servicio,Asesoria,Capacitacion,TipoAsesoria,Actividad, Visita, Checklist


class GrupoForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = '__all__'

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(min_length=5, max_length=25, widget=forms.TextInput(attrs={'class': 'form-control', 
                           'placeholder': 'Ej: Leo.Barraza'}))
    email = forms.CharField(min_length=5, max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 
                           'placeholder': 'Ej: correo@ejemplo.cl'}))

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "password1", "password2","groups", "is_staff"]

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [ "username", "first_name", "last_name", "email"]

class UserActive(forms.ModelForm):
    class Meta:
        model = User
        fields = ['is_active']

## PERFIL

class PerfilForm(forms.ModelForm):
    CHOICES = (
    ('1', "Administrador"),
    ('2', "Profesional"),
    ('3', "Cliente"),
    )
    rut = forms.CharField(min_length=5, max_length=25, widget=forms.TextInput(attrs={'class': 'form-control', 
                           'placeholder': 'Ej: 19.999.999-9'}))
    telefono = forms.CharField(min_length=5, max_length=25, widget=forms.TextInput(attrs={'class': 'form-control', 
                           'placeholder': 'Ej: 569123456'}))
    direccion = forms.CharField(min_length=5, max_length=250, widget=forms.TextInput(attrs={'class': 'form-control', 
                           'placeholder': 'Ej: mi calle # 12365'}))

    tipo_perf = forms.ChoiceField(choices=CHOICES)
    class Meta:
        model = Perfil
        fields = ['id_perfil', 'rut','telefono','direccion','tipo_perf']

class PerfilModificar(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['rut', 'telefono', 'direccion']

# Administrador
class AdminForm(forms.ModelForm):
    class Meta:
        model = Administrador
        fields = []
## PROFESIONAL

class ProfesionalForm(forms.ModelForm):
    class Meta:
        model = Profesional
        fields = []

## CLIENTE

class ClienteForm(forms.ModelForm):
    razon_social = forms.CharField(min_length=5, max_length=25, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 
                           'placeholder': 'Ej: Duoc UC'}))  
    class Meta:
        model = Cliente
        fields = ['razon_social']

## Plan 
class PlanForm(forms.ModelForm):
    nombre = forms.CharField(min_length=4, max_length=20)
    costo = forms.IntegerField(min_value=1, max_value=2000000)

    def clean_nombre(self):
        nombre = self.cleaned_data["nombre"]
        existe = Plan.objects.filter(nombre__iexact=nombre).exists()

        if existe:
            raise ValidationError("?????? El Nombre del Plan ya existe ??????")
        return nombre

    class Meta:
        model = Plan
        fields = '__all__'

        widgets = {
            'descripcion': forms.Textarea
        }

class PlanUpdateForm(forms.ModelForm):

    class Meta:
        model = Plan
        fields = ['nombre', 'descripcion','costo', 'id_servicio']

        widgets = {
            'descripcion': forms.Textarea
        }

class PlanActive(forms.ModelForm):
    class Meta:
        model = Plan
        fields = ['estado']
## Servicio 
class ServicioForm(forms.ModelForm):
    nombre = forms.CharField(min_length=4, max_length=20)
    
    class Meta:
        model = Servicio
        fields = '__all__'
    
        widgets = {
            'descripcion': forms.Textarea
        }

class ServicioUpdateForm(forms.ModelForm):
    class Meta:
        model = Servicio
        fields = ['nombre', 'descripcion']

        widgets = {
            'descripcion': forms.Textarea
        }

class ServicioActive(forms.ModelForm):
    class Meta:
        model = Servicio
        fields = ['estado']

## ASESORIAS 
class AsesoriaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AsesoriaForm, self).__init__(*args, **kwargs)
        self.initial['estado'] = '1'
    nombre = forms.CharField(min_length=4, max_length=250)

    def clean_nombre(self):
        nombre = self.cleaned_data["nombre"]
        existe = Asesoria.objects.filter(nombre__iexact=nombre).exists()

        if existe:
            raise ValidationError("?????? Ya existe esa Asesor??a ??????")
        return nombre

    class Meta:
        model = Asesoria
        fields = '__all__'

        widgets = {
            'descripcion': forms.Textarea
        }

class TipoAsesoriaForm(forms.ModelForm):
    class Meta:
        model = TipoAsesoria
        fields = '__all__'

class AsesoriaModificar(forms.ModelForm):
    class Meta:
        model = Asesoria
        fields = '__all__'
        widgets = {
            'descripcion': forms.Textarea
        }

class IngresarAsesoria(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(IngresarAsesoria, self).__init__(*args, **kwargs)
        self.initial['tipo_act'] = '2'

    class Meta:
        model = Actividad
        fields = '__all__'
        widgets = {
            'fec_estimada': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Seleccionar Fecha', 'type':'date'}),
            'fec_ida': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Seleccionar Fecha', 'type':'date'}),
        }

class DesactivarAseForm(forms.ModelForm):
    class Meta:
        model = Asesoria
        fields = ['estado']
## Capacitacion 
class CapacitacionForm(forms.ModelForm):
    nombre = forms.CharField(min_length=4, max_length=250)
    cant_asistentes = forms.IntegerField(min_value=1, max_value=100)

    def clean_nombre(self):
        nombre = self.cleaned_data["nombre"]
        existe = Capacitacion.objects.filter(nombre__iexact=nombre).exists()

        if existe:
            raise ValidationError("?????? Ya existe esa Capacitacion ??????")
        return nombre

    class Meta:
        model = Capacitacion
        fields = '__all__'
        widgets = {
            'materiales': forms.Textarea
        }

class CapacitacionModificar(forms.ModelForm):
    class Meta:
        model = Capacitacion
        fields = ['nombre', 'cant_asistentes','materiales']

class IngresarCapacitacion(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(IngresarCapacitacion, self).__init__(*args, **kwargs)
        self.initial['tipo_act'] = '1'

    class Meta:
        model = Actividad
        fields = '__all__'
        widgets = {
            'fec_estimada': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Seleccionar Fecha', 'type':'date'}),
            'fec_ida': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Seleccionar Fecha', 'type':'date'}),
        }
## Mejoras
class MejoraForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(MejoraForm, self).__init__(*args, **kwargs)
        self.initial['estado'] = '1'

    class Meta:
        model = Mejora
        fields = '__all__'

        widgets = {
            'propuesta': forms.Textarea
        }

## Actividad
class DateTimeInput(forms.DateTimeInput):
    input_type = 'date-local'

class ActividadForm(forms.ModelForm):
    nombre = forms.CharField(min_length=4, max_length=250)

    def clean_nombre(self):
        nombre = self.cleaned_data["nombre"]
        existe = Actividad.objects.filter(nombre__iexact=nombre).exists()

        if existe:
            raise ValidationError("?????? El Nombre de la actividad ya existe ??????")
        return nombre

    def clean_fec_estimada(self):
        fecha = self.cleaned_data['fec_estimada']

        if fecha < date.today():
            raise forms.ValidationError("?????? Fecha ingresada incorrecta ??????")
        return fecha
        
        
    class Meta:
        model = Actividad
        fields = '__all__'

        widgets = {
            'fec_estimada': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Selecciona una fecha', 'type':'date'}),
            'fec_ida': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Selecciona una fecha', 'type':'date'}),
            'act_extra': forms.CheckboxInput()
        }
        
class ActividadEstadoForm(forms.ModelForm):
    class Meta:
        model = Actividad
        fields = ['estado']

class ActividadModForm(forms.ModelForm):
    class Meta:
        model = Actividad
        fields = ['nombre', 'descripcion', 'fec_estimada', 'fec_ida' ]


class ActualizarActividad(forms.ModelForm):
    class Meta:
        model = Actividad
        fields = ['id_prof']
## VISITA
class VisitaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(VisitaForm, self).__init__(*args, **kwargs)
        self.initial['estado'] = '1'

    class Meta:
        model = Visita
        fields = '__all__'

class IngresarVisita(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(IngresarVisita, self).__init__(*args, **kwargs)
        self.initial['tipo_act'] = '3'

    class Meta:
        model = Actividad
        fields = '__all__'
        widgets = {
            'fec_estimada': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Seleccionar Fecha', 'type':'date'}),
            'fec_ida': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Seleccionar Fecha', 'type':'date'}),
        }

class ContratoForm(forms.ModelForm):
    class Meta:
        model = Contrato
        fields= '__all__'
        widgets = {
            'fec_inicio': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Seleccionar Fecha', 'type':'date'}),
            'fec_termino': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Seleccionar Fecha', 'type':'date'}),
        }

class BoletaForm(forms.ModelForm):
    class Meta:
        model = Boleta
        fields= '__all__'
        widgets = {
            'fec_emision_bol': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Seleccionar Fecha', 'type':'date'}),
            'fec_pago': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Seleccionar Fecha', 'type':'date'}),
            'fec_corte': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Seleccionar Fecha', 'type':'date'}),
        }

class BoletaForm2(forms.ModelForm):
    url = forms.URLField()
    class Meta:
        model = Boleta
        fields= ['id_boleta','fec_emision_bol','fec_pago','fec_corte','pago_mensual','pagado','pago_extra','url','id_contrato']

class ChecklistForm(forms.ModelForm):
    class Meta:
        model = Checklist
        fields = '__all__'

class ChecklistVerificador(forms.ModelForm):
    class Meta:
        model = Checklist
        fields = ['verificacion']

class listaForm(forms.ModelForm):
    class Meta:
        model = CliCheckPro
        fields = '__all__'