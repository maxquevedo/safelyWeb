from django.shortcuts import render


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