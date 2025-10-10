
# Evaluación Módulo 6 – Gestor de Tareas (Django)
Por Álvaro Ortega Hamel

Este proyecto corresponde a la **evaluación del módulo 6**, en la cual se desarrolla una aplicación web con **Django** que permite a los usuarios **autenticarse, crear, visualizar y eliminar tareas**.  
Las tareas se manejan **en memoria**, sin conexión a una base de datos real.

---

## 📋 Descripción General

Imagina que trabajas como desarrollador para una empresa que está creando una pequeña aplicación web para **gestionar tareas**.  
El sistema permite a los usuarios:

- Registrarse, iniciar sesión y cerrar sesión.  
- Crear nuevas tareas con título y descripción.  
- Ver la lista de sus propias tareas.  
- Consultar los detalles de una tarea específica.  
- Eliminar tareas creadas.  

Todo el sistema funciona **con almacenamiento en memoria**, usando una lista de diccionarios que guarda las tareas del usuario autenticado.

---

## ⚙️ Tecnologías Utilizadas

- **Python 3.x**  
- **Django 5.x**  
- **HTML5 / CSS3 / Bootstrap 5**  
- **Django Templates**  
- **Django Forms**  
- **Sistema de Autenticación de Django (django.contrib.auth)**

---

## 🚀 Instalación y Configuración

Sigue los pasos para ejecutar el proyecto en tu entorno local:

### 1️⃣ Clonar el repositorio

```bash
git clone https://github.com/OrtegaHamel/Evaluacion_Modulo6.git
cd Evaluacion_Modulo6
```

### 2️⃣ Crear entorno virtual e instalar dependencias

```bash
python -m venv venv
# Activar entorno virtual
venv\Scripts\activate     # En Windows
source venv/bin/activate  # En Linux/Mac

```

### 3️⃣ Ejecutar el servidor

```bash
python manage.py runserver
```

Luego, abre en tu navegador:  
👉 [http://localhost:8000](http://localhost:8000)

---

## 🧱 Estructura del Proyecto

```
Evaluacion_Modulo6/
│
├── db.sqlite3 # Base de datos local (generada por Django)
├── manage.py # Punto de entrada del proyecto
│
├── gestor_tareas/ # Configuración principal del proyecto Django
│ ├── asgi.py # Configuración ASGI para despliegue asincrónico
│ ├── settings.py # Configuración global (apps, templates, auth, etc.)
│ ├── urls.py # URLs principales del proyecto
│ ├── wsgi.py # Configuración WSGI para despliegue
│ └── init.py # Marca el directorio como paquete Python
│
└── tareas/ # Aplicación encargada de la gestión de tareas
├── admin.py # Registro de modelos en el panel de administración
├── apps.py # Configuración de la aplicación
├── forms.py # Formularios de Django
├── models.py # Modelos de datos (manejo en memoria)
├── tests.py # Pruebas automatizadas
├── urls.py # Rutas de la app 'tareas'
├── views.py # Lógica de vistas (CRUD y auth)
│
├── migrations/ # Migraciones de la base de datos
│ └── init.py
│
├── templates/ # Plantillas HTML
│ ├── base.html
│ │
│ ├── registration/
│ │ ├── login.html
│ │ └── registro.html
│ │
│ └── tareas/
│ ├── acceso_denegado.html
│ ├── agregar_tarea.html
│ ├── detalle_tarea.html
│ ├── eliminar_tarea.html
│ └── lista_tareas.html
│
└── pycache/ # Archivos compilados por Python

---

## 🧩 Funcionalidades por Parte

### **Parte 1: Configuración Inicial**
- Crear el proyecto Django `gestor_tareas`.  
- Crear la aplicación `tareas`.  
- Registrar la app en `INSTALLED_APPS`.  
- Configurar URLs del proyecto y la app.

### **Parte 2: Vistas y Plantillas**
- **Vista de Lista de Tareas:**  
  Muestra todas las tareas del usuario autenticado.  
- **Vista de Detalle de Tarea:**  
  Muestra la información completa de una tarea específica.  
- **Vista de Agregar Tarea:**  
  Formulario con `forms.Form` para título y descripción.  
- **Vista de Eliminar Tarea:**  
  Permite eliminar tareas.  
- **Plantillas Responsivas:**  
  Diseñadas con **Bootstrap** para una interfaz limpia y adaptable.

### **Parte 3: Autenticación y Seguridad**
- Registro, inicio y cierre de sesión con `django.contrib.auth`.  
- Uso de `@login_required` para proteger vistas.  
- Cada usuario solo puede ver y gestionar **sus propias tareas**.

### **Parte 4: Despliegue y Pruebas**
- Verificación del funcionamiento de todas las vistas y formularios.  
- Pruebas básicas:
  - Las tareas se muestran correctamente.  
  - Los usuarios pueden agregar y eliminar tareas.  
  - El sistema de autenticación funciona correctamente.  
  - Las tareas son privadas por usuario.  
- Configuración de producción (ajuste de `ALLOWED_HOSTS`, `DEBUG`, etc.).

---

## 🧠 Aprendizajes Clave

- Implementación del flujo **MVC (Model-View-Template)** en Django.  
- Uso de **formularios dinámicos con Django Forms**.  
- Aplicación del **sistema de autenticación** integrado.  
- Buenas prácticas de seguridad y manejo de sesiones.  
- Diseño responsivo con **Bootstrap 5**.  

---


## 🪪 Licencia

Este proyecto es de uso educativo.  
© 2025 - Proyecto Evaluación Módulo 6 - Desarrollado por **Álvaro Ortega**.
