import os
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders
from django.shortcuts import render

from django.views.generic import ListView
from .models import *

class ReporteClienteListView(ListView):
    model = Cliente
    template_name ='administrador/reportes/reporteCliHome.html'

def ReporteGlobal(request):
    
    return render(request,'administrador/reportes/reporteglohome.html')

class ReporteHome(ListView):
    model = Cliente
    template_name ='administrador/report-home.html'

def ReporteCliente_render_pdf_view(requiest,*args,**kwargs):
    id_cli = kwargs.get('id_cli')
    actividadAsesoria = Actividad.objects.filter(id_cli=id_cli, tipo_act= 2)
    actividadVisita = Actividad.objects.filter(id_cli=id_cli, tipo_act= 3)
    actividadCapacitacion = Actividad.objects.filter(id_cli=id_cli, tipo_act= 1)
    cliente = Cliente.objects.filter(id_cli=id_cli)
    alertas = Alerta.objects.filter(id_cli=id_cli)


    template_path = 'administrador/reportes/reporteCliente.html'
    context = { 'actividadA':actividadAsesoria,
                'actividadV':actividadVisita,
                'actividadC':actividadCapacitacion,
                'cliente':cliente,
                'alertas':alertas

    
    }
    
    
    
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    # En caso que se quiera descargar de inemdiato: 
    #response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    #que se habra en una ventana aparte
    response['Content-Disposition'] = 'filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response
       )
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response
    
#Administrador, Profesional, Cliente,Servicio, Plan, Contrato, Alerta,Lista,Mejora,Reporte,TipoReporte,Actividad, Capacitacion,Asesoria,Visita
def ReporteGlobal_pdf_view(request,*args,**kwargs):
    mes =  kwargs.get('mes')
    capacitacion =Actividad.objects.filter(fec_ida__month=mes, tipo_act= 1)
    asesoria =Actividad.objects.filter(fec_ida__month=mes,tipo_act= 2)
    actividad = Actividad.objects.filter(fec_ida__month=mes)
    servicio = Servicio.objects.all()
    plan = Plan.objects.all()
    accidente = Alerta.objects.all()
    mejora =Mejora.objects.all()
    visita =Actividad.objects.filter(fec_ida__month=mes,tipo_act= 3)
    perfil =Perfil.objects.all()
    alerta = Alerta.objects.filter(fec_aviso__month=mes)
    cuentaalerta = Alerta.objects.filter(fec_aviso__month=mes).count()
    admin = Perfil.objects.filter(tipo_perf=1)
    profesional = Perfil.objects.filter(tipo_perf=2) 
    cliente = Perfil.objects.filter(tipo_perf=3)
    usuario = User.objects.all()
    

    template_path = 'administrador/reportes/reporteglobal.html'
    context = {'capacitacion':capacitacion,
                'asesoria':asesoria,
                'actividad':actividad,
                'profesional':profesional,
                'cliente':cliente,
                'servicio':servicio,
                'plan':plan,
                'accidente':accidente,
                'mejora':mejora,
                'visita':visita,
                'perfil':perfil,
                'alerta':alerta,
                'cuentaalerta':cuentaalerta,
                'usuario':usuario,
                'admin':admin,
                }
    
    
    
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    # En caso que se quiera descargar de inemdiato: 
    #response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    #que se habra en una ventana aparte
    response['Content-Disposition'] = 'filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response
       )
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

