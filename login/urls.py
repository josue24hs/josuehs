"""
URL configuration for login project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.agregar, name='agregar'),
    path('agregar/', views.agregar, name='agregar'),
    path('mostrar/',views.mostrar,name='mostrar'),
    path('exportar/', views.exportar, name='exportar'),
    path('buscar/', views.buscar, name='buscar'),
    path('eliminar/<int:id>/', views.eliminar, name='eliminar'),
    path('editar/<int:id>/', views.editar, name='editar'),
]
