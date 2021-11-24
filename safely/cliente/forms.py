from django.db.models import fields
from app import models
from django import forms


class ClientUserUpdate(forms.Form):
    class Meta:
        model = models.User
        fields = [ "username", "first_name", "last_name", "email"]

class ClienteProfileUpdate(forms.Form):
    class Meta:
        model = models.Perfil
        fields = '__all__'
class ClienteUpdate(forms.Form):
    class Meta:
        model = models.Cliente
        fields = '__all__'