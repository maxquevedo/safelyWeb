from django.db.models import fields
from app import models
from django import forms


class ClientUserUpdate(forms.ModelForm):
    class Meta:
        model = models.User
        fields = [ "username", "first_name", "last_name", "email"]

class ClienteProfileUpdate(forms.ModelForm):
    class Meta:
        model = models.Perfil
        fields = ["rut","telefono","direccion"]
class ClienteUpdate(forms.ModelForm):
    class Meta:
        model = models.Cliente
        fields = ["razon_social"]

