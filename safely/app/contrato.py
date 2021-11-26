from django_filters.filters import Filter
from .models import *
from .forms import *
from django.contrib import messages
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.http.response import Http404
from django.contrib.auth.decorators import login_required
from django.db import connection


@login_required
def contratoCliente(request):
    context = {'form':ContratoForm()}

    if request.method == 'POST':
        formulario = ContratoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, " creado correctamente!")
            return redirect (to='home-adm')
        else:
            context["form"] = formulario  
    return render(request, 'administrador/contrato/contrato_cliente.html',context)

@login_required
def listaContrato(request):
    contrato = Contrato.objects.all().order_by('id_contrato')
    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(contrato, 5)
        contrato = paginator.page(page)
    except:
        raise Http404
    context = {'entity': contrato,
                'paginator': paginator}
    return render(request, 'administrador/contrato/contrato.html',context)

@login_required
def editarContrato(request,id_contrato):
    contrato = Contrato.objects.get(id_contrato=id_contrato)
    if request.method == 'GET':
        form = ContratoForm(instance=contrato)
    else:
        form = ContratoForm(request.POST, instance=contrato)
        if form.is_valid():
            form.save()
            messages.success(request, "modificado correctamente")
        return redirect(to='listaContrato')
    return render(request,'administrador/contrato/editar.html',{'form':form})
