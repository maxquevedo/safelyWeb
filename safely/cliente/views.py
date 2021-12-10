from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from.forms import ClienteProfileUpdate,ClienteUpdate,ClientUserUpdate
from app.forms import *
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http.response import Http404
from django.core.paginator import Paginator
from app.models import *

from django.views.generic.list import ListView
from django.utils.decorators import method_decorator

from datetime import date

from app.views import groups_only

@method_decorator(groups_only('Cliente'), name='dispatch')
class home_cliente(ListView):
    template_name = 'cliente/home-cliente.html'

    def get_queryset(self):
        user = self.request.user
        perfil = Perfil.objects.get(id_auth_user = user.id)
        cliente = Cliente.objects.get(id_perfil = perfil.id_perfil)
        actividad= Actividad.objects.all().filter(id_cli = cliente.id_cli)
        querySet = actividad
        return querySet


@groups_only('Cliente')
def datosUser(request):
    id_user = request.user.id
    usuario = Perfil.objects.get(id_auth_user = id_user)
    perfil = Perfil.objects.get(id_perfil=usuario.id_perfil)
    cliente = Cliente.objects.get(id_perfil = perfil.id_perfil)


    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        form_p = ClienteProfileUpdate(request.POST, instance=perfil)
        form_c = ClienteUpdate(request.POS, instance= cliente)
        if u_form.is_valid():
            u_form.save()
        if form_p.is_valid():
            form_p.save()
        if form_c.is_valid():
            form_c.save()
    else:
        u_form = UserUpdateForm(instance=request.user)
        form_p = ClienteProfileUpdate(instance=perfil)
        form_c = ClienteUpdate(instance= cliente)
    context = {
        'u_form': u_form,
        'form_p':form_p,
        'form_c':form_c,
    }
    return render(request,'cliente/perfil.html',context)

@groups_only('Cliente')
def actividades(request):
    id_usuario = request.user.id
    cli = Cliente.objects.get(id_perfil=Perfil.objects.get(id_auth_user=id_usuario))
    id_cliente = cli.id_cli
    try:
        ACT = Actividad.objects.filter(id_cli=id_cliente)
    except:
        ACT = Actividad.objects.none()
        
    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(ACT, 5)
        ACT = paginator.page(page)
    except:
        raise Http404
    context = {'entity': ACT,
                'paginator': paginator}
    return render(request, 'cliente/actividades.html', context)


@groups_only('Cliente')
def boleta(request):
    id_usuario = request.user.id
    cli = Cliente.objects.get(id_perfil=Perfil.objects.get(id_auth_user=id_usuario))
    id_cliente = cli.id_cli # Recibe la id del cliente correctamente
    contr=Contrato.objects.all().filter(id_cli = id_cliente) # recibe todos los contratos con ese cliente 

    try:
        bol = Boleta.objects.filter(id_contrato__in = contr) # todos los contratos(del cliente) listan sus boletas    
    except:
        bol = Boleta.objects.none()
    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(bol, 5)
        bol = paginator.page(page)
    except:
        raise Http404


    context = {'entity': bol,
                'paginator': paginator}  

    return render(request, 'cliente/boleta.html',context)
@groups_only('Cliente')
def lista(request):
    return render(request, 'cliente/lista.html')

