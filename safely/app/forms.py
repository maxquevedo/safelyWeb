from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db.models import fields
from django.forms.widgets import DateTimeInput
from .models import Cliente, Lista, Mejora, Perfil, Plan, Profesional, Servicio,Asesoria,Capacitacion,Lista,TipoAsesoria,Actividad, Visita




class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "password1", "password2","groups"]

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [ "username", "first_name", "last_name", "email"]

class UserActive(forms.ModelForm):
    class Meta:
        model = User
        fields = ['is_active']
## Plan 
class PlanForm(forms.ModelForm):
    class Meta:
        model = Plan
        fields = '__all__'

        widgets = {
            'descripcion': forms.Textarea
        }

class PlanUpdateForm(forms.ModelForm):
    class Meta:
        model = Plan
        fields = ['nombre', 'descripcion', 'id_servicio']

        widgets = {
            'descripcion': forms.Textarea
        }
## Servicio 
class ServicioForm(forms.ModelForm):
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

## ASESORIAS 
class AsesoriaForm(forms.ModelForm):
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
## Capacitacion 
class CapacitacionForm(forms.ModelForm):
    class Meta:
        model = Capacitacion
        fields = '__all__'

class CapacitacionModificar(forms.ModelForm):
    class Meta:
        model = Capacitacion
        fields = ['nombre', 'cant_asistentes','materiales']
## Lista 
class ListaForm(forms.ModelForm):
    class Meta:
        model = Lista
        fields = '__all__'

class ListaModificar(forms.ModelForm):
    class Meta:
        model = Lista
        fields = '__all__'
## Mejoras
class MejoraForm(forms.ModelForm):
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
    class Meta:
        model = Actividad
        fields = '__all__'

        widgets = {
            'fec_estimada': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
            'fec_ida': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
        }
        
class ActividadEstadoForm(forms.ModelForm):
    class Meta:
        model = Actividad
        fields = ['estado']

class ActividadModForm(forms.ModelForm):
    class Meta:
        model = Actividad
        fields = ['nombre', 'descripcion', 'fec_estimada', 'fec_ida' ]

## VISITA
class VisitaForm(forms.ModelForm):
    class Meta:
        model = Visita
        fields = '__all__'

## CLIENTE

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'

## PROFESIONAL

class ProfesionalForm(forms.ModelForm):
    class Meta:
        model = Profesional
        fields = '__all__'

## PERFIL

class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['id_perfil', 'rut','telefono','direccion','tipo_perf','id_auth_user']
