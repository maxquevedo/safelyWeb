from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from.forms import ClienteProfileUpdate,ClienteUpdate,ClientUserUpdate
from app.forms import *
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http.response import Http404
from django.core.paginator import Paginator
from app.models import *

@login_required
def home_cliente(request):

    return render(request, 'cliente/home-cliente.html')

@login_required
def datosUser(request):
    id_user = request.user.id
    usuario = Perfil.objects.get(id_auth_user = id_user)
    perfil = Perfil.objects.get(id_perfil=usuario.id_perfil)

    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        form_p = ClienteProfileUpdate(request.POST, instance=perfil)
        if u_form.is_valid():
            u_form.save()
        if form_p.is_valid():
            form_p.save()
    else:
        u_form = UserUpdateForm(instance=request.user)
        form_p = ClienteProfileUpdate(instance=perfil)
    context = {
        'u_form': u_form,
        'form_p':form_p,
    }
    return render(request,'cliente/perfil.html',context)


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


@login_required
def boleta(request):
    id_usuario = request.user.id
    try:
        cliente = Cliente.objects.get(id_perfil=Perfil.objects.get(id_auth_user=id_usuario))
        contrato = Contrato.objects.get(id_cli = cliente.id_cli)
        print(contrato.id_contrato)
        bol = Boleta.objects.filter(id_contrato=contrato.id_contrato)
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

def lista(request):
    return render(request, 'cliente/lista.html')

