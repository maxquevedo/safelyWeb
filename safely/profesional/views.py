from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

from django.contrib import messages
from django.core.paginator import Paginator
from django.http import Http404

from app.models import *
from app.forms import *


# Create your views here.

#INICIO PREFESIONAL
@login_required
def home_professional(request):

    return render(request, 'profesional/home-profesional.html')


def test(request):

    return render(request, 'profesional/asesorias/test.html')


#MODIFICAR DATOS PROFESIONAL
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
def modificar_ase(request,id_asesoria):
    ase = Asesoria.objects.get(id_asesoria=id_asesoria)
    if request.method == 'GET':
        form = AsesoriaModificar(instance=ase)
    else:
        form = AsesoriaModificar(request.POST, instance=ase)
        if form.is_valid():
            form.save()
            messages.success(request, "Modificado correctamente")
        return redirect(to='lista_ase')

    return render(request, 'profesional/asesorias/modificar-a.html',{'form':form})



def crear_tipo_ase(request):
    data = {
        'form': TipoAsesoriaForm
    }
    if request.method == 'POST':
        formulario = TipoAsesoriaForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Creado correctamente!")
            return redirect (to='vista_asesorias')
        else:
            data["form"] = formulario 
    return render(request, 'profesional/asesorias/crear-tipo-a.html',data )


def lista_ase(request):
    ase = Asesoria.objects.all().order_by('id_asesoria')
    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(ase, 5)
        plan = paginator.page(page)
    except:
        raise Http404

    context = {'entity': ase,
                'paginator': paginator}
    return render(request, 'profesional/asesorias/lista-asesoria.html', context)

#######################################################################################################
## CAPACITACIONES
#######################################################################################################

@login_required
def vista_capacitacion(request):

    return render(request, 'profesional/capacitaciones/capacitaciones.html')



@login_required
def crear_capa(request):
    data = {
        'form': CapacitacionForm
    }
    if request.method == 'POST':
        formulario = CapacitacionForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Creado correctamente!")
            return redirect (to='vista_capacitacion')
        else:
            data["form"] = formulario 
    return render(request, 'profesional/capacitaciones/crear-c.html',data)

@login_required
def ingresar_capa(request):

    return render(request, 'profesional/capacitaciones/ingresar-c.html')

@login_required
def modificar_capa(request,id_capacitacion):
    capa = Capacitacion.objects.get(id_capacitacion=id_capacitacion)

    if request.method == 'GET':
        form = CapacitacionModificar(instance=capa)
    else:
        form = CapacitacionModificar(request.POST, instance=capa)
        if form.is_valid():
            form.save()
            messages.success(request, "Modificado correctamente")
        return redirect(to='lista_capa')

    return render(request, 'profesional/capacitaciones/modificar-c.html',{'form':form})


def lista_capa(request):
    ase = Capacitacion.objects.all().order_by('id_capacitacion')
    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(ase, 5)
        plan = paginator.page(page)
    except:
        raise Http404

    context = {'entity': ase,
                'paginator': paginator}
    return render(request, 'profesional/asesorias/lista-capacitacion.html', context)

#######################################################################################################
## CHECKLIST
#######################################################################################################

@login_required
def vista_checklist(request):

    return render(request, 'profesional/checklist/checklist.html')

@login_required
def crear_ch(request):
    data = {
        'form': ListaForm
    }
    if request.method == 'POST':
        formulario = ListaForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Creado correctamente!")
            return redirect (to='vista_checklist')
        else:
            data["form"] = formulario 
    return render(request, 'profesional/checklist/crear-ch.html',data)

@login_required
def ingresar_ch(request):

    return render(request, 'profesional/checklist/ingresar-ch.html')

@login_required
def modificar_ch(request):
    ase = Lista.objects.get(id_lista=id_lista)
    if request.method == 'GET':
        form = ListaForm(instance=ase)
    else:
        form = ListaForm(request.POST, instance=ase)
        if form.is_valid():
            form.save()
            messages.success(request, "Modificado correctamente")
        return redirect(to='vista_checklist')


    return render(request, 'profesional/checklist/modificar-ch.html')

def lista_ch(request):
    ase = Lista.objects.all().order_by('id_lista')
    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(ase, 5)
        plan = paginator.page(page)
    except:
        raise Http404

    context = {'entity': ase,
                'paginator': paginator}
    return render(request, 'profesional/asesorias/lista-ch.html', context)

##
#######################################################################################################
## MEJORAS

#######################################################################################################

@login_required
def vista_mejoras(request):

    return render(request, 'profesional/mejoras/mejoras.html')

@login_required
def revisar_me(request):

    return render(request, 'profesional/mejoras/revisar-me.html')


def crear_me(request):
    data = {
        'form': MejorasForm
    }
    if request.method == 'POST':
        formulario = MejorasForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Creado correctamente!")
            return redirect (to='vista_mejoras')
        else:
            data["form"] = formulario 
    return render(request, 'profesional/asesorias/crear-me.html',data )





