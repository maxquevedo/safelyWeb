"""
def ProfileView(request,created):
    context = {'form': CustomUserCreationForm(),
    'form_p':PerfilForm(),
    'adminform':AdminForm(),
    'proform': ProfesionalForm(),
    'cliform': ClienteForm(),
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        formPerfil = PerfilForm(data=request.POST)
        formAdm = AdminForm(data=request.POST)
        formProf = ProfesionalForm(data=request.POST)
        formCli = ClienteForm(data=request.POST)

        if formulario.is_valid() and formPerfil.is_valid():
            usuario = formulario.save()
            group = request.POST.get('groups')
            usuario.groups.add(group)

            perfil = formPerfil.save(commit=False)    
            perfil.id_auth_user = usuario
            perfil.save()

            if perfil.tipo_perf=='1':
                admin = formAdm.save(commit=False)
                admin.id_perfil = perfil
                admin.save()
            elif perfil.tipo_perf=='2':
                prof = formProf.save(commit=False)
                prof.id_perfil = perfil
                prof.save()
            elif perfil.tipo_perf=='1':
                cli = formCli.save(commit=False)
                cli.id_perfil =perfil
                cli.save()

            messages.success(request, 'Usuario creado correctamente')
            return redirect(to="mantenedor")
        context = {'form': CustomUserCreationForm(),
        'form_p':PerfilForm(),
        'adminform':AdminForm(),
        'proform': ProfesionalForm(),
        'cliform': ClienteForm(),
        }

    return render(request, 'pruebas/profile.html', context)




"""