from django.db.models import query
from django.http.response import HttpResponseRedirect
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

from django.contrib import messages
from django.core.paginator import Paginator
from django.http import Http404

from app.models import *
from app.forms import *

from django.views.generic.list import ListView
from django.utils.decorators import method_decorator


from app.views import groups_only



# Create your views here.

#INICIO PREFESIONAL

#def home_professional(request):
#    return render(request, 'profesional/home-profesional.html')

@method_decorator(groups_only('Profesional'), name='dispatch')
class home_professional(ListView):
    model = Actividad
    template_name = 'profesional/home-profesional.html'

    def get_queryset(self):
        user = self.request.user
        perfil = Perfil.objects.get(id_auth_user = user.id)
        profesional = Profesional.objects.get(id_perfil = perfil.id_perfil)
        actividad= Actividad.objects.all().filter(id_prof = profesional.id_prof)
        print(actividad)
        querySet = actividad
        return querySet


#MODIFICAR DATOS PROFESIONAL
@groups_only('Profesional')
def datos_pro(request):
    id_user = request.user.id
    usuario = Perfil.objects.get(id_auth_user = id_user)
    perfil = Perfil.objects.get(id_perfil=usuario.id_perfil)

    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        form_p = PerfilModificar(request.POST, instance=perfil)
        if u_form.is_valid():
            u_form.save()
        if form_p.is_valid():
            form_p.save()
    else:
        u_form = UserUpdateForm(instance=request.user)
        form_p = PerfilModificar( instance=perfil)
    context = {
        'u_form': u_form,
        'form_p':form_p,
    }
    return render(request,'profesional/datos-pro.html',context)

#######################################################################################################
## ASESORIAS
#######################################################################################################


@groups_only('Profesional')
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


@groups_only('Profesional')
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

