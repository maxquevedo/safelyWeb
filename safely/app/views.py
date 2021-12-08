from .models import *
from .forms import *
from app import filtersets

import cx_Oracle

from django.http.response import Http404
from django.shortcuts import render, redirect
from django.contrib.auth import  login

from django.contrib.auth.forms import  AuthenticationForm

from django.contrib.auth.models import  User

from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import Http404

from django.db import connection

def crear_grupo(request):
    data = {
        'form': GrupoForm
    }
    if request.method == 'POST':
        formulario = GrupoForm(data=request.POST)
        if formulario.is_valid():
            gru = formulario.save()
            messages.success(request, "Grupo "+gru.name+" creado correctamente!")
            return redirect (to='mantenedor-usr')
        else:
            data["form"] = formulario 
    return render(request, 'registration/group.html',data )



def user_filter(request):
    # https://www.youtube.com/watch?v=dkJ3uqkdCcY
    #https://django-filter.readthedocs.io/en/stable/index.html
    """
    filtro = filtersets.UsertFilter(
        request.GET,
        queryset= User.objects.all()
    )

    PerfilF = filtersets.PerfilFilter(
        request.GET,
        queryset= Perfil.objects.all()
    )
    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(PerfilF, 5)
        PerfilF = paginator.page(page)
    except:
        raise Http404
    context = {
        'filtro': filtro,
        'entity':PerfilF,
        'paginator': paginator
    }
    """

    filtro = filtersets.UsertFilter(
        request.GET,
        queryset= User.objects.all()
    )

    PerfilF = filtersets.PerfilFilter(
        request.GET,
        queryset= Perfil.objects.all()
    )
    context = {
        'filtro': filtro,
        'PerfilF':PerfilF,
    }
    return render(request, 'pruebas/ekisde.html', context)


