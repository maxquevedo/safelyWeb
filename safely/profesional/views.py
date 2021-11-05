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
def lista_ase(request):
    ase = Asesoria.objects.all().order_by('id_asesoria')
    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(ase, 5)
        ase = paginator.page(page)
    except:
        raise Http404
    context = {'entity': ase,
                'paginator': paginator}
    return render(request, 'profesional/asesorias/asesoria.html', context)


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
            return redirect (to='lista_ase')
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

@login_required
def crear_tipo_ase(request):
    data = {
        'form': TipoAsesoriaForm
    }
    if request.method == 'POST':
        formulario = TipoAsesoriaForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Creado correctamente!")
            return redirect (to='lista_ase')
        else:
            data["form"] = formulario 
    return render(request, 'profesional/asesorias/crear-tipo-a.html',data )



#######################################################################################################
## CAPACITACIONES
#######################################################################################################
@login_required
def lista_capa(request):
    capa = Capacitacion.objects.all().order_by('id_capacitacion')
    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(capa, 5)
        capa = paginator.page(page)
    except:
        raise Http404

    context = {'entity': capa,
                'paginator': paginator}
    return render(request, 'profesional/capacitaciones/capacitaciones.html', context)


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
            return redirect (to='lista_capa')
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



#######################################################################################################
## CHECKLIST
#######################################################################################################

@login_required
def lista_ch(request):
    CH = Lista.objects.all().order_by('id_lista')
    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(CH, 5)
        CH = paginator.page(page)
    except:
        raise Http404

    context = {'entity': CH,
                'paginator': paginator}
    return render(request, 'profesional/checklist/checklist.html', context)


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
            return redirect (to='lista_ch')
        else:
            data["form"] = formulario 
    return render(request, 'profesional/checklist/crear-ch.html',data)

@login_required
def ingresar_ch(request):

    return render(request, 'profesional/checklist/ingresar-ch.html')

@login_required
def modificar_ch(request,id_lista):
    lis = Lista.objects.get(id_lista=id_lista)

    if request.method == 'GET':
        form = ListaForm(instance=lis)
    else:
        form = ListaForm(request.POST, instance=lis)
        if form.is_valid():
            form.save()
            messages.success(request, "Modificado correctamente")
        return redirect(to='lista_ch')

    return render(request, 'profesional/checklist/modificar-ch.html',{'form':form})

##
#######################################################################################################
## MEJORAS

#######################################################################################################

@login_required
def vista_mejoras(request):
    me = Mejoras.objects.all().order_by('id_mejora')
    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(me, 5)
        me = paginator.page(page)
    except:
        raise Http404
    context = {'entity': me,
                'paginator': paginator}
    return render(request, 'profesional/mejoras/mejoras.html', context)


@login_required
def revisar_me(request):

    return render(request, 'profesional/mejoras/revisar-me.html')

@login_required
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
    return render(request, 'profesional/mejoras/crear-me.html',data )



#######################################################################################################
## ACTIVIDAD

#######################################################################################################


@login_required
def vista_actividad(request):
    ACT = Actividad.objects.all().order_by('id_actividad')
    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(ACT, 5)
        ACT = paginator.page(page)
    except:
        raise Http404
    context = {'entity': ACT,
                'paginator': paginator}
    return render(request, 'profesional/actividad/actividad.html', context)

@login_required
def crear_actividad(request):
    data = {
        'form': ActividadForm
    }
    if request.method == 'POST':
        formulario = ActividadForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Creado correctamente!")
            return redirect (to='vista_actividad')
        else:
            data["form"] = formulario 
    return render(request, 'profesional/actividad/crear-act.html',data )

@login_required
def modificar_actividad(request,id_actividad):
    ACT = Actividad.objects.get(id_actividad=id_actividad)

    if request.method == 'GET':
        form = ActividadForm(instance=ACT)
    else:
        form = ActividadForm(request.POST, instance=ACT)
        if form.is_valid():
            form.save()
            messages.success(request, "Modificado correctamente")
        return redirect(to='vista_actividad')

    return render(request, 'profesional/actividad/modificar-act.html',{'form':form})


#######################################################################################################
## VISITA

#######################################################################################################
@login_required
def vista_visita(request):
    vis = Visita.objects.all().order_by('id_visita')
    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(vis, 5)
        vis = paginator.page(page)
    except:
        raise Http404
    context = {'entity': vis,
                'paginator': paginator}
    return render(request, 'profesional/visita/visita.html', context)

@login_required
def crear_visita(request):
    data = {
        'form': VisitaForm
    }
    if request.method == 'POST':
        formulario = VisitaForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Creado correctamente!")
            return redirect (to='vista_visita')
        else:
            data["form"] = formulario 
    return render(request, 'profesional/visita/crear-vista.html',data )


@login_required
def modificar_visita(request,id_visita):
    vis = Visita.objects.get(id_visita=id_visita)

    if request.method == 'GET':
        form = VisitaForm(instance=vis)
    else:
        form = VisitaForm(request.POST, instance=vis)
        if form.is_valid():
            form.save()
            messages.success(request, "Modificado correctamente")
        return redirect(to='vista_visita')

    return render(request, 'profesional/visita/modificar-visita.html',{'form':form})