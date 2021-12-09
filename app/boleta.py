from django_filters.filters import Filter

from .models import *
from .forms import *
from django.contrib import messages
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.http.response import Http404
from django.contrib.auth.decorators import login_required
from django.db import connection


from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.conf import settings

from datetime import date

@login_required
def creaBoleta(request):
    context = {'form':BoletaForm()}

    if request.method == 'POST':
        formulario = BoletaForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Creado correctamente!")
            return redirect (to='listaBoletas')
        else:
            context["form"] = formulario  
    return render(request, 'administrador/boleta/crear.html',context)
@login_required
def editarBoleta(request,id_boleta):
    boleta = Boleta.objects.get(id_boleta=id_boleta)
    if request.method == 'GET':
        form = BoletaForm(instance=boleta)
    else:
        form = BoletaForm(request.POST, instance=boleta)
        if form.is_valid():
            form.save()
            messages.success(request, "modificado correctamente")
        return redirect(to='listaBoletas')
    return render(request,'administrador/boleta/modificar.html',{'form':form})

@login_required
def listaBoletas(request):
    boleta = Boleta.objects.all().order_by('pagado') 
    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(boleta, 5)
        boleta = paginator.page(page)  
    except:
        raise Http404
    context = {'entity': boleta,
                'paginator': paginator}
    return render(request, 'administrador/boleta/boleta.html',context)

@login_required
def datosBoleta(request, id_boleta):
    boleta = Boleta.objects.get(id_boleta=id_boleta)
    context = {'form': boleta}
    template = get_template('administrador/correo/enviar_boleta.html')
    content = template.render(context)
    mail = EmailMultiAlternatives(
        'Boleta Electronica Safely',
        'Mensaje: Aqui va el mensaje jaja',
        settings.EMAIL_HOST_USER,
        [boleta.id_contrato.id_cli.id_perfil.id_auth_user.email]
    )
    mail.attach_alternative(content,'text/html')
    mail.send()
    return render(request,'administrador/correo/enviar_boleta.html',context)

