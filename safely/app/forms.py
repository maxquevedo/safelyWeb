from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db.models import fields
from django.forms.widgets import DateTimeInput
from .models import Lista, Mejoras, Plan, Servicio,Asesoria,Capacitacion,Lista,Mejoras,TipoAsesoria,Actividad, Visita




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

class PlanUpdateForm(forms.ModelForm):
    class Meta:
        model = Plan
        fields = ['nombre', 'descripcion', 'id_servicio']
## Servicio 
class ServicioForm(forms.ModelForm):
    class Meta:
        model = Servicio
        fields = '__all__'

class ServicioUpdateForm(forms.ModelForm):
    class Meta:
        model = Servicio
        fields = ['nombre', 'descripcion']

## ASESORIAS 
class AsesoriaForm(forms.ModelForm):
    class Meta:
        model = Asesoria
        fields = '__all__'

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
class MejorasForm(forms.ModelForm):
    class Meta:
        model = Mejoras
        fields = '__all__'

## Actividad
class DateTimeInput(forms.DateTimeInput):
    input_type = 'datetime-local'

class ActividadForm(forms.ModelForm):
    class Meta:
        model = Actividad
        fields = '__all__'

        widgets = {
            
            'fec_estimada': DateTimeInput(attrs={'class': 'form-control'}),
            'fec_ida': DateTimeInput(attrs={'class': 'form-control'}),
        }
      
## VISITA
class VisitaForm(forms.ModelForm):
    class Meta:
        model = Visita
        fields = '__all__'