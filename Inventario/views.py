from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm 
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from Inventario.forms import ProductoForm
from Inventario.models import Inventario
from django.contrib.auth.decorators import login_required
# Create your views here.

def Inicio(request):
    return render(request, "index.html") 

def CrearUsuario(request):
    
    if request.method == "GET":
        return render(request, "RegistroU.html",{
        "form" : UserCreationForm
    }) 
    else:
        if request.POST["password1"] == request.POST["password2"]:
            #Resgistro de usuario
            try:
                user = User.objects.create_user(username=request.POST["username"], password=request.POST["password1"])
                user.save()
                login(request, user)
                return redirect('inventario')
            except IntegrityError:
                return render(request, "RegistroU.html",{
                    "form" : UserCreationForm,
                    "error": "Usuario ya existe"
                }) 
                
        return render(request, "RegistroU.html",{
                    "form" : UserCreationForm,
                    "error": "Contraseñas no conciden"
                }) 

@login_required
def listarProducto(request):
    productos = Inventario.objects.filter(user=request.user)
    return render(request, "inventario.html", {
        "productos": productos
    })

@login_required
def crearProducto(request):
    if request.method == "GET":
        return render(request, "crearProducto.html", {
            "form": ProductoForm
        })
    else:
        try:
            form = ProductoForm(request.POST)
            nuevoProducto = form.save(commit=False)
            nuevoProducto.user = request.user
            nuevoProducto.save()
            return redirect("inventario")
        except ValueError:
            return render(request, "crearProducto.html", {
            "form": ProductoForm,
            "Error": "Proporciona información valida"
        })

@login_required
def detalleProducto(request, idProducto):
    if request.method == "GET":
        producto = get_object_or_404(Inventario, pk=idProducto)
        form = ProductoForm(instance=producto)        
        return render(request, "detalleProducto.html", {
            "producto": producto,
            "form": form  
        })
    else:
        try:
            producto = get_object_or_404(Inventario, pk=idProducto)
            form = ProductoForm(request.POST, instance=producto)
            form.save()
            return redirect("inventario")
        except ValueError:
            return render(request, "detalleProducto.html", {
            "producto": producto,
            "form": form,
            "error": "Error editando el producto"
        })

@login_required
def eliminarProducto(request, idProducto):
    producto = get_object_or_404(Inventario, pk=idProducto)
    if request.method == "POST":
        producto.delete()
        return redirect("inventario")

@login_required
def CierreSesion(request):
    logout(request)
    return redirect("index")

def InicioSesion(request):
    if request.method == "GET": 
        return render(request, "login.html", {
            "form": AuthenticationForm
        })
    else:
        user = authenticate(request, username=request.POST["username"], password=request.POST["password"])
        if user is None:
            return render(request, "login.html", {
                "form": AuthenticationForm,
                "error": "Usuario o contraseña incorrecta"
            })
        else:
            login(request, user)
            return redirect("inventario")
