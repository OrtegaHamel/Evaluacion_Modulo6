from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.views.generic.base import RedirectView
from tareas.forms import CustomAuthenticationForm

# Sobrescribir el formulario de login
auth_views.LoginView.form_class = CustomAuthenticationForm

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tareas/', include('tareas.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', RedirectView.as_view(pattern_name='login'), name='home'),
]
