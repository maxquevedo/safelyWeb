from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

from django.contrib import messages
from django.core.paginator import Paginator
from django.http import Http404

from app.models import *
from app.forms import *

# Create your views here.
@login_required
def home_professional(request):

    return render(request, 'profesional/home-profesional.html')


@login_required
def datos_pro(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        if u_form.is_valid():
            u_form.save()
    else:
        u_form = UserUpdateForm(instance=request.user)
    context = {
        'u_form': u_form,
    }

    return render(request,'profesional/datos-pro.html',context)

#######################################################################################################
## ASESORIAS
#######################################################################################################

@login_required
def vista_asesorias(request):

    return render(request, 'profesional/asesorias/asesoria.html')

@login_required
def crear_ase(request):
    data = {
        'form': AsesoriaForm
    }
    if request.method == 'POST':
        formulario = AsesoriaForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Creado correctamente!")
            return redirect (to='vista_asesorias')
        else:
            data["form"] = formulario  
    return render(request, 'profesional/asesorias/crear-a.html',data)

@login_required
def ingresar_ase(request):

    return render(request, 'profesional/asesorias/ingresar-a.html')

@login_required
def modificar_ase(request):
    return render(request, 'profesional/asesorias/modificar-a.html')


#######################################################################################################
## CAPACITACIONES
#######################################################################################################

@login_required
def vista_capacitacion(request):

    return render(request, 'profesional/capacitaciones/capacitaciones.html')

@login_required
def crear_capa(request):

    return render(request, 'profesional/capacitaciones/crear-c.html')

@login_required
def ingresar_capa(request):

    return render(request, 'profesional/capacitaciones/ingresar-c.html')

@login_required
def modificar_capa(request):

    return render(request, 'profesional/capacitaciones/modificar-c.html')


#######################################################################################################
## CHECKLIST
#######################################################################################################

@login_required
def vista_checklist(request):

    return render(request, 'profesional/checklist/checklist.html')

@login_required
def crear_ch(request):

    return render(request, 'profesional/checklist/crear-ch.html')

@login_required
def ingresar_ch(request):

    return render(request, 'profesional/checklist/ingresar-ch.html')

@login_required
def modificar_ch(request):

    return render(request, 'profesional/checklist/modificar-ch.html')

#######################################################################################################
## MEJORAS
#######################################################################################################

@login_required
def vista_mejoras(request):

    return render(request, 'profesional/mejoras/mejoras.html')

@login_required
def revisar_me(request):

    return render(request, 'profesional/mejoras/revisar-me.html')

@login_required
def ingresar_me(request):

    return render(request, 'profesional/mejoras/ingresar-me.html')







