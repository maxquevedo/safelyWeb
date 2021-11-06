from django.http.response import Http404
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import (
CustomUserCreationForm, UserActive,UserUpdateForm, PlanUpdateForm, PlanForm,ServicioForm,ServicioUpdateForm,
ClienteForm,ProfesionalForm

)
from django.contrib.auth.forms import  AuthenticationForm
from rest_framework import viewsets

from django.contrib.auth.models import Group, User
from .models import ( Perfil, 
Administrador, Profesional, Cliente,
Servicio, Plan, Contrato, 
Alerta,
Lista,Mejoras,
Reporte,TipoReporte,
Actividad, Capacitacion,Asesoria,Visita
)
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import Http404

def home(request):
    return render(request, 'home.html')

def signup_view(request):
    data = {
        'form': CustomUserCreationForm()
    }
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            usuario = formulario.save()
            group = request.POST.get('groups')
            usuario.groups.add(group)
            messages.success(request, 'Usuario creado correctamente')
            return redirect(to="mantenedor")
        data["form"] = formulario
    return render(request, 'registration/signup.html', data)
    
@login_required
def home_professional(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        if u_form.is_valid():
            u_form.save()
    else:
        u_form = UserUpdateForm(instance=request.user)
    context = {
        'u_form': u_form,
    }

    return render(request, 'profesional/home-profesional.html', context)

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
    if request.user.groups.filter(name="Administrador"):
        return redirect(to='home-adm')
    elif request.user.groups.filter(name="Profesional"):
        return redirect(to='home-prof')
    else:
        return redirect(to='home')

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
            messages.success(request, "Usuario modificado correctamente")
        return redirect(to="listar")
    return render(request,'administrador/editar.html',{'form':form})

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
    plan.delete()
    messages.success(request, "Plan eliminado correctamente")
    return redirect(to='lista-plan')

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
    servicio = Servicio.objects.get(id_servicio=id)
    servicio.delete()
    messages.success(request, "Servicio eliminado correctamente")
    return redirect(to='lista-servicios')


#informacion de clientes ClienteForm

@login_required
def infoCliente(request):
    cli = Cliente.objects.all().order_by('id_cli')
    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(cli, 5)
        cli = paginator.page(page)
    except:
        raise Http404
    context = {'entity': cli,
                'paginator': paginator}   
    return render(request, 'administrador/info_cliente/info-cliente.html',context)

@login_required
def crear_cliente(request):
    data = {
        'form': ClienteForm
    }
    if request.method == 'POST':
        formulario = ClienteForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Creado correctamente!")
            return redirect (to='infoCliente')
        else:
            data["form"] = formulario 
    return render(request, 'administrador/info_cliente/crear-cliente.html',data )


@login_required
def modificar_cliente(request,id_cli):
    cli = Cliente.objects.get(id_cli=id_cli)
    if request.method == 'GET':
        form = ClienteForm(instance=cli)
    else:
        form = ClienteForm(request.POST, instance=cli)
        if form.is_valid():
            form.save()
            messages.success(request, "Modificado correctamente")
        return redirect(to='infoCliente')
    return render(request, 'administrador/info_cliente/modificar-cliente.html',{'form':form})

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


@login_required
def crear_profesional(request):
    data = {
        'form': ProfesionalForm
    }
    if request.method == 'POST':
        formulario = ProfesionalForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Creado correctamente!")
            return redirect (to='infoProfesional')
        else:
            data["form"] = formulario 
    return render(request, 'administrador/info_profesional/crear-profesional.html',data )

@login_required
def modificar_profesional(request,id_prof):
    pro = Profesional.objects.get(id_prof=id_prof)
    if request.method == 'GET':
        form = ClienteForm(instance=pro)
    else:
        form = ClienteForm(request.POST, instance=pro)
        if form.is_valid():
            form.save()
            messages.success(request, "Modificado correctamente")
        return redirect(to='infoProfesional')
    return render(request, 'administrador/info_profesional/modificar-profesional.html',{'form':form})