@groups_only('Profesional')
def ingresar_ase(request):
    data = {
        'form': IngresarAsesoria
    }
    if request.method == 'POST':
        formulario = IngresarAsesoria(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Creado correctamente!")
            return redirect (to='vista_actividad')
        else:
            data["form"] = formulario 
    return render(request, 'profesional/asesorias/ingresar-a.html',data)

@groups_only('Profesional')
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

@groups_only('Profesional')
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

def DesactivarAse(request,id_asesoria):
    ase = Asesoria.objects.get(id_asesoria=id_asesoria)
    ase.estado = 0
    if request.method == 'POST':
        form = DesactivarAseForm(instance=ase)
    else:
        form = DesactivarAseForm(request.POST, instance=ase)
        if form.is_valid():
            form.save()
            messages.success(request, "Asesoría desactivada correctamente")
    return redirect(to="lista_ase")

def ActivarAse(request,id_asesoria):
    ase = Asesoria.objects.get(id_asesoria=id_asesoria)
    if request.method == 'POST':
        form = DesactivarAseForm(instance=ase)
    else:
        form = DesactivarAseForm(request.POST, instance=ase)
        if form.is_valid():
            ase = form.save()
            ase.estado = 1
            ase.save()
            messages.success(request, "Asesoría activada correctamente")
    return redirect(to="lista_ase")


#######################################################################################################
## CAPACITACIONES
#######################################################################################################
@groups_only('Profesional')
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


@groups_only('Profesional')
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

@groups_only('Profesional')
def ingresar_capa(request):
    data = {
        'form': IngresarCapacitacion
    }
    if request.method == 'POST':
        formulario = IngresarCapacitacion(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Creado correctamente!")
            return redirect (to='vista_actividad')
        else:
            data["form"] = formulario 
    return render(request, 'profesional/capacitaciones/ingresar-c.html', data)

@groups_only('Profesional')
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
@groups_only('Profesional')
def ver_check_cli(request):
    id_usuario = request.user.id

    try:
        pro = Profesional.objects.get(id_perfil=Perfil.objects.get(id_auth_user=id_usuario))

        clicheck = CliCheckPro.objects.filter(id_prof = pro)
    except:
        clicheck = CliCheckPro.objects.none()

    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(clicheck, 5)
        clicheck = paginator.page(page)
    except:
        raise Http404
    context = {'entity': clicheck,
                'paginator': paginator}
    return render(request, 'profesional/checklist/home-check.html',context)

@groups_only('Profesional')
def ver_checklist(request, id_clicheck):
    id_usuario = request.user.id

    try:
        checklist = Checklist.objects.filter(id_clicheck=id_clicheck).order_by('id_check')
    except:
        checklist = Checklist.objects.none()

    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(checklist, 10)
        checklist = paginator.page(page)
    except:
        raise Http404
    context = {'entity': checklist,
                'paginator': paginator}
    return render(request, 'profesional/checklist/checklist.html',context)

@groups_only('Profesional')
def añadir_item_check(request, id_clicheck):
    data = {
        'form': ChecklistForm(initial={'id_clicheck': id_clicheck})
    }
    if request.method == 'POST':
        formulario = ChecklistForm(data=request.POST, initial={'id_clicheck': id_clicheck})
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Creado correctamente!")
            return redirect (to='home-check')
        else:
            data["form"] = formulario 
    return render(request, 'profesional/checklist/crear-ITEM.html',data )

@groups_only('Profesional')
def desverificar_check(request, id_check):
    check = Checklist.objects.get(id_check=id_check)
    check.verificacion = 0
    if request.method == 'POST':
        form = ChecklistVerificador(instance=check)
    else:
        form = ChecklistVerificador(request.POST, instance=check)
        if form.is_valid():
            form.save()
    return HttpResponseRedirect('/profesional/checklist/%i/' % check.id_clicheck.id_clicheck)

@groups_only('Profesional')
def verificar_check(request, id_check):
    check = Checklist.objects.get(id_check=id_check)
    if request.method == 'POST':
        form = ChecklistVerificador(instance=check)
    else:
        form = ChecklistVerificador(request.POST, instance=check)
        if form.is_valid():
            check = form.save()
            check.verificacion = True
            check.save()
    return HttpResponseRedirect('/profesional/checklist/%i/' % check.id_clicheck.id_clicheck)
##
#######################################################################################################
## MEJORAS

#######################################################################################################

@groups_only('Profesional')
def vista_mejoras(request):
    me = Mejora.objects.all().order_by('id_mejora')
    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(me, 5)
        me = paginator.page(page)
    except:
        raise Http404
    context = {'entity': me,
                'paginator': paginator}
    return render(request, 'profesional/mejoras/mejoras.html', context)


@groups_only('Profesional')
def modificar_me(request,id_mejora):
    mejora = Mejora.objects.get(id_mejora=id_mejora)
    if request.method == 'GET':
        form = MejoraForm(instance=mejora)
    else:
        form = MejoraForm(request.POST, instance=mejora)
        if form.is_valid():
            form.save()
            messages.success(request, "Modificado correctamente")
        return redirect(to='vista_mejoras')
    return render(request, 'profesional/mejoras/modificar.html',{'form':form})

@groups_only('Profesional')
def crear_me(request):
    data = {
        'form': MejoraForm
    }
    if request.method == 'POST':
        formulario = MejoraForm(data=request.POST)
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


@groups_only('Profesional')
def vista_actividad(request):
    id_usuario = request.user.id

    try:
        pro = Profesional.objects.get(id_perfil=Perfil.objects.get(id_auth_user=id_usuario))
        id_profesional = pro.id_prof
        ACT = Actividad.objects.filter(id_prof=id_profesional).order_by('-id_actividad')
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
    return render(request, 'profesional/actividad/actividad.html', context)

@groups_only('Profesional')
def crear_actividad(request):
    data = {
        'form': ActividadForm
    }
    if request.method == 'POST':
        formulario = ActividadForm(data=request.POST)
        if formulario.is_valid():
            data["form"] = formulario 
            formulario.save()
            messages.success(request, "Creado correctamente!")
            return redirect (to='vista_actividad')
        else:
            data["form"] = formulario 
    return render(request, 'profesional/actividad/crear-act.html',data )

@groups_only('Profesional')
def modificar_actividad(request,id_actividad):
    act = Actividad.objects.get(id_actividad=id_actividad)

    if request.method == 'GET':
        form = ActividadModForm(instance=act)
    else:
        form = ActividadModForm(request.POST, instance=act)
        if form.is_valid():
            form.save()
            messages.success(request, "Actividad modificada correctamente")
        return redirect(to='vista_actividad')

    return render(request, 'profesional/actividad/modificar-act.html',{'form':form})

@groups_only('Profesional')
def estado_actividad(request,id_actividad):
    act = Actividad.objects.get(id_actividad=id_actividad)

    if request.method == 'GET':
        form = ActividadEstadoForm(instance=act)
    else:
        form = ActividadEstadoForm(request.POST, instance=act)
        if form.is_valid():
            form.save()
            messages.success(request, "Estado modificado correctamente")
        return redirect(to='vista_actividad')

    return render(request, 'profesional/actividad/estado-act.html',{'form':form})

#######################################################################################################
## VISITA
#######################################################################################################
@groups_only('Profesional')
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

@groups_only('Profesional')
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

@groups_only('Profesional')
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

@groups_only('Profesional')
def ingresar_visita(request):
    data = {
        'form': IngresarVisita
    }
    if request.method == 'POST':
        formulario = IngresarVisita(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Creado correctamente!")
            return redirect (to='vista_actividad')
        else:
            data["form"] = formulario
    return render(request, 'profesional/visita/ingresar-visita.html',data)

@groups_only('Profesional')
def cliente_asignado(request):
    id_usuario = request.user.id

    try:
        pro = Profesional.objects.get(id_perfil=Perfil.objects.get(id_auth_user=id_usuario))
        id_profesional = pro.id_prof
        ACT = Actividad.objects.filter(id_prof=id_profesional)
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
    return render(request, 'profesional/clientes.html', context)
