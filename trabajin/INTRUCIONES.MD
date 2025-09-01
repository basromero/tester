1️⃣ Crear la carpeta contenedora y entrar en ella
mkdir ProyectoFront
cd ProyectoFront
------------------------------------------------------------------------------------------------------------------------------------------------------------------
2️⃣ Crear y activar un ambiente virtual
# Crear ambiente virtual
py -m venv .venv
------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Activarlo (PowerShell)
.\.venv\Scripts\Activate.ps1

# (Opcional) Si falla la activación por políticas:
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
.\.venv\Scripts\Activate.ps1

3️⃣ Instalar Django dentro del ambiente
pip install django
pip freeze > requirements.txt
------------------------------------------------------------------------------------------------------------------------------------------------------------------
4️⃣ Crear el proyecto Django
django-admin startproject proyectofront .
------------------------------------------------------------------------------------------------------------------------------------------------------------------
5️⃣ Crear la app principal
python manage.py startapp Pfront
------------------------------------------------------------------------------------------------------------------------------------------------------------------
6️⃣ Crear carpeta de templates dentro de la app
mkdir Pfront\templates
mkdir Pfront\templates\Pfront

Crear el archivo home.html:

New-Item Pfront\templates\Pfront\home.html -ItemType File

<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <title>Inicio ProyectoFront</title>
</head>
<body>
  <h1>¡Hola, Django funciona con templates!</h1>
  <p>Esta es la página de inicio de tu app Pfront.</p>
</body>
</html>
------------------------------------------------------------------------------------------------------------------------------------------------------------------
7️⃣ Definir la vista en Pfront/views.py
from django.shortcuts import render

def home(request):
    return render(request, 'Pfront/home.html')
------------------------------------------------------------------------------------------------------------------------------------------------------------------
8️⃣ Crear rutas de la app Pfront

Archivo Pfront/urls.py:

from django.urls import path
from . import views

app_name = 'Pfront'

urlpatterns = [
    path('', views.home, name='home'),
]
------------------------------------------------------------------------------------------------------------------------------------------------------------------
9️⃣ Conectar la app al proyecto principal

En proyectofront/urls.py:

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Pfront.urls')),  # 👈 conectamos la app
]
------------------------------------------------------------------------------------------------------------------------------------------------------------------
🔟 Probar el servidor
python manage.py migrate   # preparar base de datos inicial
python manage.py runserver
------------------------------------------------------------------------------------------------------------------------------------------------------------------
modificacion a system.py
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],  # vacío porque usas templates dentro de apps
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',



                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
Requisitos de entorno
Python: 3.8 o superior (idealmente 3.10+).
Django: versión estable (por ejemplo, 4.2 o 5.0).
pip: para instalar dependencias.
Virtualenv (opcional, pero recomendable): para aislar el entorno del proyecto.
SQLite: como base de datos por defecto (ya viene con Django).
requirements.txt con dependencias del proyecto (puede incluir Django, gunicorn, etc.).
