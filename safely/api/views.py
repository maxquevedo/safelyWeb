from rest_framework.response import Response
from rest_framework.decorators import api_view
from app.models import (Actividad,Administrador,Alerta,Asesoria,Capacitacion,Chat,Cliente,
Contrato,ClienteContrato,Lista,Mejora,Perfil,Plan,Profesional,Reporte,
Servicio,TipoAsesoria,TipoReporte,User,Visita
)
from .serializers import (ActividadSerializer,AdministradorSerializer,AlertaSerializer,AsesoriaSerializer,
CapacitacionSerializer,ChatSerializer,ClienteSerializer,ContratoSerializer,ClienteContratoSerializer,
ListaSerializer,MejoraSerializer,PerfilSerializer,PlanSerializer,ProfesionalSerializer,
ReporteSerializer,ServicioSerializer,TipoAsesoriaSerializer,TipoReporteSerializer,UserSerializer,
VisitaSerializer
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

# mejoraSerializer

@api_view(['GET'])
def MejoraLista(request):
    act = Mejora.objects.all()
    serializer = MejoraSerializer(act, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def MejoraDetalles(request,pk):
    act = Mejora.objects.get(id_mejora=pk)
    serializer = MejoraSerializer(act, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def MejoraCrear(request):
    serializer = MejoraSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['PATCH'])
def MejoraModificar(request,pk):
    act = Mejora.objects.get(id_mejora=pk)
    data = request.data

    act.id_mejora = data.get("id_mejora", act.id_mejora)
    act.propuesta = data.get("propuesta", act.propuesta)
    act.aceptacion = data.get("aceptacion", act.aceptacion)
    act.pac = data.get("pac", act.pac)

    act.save()
    serializer = MejoraSerializer(act)
    return Response(serializer.data)


@api_view(['DELETE'])
def MejoraEliminar(request, pk):
    act = Mejora.objects.get(id_mejora=pk)
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

# PerfilSerializer
@api_view(['GET'])
def PerfilLista(request):
    act = Perfil.objects.all()
    serializer = PerfilSerializer(act, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def PerfilDetalles(request,pk):
    act = Perfil.objects.get(id_perfil=pk)
    serializer = PerfilSerializer(act, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def PerfilCrear(request):
    serializer = PerfilSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['PATCH'])
def PerfilModificar(request,pk):
    act = Perfil.objects.get(id_perfil=pk)
    data = request.data

    act.id_perfil = data.get("id_perfil", act.id_perfil)
    act.rut = data.get("rut", act.rut)
    act.telefono = data.get("telefono", act.telefono)
    act.direccion = data.get("direccion", act.direccion)
    act.tipo_perf = data.get("tipo_perf", act.tipo_perf)
    act.id_auth_user = data.get("id_auth_user", act.id_auth_user)

    act.save()
    serializer = PerfilSerializer(act)
    return Response(serializer.data)

@api_view(['DELETE'])
def PerfilEliminar(request, pk):
    act = Perfil.objects.get(id_perfil=pk)
    act.delete()
    return Response('Eliminado correctamente')

##########
##########
##########

# ReporteSerializer
@api_view(['GET'])
def ReporteLista(request):
    act = Reporte.objects.all()
    serializer = ReporteSerializer(act, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def ReporteDetalles(request,pk):
    act = Reporte.objects.get(id_reporte=pk)
    serializer = ReporteSerializer(act, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def ReporteCrear(request):
    serializer = ReporteSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['PATCH'])
def ReporteModificar(request,pk):
    act = Reporte.objects.get(id_reporte=pk)
    data = request.data

    act.id_reporte = data.get("id_reporte", act.id_reporte)
    act.cant_asesoria = data.get("cant_asesoria", act.cant_asesoria)
    act.cant_llamadas = data.get("cant_llamadas", act.cant_llamadas)
    act.cant_visitas = data.get("cant_visitas", act.cant_visitas)
    act.cant_accidentes = data.get("cant_accidentes", act.cant_accidentes)
    act.cant_multas = data.get("cant_multas", act.cant_multas)
    act.id_tipo_reporte = data.get("id_tipo_reporte", act.id_tipo_reporte)
    act.id_pac = data.get("id_pac", act.id_pac)

    act.save()
    serializer = ReporteSerializer(act)
    return Response(serializer.data)

@api_view(['DELETE'])
def ReporteEliminar(request, pk):
    act = Reporte.objects.get(id_reporte=pk)
    act.delete()
    return Response('Eliminado correctamente')

##########
##########
##########

# ChatSerializer
@api_view(['GET'])
def ChatLista(request):
    act = Chat.objects.all()
    serializer = ChatSerializer(act, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def ChatDetalles(request,pk):
    act = Chat.objects.get(id_chat=pk)
    serializer = ChatSerializer(act, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def ChatCrear(request):
    serializer = ChatSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['PATCH'])
def ChatModificar(request,pk):
    act = Reporte.objects.get(id_chat=pk)
    data = request.data

    act.id_chat = data.get("id_chat", act.id_chat)
    act.mensaje = data.get("mensaje", act.mensaje)
    act.fec_mensaje = data.get("fec_mensaje", act.fec_mensaje)
    act.enviado_por = data.get("enviado_por", act.enviado_por)
    act.cabecera = data.get("cabecera", act.cabecera)
    act.cant_multas = data.get("cant_multas", act.cant_multas)
    act.id_prof = data.get("id_prof", act.id_prof)
    act.id_cli = data.get("id_cli", act.id_cli)

    act.save()
    serializer = ChatSerializer(act)
    return Response(serializer.data)

@api_view(['DELETE'])
def ChatEliminar(request, pk):
    act = Chat.objects.get(id_chat=pk)
    act.delete()
    return Response('Eliminado correctamente')

##########
##########
##########