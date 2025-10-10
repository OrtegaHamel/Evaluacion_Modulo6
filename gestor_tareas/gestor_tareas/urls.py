# gestor_tareas/urls.py
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='tareas/', permanent=True)),  # Redirige la raíz a /tareas/
    path('tareas/', include('tareas.urls')),  # Incluye las URLs de la app tareas
]
