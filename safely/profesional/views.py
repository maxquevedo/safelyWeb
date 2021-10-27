from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from app.forms import UserUpdateForm
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