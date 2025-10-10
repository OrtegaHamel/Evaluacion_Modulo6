from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from tareas.forms import CustomAuthenticationForm

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tareas/', include('tareas.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]

# Sobrescribir el formulario de login
auth_views.LoginView.form_class = CustomAuthenticationForm
