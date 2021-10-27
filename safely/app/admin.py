from django.contrib import admin

from app.models import *

admin.site.register(Perfil)
admin.site.register(Profesional)
admin.site.register(Administrador)
admin.site.register(Cliente)


admin.site.register(Actividad)
admin.site.register(Asesoria)
admin.site.register(TipoAsesoria)
admin.site.register(Capacitacion)
admin.site.register(Mejoras)
admin.site.register(Pac)

admin.site.register(Alerta)
admin.site.register(Lista)

admin.site.register(ClienteContrato)
admin.site.register(Contrato)



admin.site.register(Plan)
admin.site.register(Servicio)


admin.site.register(Reporte)
admin.site.register(TipoReporte)
