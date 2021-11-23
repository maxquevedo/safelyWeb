from django.forms import fields
import django_filters
from django.contrib.auth.models import User

from app import models


class UsertFilter(django_filters.FilterSet):
    username = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = User 
        fields = ['username','groups','first_name','email','is_active']

class PerfilFilter(django_filters.FilterSet):
    class Meta:
        model = models.Perfil
        fields = '__all__'