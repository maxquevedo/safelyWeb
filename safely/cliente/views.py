from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from cliente import forms

"""
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
"""
@login_required
def home_cliente(request):

    return render(request, 'cliente/home-cliente.html')

def accidentes(request):
    return render(request, 'cliente/accidentes.html')

def actividades(request):
    return render(request, 'cliente/actividades.html')

def boleta(request):
    return render(request, 'cliente/boleta.html')

def contrato(request):
    return render(request, 'cliente/contrato.html')

def lista(request):
    return render(request, 'cliente/lista.html')

def perfil(request):
    return render(request, 'cliente/perfil.html')