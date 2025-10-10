# tareas/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .forms import TareaForm

# Diccionario para almacenar tareas por usuario
tareas = {}  
@login_required
def lista_tareas(request):
    # Obtener las tareas del usuario actual
    tareas_usuario = tareas.get(request.user.username, [])
    return render(request, 'tareas/lista_tareas.html', {'tareas': tareas_usuario})

@login_required
def detalle_tarea(request, tarea_id):
    tareas_usuario = tareas.get(request.user.username, [])
    if tarea_id >= len(tareas_usuario):
        return render(request, 'tareas/acceso_denegado.html', status=403)
    tarea = tareas_usuario[tarea_id]
    return render(request, 'tareas/detalle_tarea.html', {'tarea': tarea})

# Vista para agregar una nueva tarea
@login_required
def agregar_tarea(request):
    if request.method == 'POST':
        form = TareaForm(request.POST)
        if form.is_valid():
            titulo = form.cleaned_data['titulo']
            descripcion = form.cleaned_data['descripcion']
            # Usar el username como clave en el diccionario
            if request.user.username not in tareas:
                tareas[request.user.username] = []
            tarea_id = len(tareas[request.user.username])
            tareas[request.user.username].append({
                'id': tarea_id,
                'titulo': titulo,
                'descripcion': descripcion,
            })
            return redirect('lista_tareas')
    else:
        form = TareaForm()
    return render(request, 'tareas/agregar_tarea.html', {'form': form})

# Vista para eliminar una tarea
@login_required
def eliminar_tarea(request, tarea_id):
    tareas_usuario = tareas.get(request.user.username, [])
    if tarea_id >= len(tareas_usuario):
        return render(request, 'tareas/acceso_denegado.html', status=403)
    if request.method == 'POST':
        del tareas_usuario[tarea_id]
        return redirect('lista_tareas')
    tarea = tareas_usuario[tarea_id]
    return render(request, 'tareas/eliminar_tarea.html', {'tarea': tarea})

# Vista para el registro de nuevos usuarios
def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('lista_tareas')
        else:
            if 'password2' in form.errors:
                form.errors['password2'] = form.error_class(['Las contraseñas no coinciden.'])
    else:
        form = UserCreationForm()

    form.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Nombre de usuario'})
    form.fields['password1'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Contraseña'})
    form.fields['password2'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Confirmar contraseña'})

    return render(request, 'registration/registro.html', {'form': form})