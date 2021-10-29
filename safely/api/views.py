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