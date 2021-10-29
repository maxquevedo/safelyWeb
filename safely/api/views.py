from rest_framework.response import Response
from rest_framework.decorators import api_view
from app.models import (Actividad,Administrador,Alerta,Asesoria,Capacitacion,Cliente,Contrato,Lista,
Mejoras,Pac,Perfil,Plan,Profesional,Reporte,Servicio,TipoAsesoria,TipoReporte,User,Visita
)
from .serializers import (ActividadSerializer,AdministradorSerializer,AlertaSerializer,AsesoriaSerializer,
CapacitacionSerializer,ClienteSerializer,ContratoSerializer,ListaSerializer,MejorasSerializer,
PacSerializer,PerfilSerializer,PlanSerializer,ProfesionalSerializer,ReporteSerializer,ServicioSerializer,
TipoAsesoriaSerializer,TipoReporteSerializer,UserSerializer,VisitaSerializer
)

from django.contrib.auth.models import Group, User
# ACTIVIDAD

@api_view(['GET'])
def ActividadLista(request):
    act = Actividad.objects.all()
    serializer = ActividadSerializer(act, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def ActividadDetalles(request,pk):
    act = Actividad.objects.get(id_actividad=pk)
    serializer = ActividadSerializer(act, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def ActividadCrear(request):
    serializer = ActividadSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['PATCH'])
def ActividadModificar(request,pk):
    act = Actividad.objects.get(id_actividad=pk)
    data = request.data

    act.nombre = data.get("nombre", act.nombre)
    act.descripcion = data.get("descripcion", act.descripcion)
    act.tipo_actividad = data.get("tipo_actividad", act.tipo_actividad)
    act.id_capacitacion = data.get("id_capacitacion", act.id_capacitacion)
    act.id_asesoria = data.get("id_asesoria", act.id_asesoria)
    act.id_visita = data.get("id_visita", act.id_visita)

    act.save()
    serializer = ActividadSerializer(act)
    return Response(serializer.data)


#@api_view(['POST'])
#def ActividadModificar(request, pk):
#    act = Actividad.objects.get(id_actividad=pk)
#    serializer = ActividadSerializer(instance = act ,data=request.data)

#    if serializer.is_valid():
#        serializer.save()
#    return Response(serializer.data)

@api_view(['DELETE'])
def ActividadEliminar(request, pk):
    act = Actividad.objects.get(id_actividad=pk)
    act.delete()
    return Response('Eliminado correctamente')

##########
##########
##########

# CapacitacionSerializer

@api_view(['GET'])
def CapacitacionLista(request):
    act = Capacitacion.objects.all()
    serializer = CapacitacionSerializer(act, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def CapacitacionDetalles(request,pk):
    act = Capacitacion.objects.get(id_capacitacion=pk)
    serializer = CapacitacionSerializer(act, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def CapacitacionCrear(request):
    serializer = CapacitacionSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['PATCH'])
def CapacitacionModificar(request,pk):
    act = Capacitacion.objects.get(id_capacitacion=pk)
    data = request.data

    act.id_capacitacion = data.get("id_capacitacion", act.id_capacitacion)
    act.cant_asistentes = data.get("cant_asistentes", act.cant_asistentes)
    act.materiales = data.get("materiales", act.materiales)

    act.save()
    serializer = CapacitacionSerializer(act)
    return Response(serializer.data)


@api_view(['DELETE'])
def CapacitacionEliminar(request, pk):
    act = Capacitacion.objects.get(id_capacitacion=pk)
    act.delete()
    return Response('Eliminado correctamente')

##########
##########
##########

# ClienteSerializer

@api_view(['GET'])
def ClienteLista(request):
    act = Cliente.objects.all()
    serializer = ClienteSerializer(act, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def ClienteDetalles(request,pk):
    act = Cliente.objects.get(id_cliente=pk)
    serializer = ClienteSerializer(act, many=False)
    return Response(serializer.data)

#agregar lo demais
##########
##########
##########

# ContratoSerializer

@api_view(['GET'])
def ContratoLista(request):
    act = Contrato.objects.all()
    serializer = ContratoSerializer(act, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def ContratoDetalles(request,pk):
    act = Contrato.objects.get(id_contrato=pk)
    serializer = ContratoSerializer(act, many=False)
    return Response(serializer.data)

##########
##########
##########
# ProfesionalSerializer

@api_view(['GET'])
def ProfesionalLista(request):
    act = Profesional.objects.all()
    serializer = ProfesionalSerializer(act, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def ProfesionalDetalles(request,pk):
    act = Profesional.objects.get(id_profesional=pk)
    serializer = ProfesionalSerializer(act, many=False)
    return Response(serializer.data)

##########
##########
##########
# AsesoriaSerializer

@api_view(['GET'])
def AsesoriaLista(request):
    act = Asesoria.objects.all()
    serializer = AsesoriaSerializer(act, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def AsesoriaDetalles(request,pk):
    act = Asesoria.objects.get(id_asesoria=pk)
    serializer = AsesoriaSerializer(act, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def AsesoriaCrear(request):
    serializer = AsesoriaSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['PATCH'])
def AsesoriaModificar(request,pk):
    act = Asesoria.objects.get(id_asesoria=pk)
    data = request.data

    act.id_asesoria = data.get("id_asesoria", act.id_asesoria)
    act.descripcion = data.get("descripcion", act.descripcion)
    act.id_tipo_asesoria = data.get("id_tipo_asesoria", act.id_tipo_asesoria)

    act.save()
    serializer = AsesoriaSerializer(act)
    return Response(serializer.data)


@api_view(['DELETE'])
def AsesoriaEliminar(request, pk):
    act = Asesoria.objects.get(id_asesoria=pk)
    act.delete()
    return Response('Eliminado correctamente')

##########
##########
##########

# TipoAsesoriaSerializer

@api_view(['GET'])
def TipoAsesoriaLista(request):
    act = TipoAsesoria.objects.all()
    serializer = TipoAsesoriaSerializer(act, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def TipoAsesoriaDetalles(request,pk):
    act = TipoAsesoria.objects.get(id_tipo_asesoria=pk)
    serializer = TipoAsesoriaSerializer(act, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def TipoAsesoriaCrear(request):
    serializer = TipoAsesoriaSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['PATCH'])
def TipoAsesoriaModificar(request,pk):
    act = TipoAsesoria.objects.get(id_tipo_asesoria=pk)
    data = request.data

    act.id_tipo_asesoria = data.get("id_tipo_asesoria", act.id_tipo_asesoria)
    act.nombre = data.get("nombre", act.nombre)

    act.save()
    serializer = TipoAsesoriaSerializer(act)
    return Response(serializer.data)


@api_view(['DELETE'])
def TipoAsesoriaEliminar(request, pk):
    act = TipoAsesoria.objects.get(id_tipo_asesoria=pk)
    act.delete()
    return Response('Eliminado correctamente')

##########
##########
##########

# ListaSerializer

@api_view(['GET'])
def ListaLista(request):
    act = Lista.objects.all()
    serializer = ListaSerializer(act, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def ListaDetalles(request,pk):
    act = Lista.objects.get(id_lista=pk)
    serializer = ListaSerializer(act, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def ListaCrear(request):
    serializer = ListaSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['PATCH'])
def ListaModificar(request,pk):
    act = Lista.objects.get(id_lista=pk)
    data = request.data

    act.id_lista = data.get("id_lista", act.id_lista)
    act.descripcion = data.get("descripcion", act.descripcion)
    act.is_valid = data.get("is_valid", act.is_valid)
    act.recomendacion = data.get("recomendacion", act.recomendacion)
    act.id_cliente = data.get("id_cliente", act.id_cliente)
    act.id_profesional = data.get("id_profesional", act.id_profesional)

    act.save()
    serializer = ListaSerializer(act)
    return Response(serializer.data)


@api_view(['DELETE'])
def ListaEliminar(request, pk):
    act = Lista.objects.get(id_lista=pk)
    act.delete()
    return Response('Eliminado correctamente')

##########
##########
##########

# VisitaSerializer

@api_view(['GET'])
def VisitaLista(request):
    act = Visita.objects.all()
    serializer = VisitaSerializer(act, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def VisitaDetalles(request,pk):
    act = Visita.objects.get(id_visita=pk)
    serializer = VisitaSerializer(act, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def VisitaCrear(request):
    serializer = VisitaSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['PATCH'])
def VisitaModificar(request,pk):
    act = Visita.objects.get(id_visita=pk)
    data = request.data

    act.id_visita = data.get("id_visita", act.id_visita)
    act.is_extra = data.get("is_extra", act.is_extra)

    act.save()
    serializer = VisitaSerializer(act)
    return Response(serializer.data)


@api_view(['DELETE'])
def VisitaEliminar(request, pk):
    act = Visita.objects.get(id_visita=pk)
    act.delete()
    return Response('Eliminado correctamente')

##########
##########
##########


# AlertaSerializer

@api_view(['GET'])
def AlertaLista(request):
    act = Alerta.objects.all()
    serializer = AlertaSerializer(act, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def AlertaDetalles(request,pk):
    act = Alerta.objects.get(id_alerta=pk)
    serializer = AlertaSerializer(act, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def AlertaCrear(request):
    serializer = AlertaSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['PATCH'])
def AlertaModificar(request,pk):
    act = Alerta.objects.get(id_alerta=pk)
    data = request.data

    act.id_alerta = data.get("id_alerta", act.id_alerta)
    act.fec_aviso = data.get("fec_aviso", act.fec_aviso)
    act.id_cliente = data.get("id_cliente", act.id_cliente)
    act.id_profesional = data.get("id_profesional", act.id_profesional)

    act.save()
    serializer = AlertaSerializer(act)
    return Response(serializer.data)


@api_view(['DELETE'])
def AlertaEliminar(request, pk):
    act = Alerta.objects.get(id_alerta=pk)
    act.delete()
    return Response('Eliminado correctamente')

##########
##########
##########

# MejorasSerializer

@api_view(['GET'])
def MejorasLista(request):
    act = Mejoras.objects.all()
    serializer = MejorasSerializer(act, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def MejorasDetalles(request,pk):
    act = Mejoras.objects.get(id_mejora=pk)
    serializer = MejorasSerializer(act, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def MejorasCrear(request):
    serializer = MejorasSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['PATCH'])
def MejorasModificar(request,pk):
    act = Mejoras.objects.get(id_mejora=pk)
    data = request.data

    act.id_mejora = data.get("id_mejora", act.id_mejora)
    act.propuesta = data.get("propuesta", act.propuesta)
    act.aceptacion = data.get("aceptacion", act.aceptacion)
    act.pac = data.get("pac", act.pac)

    act.save()
    serializer = MejorasSerializer(act)
    return Response(serializer.data)


@api_view(['DELETE'])
def MejorasEliminar(request, pk):
    act = Mejoras.objects.get(id_mejora=pk)
    act.delete()
    return Response('Eliminado correctamente')

##########
##########
##########

# PacSerializer

@api_view(['GET'])
def PacLista(request):
    act = Pac.objects.all()
    serializer = PacSerializer(act, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def PacDetalles(request,pk):
    act = Pac.objects.get(id=pk)
    serializer = PacSerializer(act, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def PacCrear(request):
    serializer = PacSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['PATCH'])
def PacModificar(request,pk):
    act = Pac.objects.get(id=pk)
    data = request.data

    act.id = data.get("id", act.id)
    act.fec_estimada = data.get("fec_estimada", act.fec_estimada)
    act.fec_ida = data.get("fec_ida", act.fec_ida)
    act.estado = data.get("estado", act.estado)
    act.id_actividad = data.get("id_actividad", act.id_actividad)
    act.id_cliente = data.get("id_cliente", act.id_cliente)
    act.id_profesional = data.get("id_profesional", act.id_profesional)

    act.save()
    serializer = PacSerializer(act)
    return Response(serializer.data)


@api_view(['DELETE'])
def PacEliminar(request, pk):
    act = Pac.objects.get(id=pk)
    act.delete()
    return Response('Eliminado correctamente')

##########
##########
##########

# UserSerializer

@api_view(['GET'])
def UserLista(request):
    act = User.objects.all()
    serializer = UserSerializer(act, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def UserDetalles(request,pk):
    act = User.objects.get(id=pk)
    serializer = UserSerializer(act, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def UserCrear(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['PATCH'])
def UserModificar(request,pk):
    act = User.objects.get(id=pk)
    data = request.data

    act.id = data.get("id", act.id)
    act.username = data.get("username", act.username)
    act.password = data.get("password", act.password)
    act.first_name = data.get("first_name", act.first_name)
    act.last_name = data.get("last_name", act.last_name)
    act.email = data.get("email", act.email)

    act.save()
    serializer = UserSerializer(act)
    return Response(serializer.data)


@api_view(['DELETE'])
def UserEliminar(request, pk):
    act = User.objects.get(id=pk)
    act.delete()
    return Response('Eliminado correctamente')

##########
##########
##########

#perfil