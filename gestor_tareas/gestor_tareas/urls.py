# gestor_tareas/urls.py
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tareas/', include('tareas.urls')),
    path('accounts/', include('django.contrib.auth.urls')),  # URLs de autenticación
]
