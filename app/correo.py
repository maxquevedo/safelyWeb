from django.shortcuts import render,redirect
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.conf import settings

from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *
from .forms import *

def enviar_mail(email):
    context ={'email':email}
    template = get_template('administrador/correo/test.html')
    content = template.render(context)
    mail = EmailMultiAlternatives(
        'Boleta Electronica Safely',
        'Mensaje: Aqui va el mensaje jaja',
        settings.EMAIL_HOST_USER,
        [email]
    )
    mail.attach_alternative(content,'text/html')
    mail.send()


def correo(request):
    if request.method == 'POST':
        email = request.POST.get('mail')
        enviar_mail(email)
        print(email)
    return render(request, 'administrador/boleta/boleta.html')

"""
"""
