"""
URL configuration for Djangocrud project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from Inventario.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", Inicio, name="index"),
    path("RegistroU/", CrearUsuario, name="registroU"),
    path("inventario/", listarProducto, name="inventario"),
    path("logout/", CierreSesion, name="logout"),
    path("login/", InicioSesion, name="login"),
    path("crearProducto/", crearProducto, name="crearProducto"),
    path("detalleProducto/<int:idProducto>/", detalleProducto, name="detalleProducto"),
    path("detalleProducto/<int:idProducto>/eliminar/", eliminarProducto, name="eliminarProducto"),
]