def signup_view(request):
    context = {'form': CustomUserCreationForm(),
    'form_p':PerfilForm(),
    'adminform':AdminForm(),
    'proform': ProfesionalForm(),
    'cliform': ClienteForm(),
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        formPerfil = PerfilForm(data=request.POST)
        formAdm = AdminForm(data=request.POST)
        formProf = ProfesionalForm(data=request.POST)
        formCli = ClienteForm(data=request.POST)

        if formulario.is_valid() and formPerfil.is_valid():
            usuario = formulario.save()
            group = request.POST.get('groups')
            usuario.groups.add(group)

            perfil = formPerfil.save(commit=False)    
            perfil.id_auth_user = usuario
            perfil.save()
            
            if perfil.tipo_perf=='1':
                admin = formAdm.save(commit=False)
                admin.id_perfil = perfil
                admin.save()
            elif perfil.tipo_perf=='2':
                prof = formProf.save(commit=False)
                prof.id_perfil = perfil
                prof.save()
            elif perfil.tipo_perf=='3':
                cli = formCli.save(commit=False)
                cli.id_perfil =perfil
                cli.save()

            messages.success(request, 'Usuario '+usuario.username+' creado correctamente')
            return redirect(to="mantenedor")
        context = {'form': CustomUserCreationForm(),
        'form_p':PerfilForm(),
        'adminform':AdminForm(),
        'proform':ProfesionalForm(),
        'cliform': ClienteForm(),
        }

    return render(request, 'registration/signup.html', context)


def home(request):
    return render(request, 'home.html')


    

def home_admin(request):
    usuario = User.objects.all().order_by('id')
    context = {'usuario': usuario }
    return render(request,'administrador/home-adm.html', context)

def maintainer(request):
    return render(request, 'administrador/mantenedor.html')

def maintainer_user(request):
    return render(request, 'administrador/mantenedor-usuario.html')

def maintainer_plan(request):
    return render(request, 'administrador/mantenedor-plan.html')

def maintainer_service(request):
    return render(request, 'administrador/mantenedor-servicio.html')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect(to='home-adm')
    else:
            form = AuthenticationForm()
    return render(request,'registration/login.html',{'form':form})

def login_filter(request):
    if request.user.groups.filter(name="Administrador") or request.user.is_staff:
        return redirect(to='home-adm')
    elif request.user.groups.filter(name="Profesional"):
        return redirect(to='home-prof')
    else:
        return redirect(to='home-cliente')

#mantenedor 
@permission_required('app.view_user')
def UserLista(request):
    usuario = User.objects.all().order_by('id')
    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(usuario, 5)
        usuario = paginator.page(page)
    except:
        raise Http404

    context = {'entity': usuario,
                'paginator': paginator}
    return render(request, 'administrador/lista.html', context)

@permission_required('app.change_user')
def UserEdit(request,id):
    usuario = User.objects.get(id=id)
   
    if request.method == 'GET':
        form = UserUpdateForm(instance=usuario)   
    else:
        form = UserUpdateForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            messages.success(request, "Usuario "+usuario.username+" modificado correctamente")
        return redirect(to="listar")
    context = {
            'form':form,
        }  
    return render(request,'administrador/editar.html', context)

@permission_required('app.delete_user')
def UserDelete(request,id):
    usuario = User.objects.get(id=id)
    usuario.is_active = 0
    if request.method == 'POST':
        form = UserActive(instance=usuario)
    else:
        form = UserActive(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            messages.success(request, "Usuario desactivado correctamente")
    return redirect(to="listar")

def UserActivate(request,id):
    usuario = User.objects.get(id=id)
    if request.method == 'POST':
        form = UserActive(instance=usuario)
    else:
        form = UserActive(request.POST, instance=usuario)
        if form.is_valid():
            user = form.save()
            user.is_active = True
            user.save()
            messages.success(request, "Usuario activado correctamente")
    return redirect(to="listar")

##PLAN
def PlanCreate(request):
    data = {
        'form': PlanForm
    }

    if request.method == 'POST':
        formulario = PlanForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Plan creado correctamente!")
            return redirect (to='mantenedor')
        else:
            data["form"] = formulario       
    return render(request, 'administrador/planes/agregar-plan.html', data)

def plan_lista(request):
    plan = Plan.objects.all().order_by('id_plan')
    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(plan, 5)
        plan = paginator.page(page)
    except:
        raise Http404

    context = {'entity': plan,
                'paginator': paginator}
    return render(request, 'administrador/planes/lista-plan.html', context)

def PlanEdit(request,id_plan):
    plan = Plan.objects.get(id_plan=id_plan)
    if request.method == 'GET':
        form = PlanUpdateForm(instance=plan)
    else:
        form = PlanUpdateForm(request.POST, instance=plan)
        if form.is_valid():
            form.save()
            messages.success(request, "Plan modificado correctamente")
        return redirect(to='lista-plan')
    return render(request,'administrador/planes/editar-plan.html',{'form':form})


def PlanDelete(request,id):
    plan = Plan.objects.get(id_plan=id)
    plan.estado = 0
    if request.method == 'POST':
        form = PlanActive(instance=plan)
    else:
        form = PlanActive(request.POST, instance=plan)
        if form.is_valid():
            form.save()
            messages.success(request, "Plan desactivado correctamente")
    return redirect(to="lista-plan")

def PlanActivate(request,id):
    plan = Plan.objects.get(id_plan=id)
    if request.method == 'POST':
        form = PlanActive(instance=plan)
    else:
        form = PlanActive(request.POST, instance=plan)
        if form.is_valid():
            plan = form.save()
            plan.estado = 1
            plan.save()
            messages.success(request, "Plan activado correctamente")
    return redirect(to="lista-plan")

##SERVICIOS

def ServicioCreate(request):
    data = {
        'form': ServicioForm
    }

    if request.method == 'POST':
        formulario = ServicioForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Servicio creado correctamente!")
            return redirect (to='mantenedor')
        else:
            data["form"] = formulario       
    return render(request, 'administrador/servicios/agregar-servicio.html', data)

def Servicio_lista(request):
    servicio = Servicio.objects.all().order_by('id_servicio')
    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(servicio, 5)
        servicio = paginator.page(page)
    except:
        raise Http404

    context = {'entity': servicio,
                'paginator': paginator}
    return render(request, 'administrador/servicios/lista-servicio.html', context)

def ServicioEdit(request,id_servicio):
    servicio = Servicio.objects.get(id_servicio=id_servicio)
    if request.method == 'GET':
        form = ServicioUpdateForm(instance=servicio)
    else:
        form = ServicioUpdateForm(request.POST, instance=servicio)
        if form.is_valid():
            form.save()
            messages.success(request, "Servicio modificado correctamente")
        return redirect(to='lista-servicios')
    return render(request,'administrador/servicios/editar-servicio.html',{'form':form})



def ServicioDelete(request,id):
    serv = Servicio.objects.get(id_servicio=id)
    serv.estado = 0
    if request.method == 'POST':
        form = ServicioActive(instance=serv)
    else:
        form = ServicioActive(request.POST, instance=serv)
        if form.is_valid():
            form.save()
            messages.success(request, "Servicio desactivado correctamente")
    return redirect(to="lista-servicios")

def ServicioActivate(request,id):
    serv = Servicio.objects.get(id_servicio=id)
    if request.method == 'POST':
        form = ServicioActive(instance=serv)
    else:
        form = ServicioActive(request.POST, instance=serv)
        if form.is_valid():
            serv = form.save()
            serv.estado = 1
            serv.save()
            messages.success(request, "Servicio activado correctamente")
    return redirect(to="lista-servicios")


#informacion de clientes ClienteForm
def cliente_datos():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor() #Este llama
    out_cur = django_cursor.connection.cursor() # este recive
    cursor.callproc("sp_listar_datos_cliente",[out_cur])
    lista =[]
    for fila in out_cur:
        lista.append(fila)
    return lista

@login_required
def infoCliente(request):

    cliente = cliente_datos()
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(cliente, 5)
        cliente = paginator.page(page)
    except:
        raise Http404
    context = {'entity': cliente,
                'paginator': paginator,
                }
    return render(request, 'administrador/info_cliente/info-cliente.html',context)
    

#informacion de clientes ProfesionalForm
@login_required
def infoProfesional(request):
    pro = Profesional.objects.all().order_by('id_prof')
    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(pro, 5)
        pro = paginator.page(page)
    except:
        raise Http404
    context = {'entity': pro,
                'paginator': paginator}   
    return render(request, 'administrador/info_profesional/info-profesional.html',context)


#informacion de perfiles 

@login_required
def infoPerfil(request):

    PerfilF = filtersets.PerfilFilter(request.GET,queryset= Perfil.objects.all())
    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(PerfilF, 5)
        PerfilF = paginator.page(page)
    except:
        """raise Http404"""
    context = {
        'entity':PerfilF,
        'paginator': paginator
    }
    return render(request, 'administrador/info_perfil/info-perfil.html', context)


@login_required
def modificar_perfil(request,id_perfil):
    perfil = Perfil.objects.get(id_perfil=id_perfil)

    if request.method == 'GET':
        form = PerfilModificar(instance=perfil)
    else:
        form = PerfilModificar(request.POST, instance=perfil)
        if form.is_valid():
            form.save()
            messages.success(request,"Perfil de "+perfil.id_auth_user.first_name+" "+perfil.id_auth_user.last_name+" modificado correctamente!")
        return redirect(to='infoPerfil')
    context = {
        'form':form

    }
    return render(request, 'administrador/info_perfil/modificar-perfil.html',context)


"""
Utilizando procedures
"""

def lista_actividades():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor() #Este llama
    out_cur = django_cursor.connection.cursor() # este recive
    cursor.callproc("sp_listar_actividades",[out_cur])
    lista =[]
    for fila in out_cur:
        lista.append(fila)
    return lista

def lista_capacitacion():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor() #Este llama
    out_cur = django_cursor.connection.cursor() # este recive
    cursor.callproc("sp_listar_capacitacion",[out_cur])
    lista =[]
    for fila in out_cur:
        lista.append(fila)
    return lista

def lista_asesoria():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor() #Este llama
    out_cur = django_cursor.connection.cursor() # este recive
    cursor.callproc("sp_listar_asesoria",[out_cur])
    lista =[]
    for fila in out_cur:
        lista.append(fila)
    return lista

def lista_visita():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor() #Este llama
    out_cur = django_cursor.connection.cursor() # este recive
    cursor.callproc("sp_listar_visita",[out_cur])
    lista =[]
    for fila in out_cur:
        lista.append(fila)
    return lista

def lista_cliente():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor() #Este llama
    out_cur = django_cursor.connection.cursor() # este recive
    cursor.callproc("sp_listar_cliente",[out_cur])
    lista =[]
    for fila in out_cur:
        lista.append(fila)
    return lista
def lista_profesional():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor() #Este llama
    out_cur = django_cursor.connection.cursor() # este recive
    cursor.callproc("sp_listar_profesional",[out_cur])
    lista =[]
    for fila in out_cur:
        lista.append(fila)
    return lista

def guardar_actividad(nombre,descripcion,tipo_act,fec_estimada,estado,id_cli,id_prof):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor() #Este llama
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('sp_agregar_actividad_corta',[nombre,descripcion,tipo_act,fec_estimada,estado,id_cli,id_prof, salida])
    return salida.getvalue()

# actividades
@login_required
def actividades(request):

    actividad = lista_actividades()
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(actividad, 5)
        actividad = paginator.page(page)
    except:
        raise Http404
    context = {'entity': actividad,
                'paginator': paginator,
                }
    return render(request, 'administrador/actividades/actividades_lista.html',context)




@login_required
def crear_actividad(request):
    #print(request.user.username)

    capacitacion = lista_capacitacion()
    asesoria = lista_asesoria()
    visita = lista_visita()
    cliente = Cliente.objects.all()
    profesional = Profesional.objects.all()
    data = {
                'capacitacion':capacitacion,
                'asesoria':asesoria,
                'visita':visita,
                'cliente':cliente,
                'profesional':profesional
                }

    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        descripcion =request.POST.get('descripcion')
        tipo_act = request.POST.get('tipo_act')
        fec_estimada = request.POST.get('fec_estimada')
        estado = request.POST.get('estado')
        id_cli = request.POST.get('id_cli')
        id_prof = request.POST.get('id_prof')
        salida = guardar_actividad(nombre,descripcion,tipo_act,fec_estimada,estado,id_cli,id_prof)
        if salida == 1:
            data['mensaje'] = 'Agregado Correctamente'
            return redirect(to='actividades')
        else:
            data['mensaje'] = 'No se a podido guardar'
    return render(request, 'administrador/actividades/crear.html',data)

@login_required
def actualizar_actividad(request,id_actividad):
    act = Actividad.objects.get(id_actividad=id_actividad)

    if request.method == 'GET':
        form = ActualizarActividad(instance=act)
    else:
        form = ActualizarActividad(request.POST, instance=act)
        if form.is_valid():
            form.save()
            messages.success(request, "Actividad modificada correctamente")
        return redirect(to='actividades')

    context = {'form':form}
    return render(request, 'administrador/actividades/actualizar.html',context)


def checklist(request):
    data = {
        'form': listaForm
    }

    if request.method == 'POST':
        formulario = listaForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Creado correctamente!")
        else:
            data["form"] = formulario       
    return render(request, 'administrador/checklist/checklist.html', data)


def listaCheck(request):
    lista = CliCheckPro.objects.all().order_by('id_clicheck')
    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(lista, 5)
        lista = paginator.page(page)
    except:
        raise Http404

    context = {'entity': lista,
                'paginator': paginator}
    return render(request, 'administrador/checklist/listado.html', context)

def modificaCheck(request,id_clicheck):
    lista = CliCheckPro.objects.get(id_clicheck=id_clicheck)
    if request.method == 'GET':
        form = listaForm(instance=lista)
    else:
        form = listaForm(request.POST, instance=lista)
        if form.is_valid():
            form.save()
            messages.success(request, "Modificado correctamente")
        return redirect(to='listaCheck')
    return render(request,'administrador/checklist/modificar.html',{'form':form})