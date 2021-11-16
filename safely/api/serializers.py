from django.db import models
from rest_framework import fields, serializers
from django.contrib.auth.models import User

# Import Modelos
from app import models

"""
    ModelSerializer:

    Un `ModelSerializer` es solo un` Serializer` normal, excepto que:

    * Un conjunto de campos predeterminados se completa automáticamente.
    * Un conjunto de validadores predeterminados se completa automáticamente.
    * Se proporcionan implementaciones predeterminadas `.create ()` y `.update ()`.

    El proceso de determinar automáticamente un conjunto de campos de serializador.
    basado en los campos del modelo es razonablemente complejo, pero es casi seguro que
    no es necesario profundizar en la implementación.

    Si la clase `ModelSerializer` * no * genera el conjunto de campos que
    necesita, debe declarar los campos adicionales / diferentes explícitamente en
    la clase serializador, o simplemente use una clase `Serializador`.
"""

# User Model
class UserSerializer(serializers.ModelSerializer):
    """ Serializa objeto de User"""
    class Meta:
        model = models.User
        #fields = ('id', 'username','password')
        fields = '__all__'
        extra_kwargs = {
            'password':{
                'write_only':True,
                'style': {'input_type':'password'}
            }
        }
        
#Model actividad

class ActividadSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Actividad
        fields = '__all__'