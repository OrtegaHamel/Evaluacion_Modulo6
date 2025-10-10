# tareas/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import TareaForm

# Lista en memoria para almacenar tareas
tareas = []

@login_required
def lista_tareas(request):
    return render(request, 'tareas/lista_tareas.html', {'tareas': tareas})

def detalle_tarea(request, tarea_id):
    tarea = tareas[tarea_id]
    return render(request, 'tareas/detalle_tarea.html', {'tarea': tarea})

# Vista para agregar una nueva tarea
@login_required
def agregar_tarea(request):
    if request.method == 'POST':
        form = TareaForm(request.POST)
        if form.is_valid():
            titulo = form.cleaned_data['titulo']
            descripcion = form.cleaned_data['descripcion']
            tareas.append({'titulo': titulo, 'descripcion': descripcion})
            return redirect('lista_tareas')
    else:
        form = TareaForm()
    return render(request, 'tareas/agregar_tarea.html', {'form': form})

# Vista para eliminar una tarea
@login_required
def eliminar_tarea(request, tarea_id):
    tarea = tareas[tarea_id]
    if request.method == 'POST':
        del tareas[tarea_id]
        return redirect('lista_tareas')
    return render(request, 'tareas/eliminar_tarea.html', {'tarea': tarea})
