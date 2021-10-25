from django.contrib import admin
from .models import (
    Actividad,Asesoria,Capacitacion,Mejoras,Pac,TipoAsesoria,Visita, Cliente, Profesional, Perfil,
    User
)
# Register your models here.

admin.site.register(Actividad)
admin.site.register(Asesoria)
admin.site.register(Capacitacion)
admin.site.register(Mejoras)
admin.site.register(Pac)
admin.site.register(TipoAsesoria)
admin.site.register(Visita)

admin.site.register(Cliente)
admin.site.register(Profesional)
admin.site.register(Perfil)
admin.site.register(User)
