from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db.models import fields
from .models import Plan, Servicio

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "password1", "password2"]

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [ "username", "first_name", "last_name", "email"]

class PlanForm(forms.ModelForm):
    class Meta:
        model = Plan
        fields = '__all__'

class PlanUpdateForm(forms.ModelForm):
    class Meta:
        model = Plan
        fields = ['nombre', 'descripcion', 'id_servicio']

class ServicioForm(forms.ModelForm):
    class Meta:
        model = Servicio
        fields = '__all__'

class ServicioUpdateForm(forms.ModelForm):
    class Meta:
        model = Servicio
        fields = ['nombre', 'descripcion']
