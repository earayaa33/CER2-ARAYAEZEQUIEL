from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto
from django.contrib import messages
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login

def home(request):
    return render(request, 'core/home.html', {})

def catalogo(request):
    productos = Producto.objects.all()
    data = {
        'productos': productos
    }
    return render(request, 'core/catalogo.html', data)

def formulario(request):
    return render(request, 'core/formulario.html', {})

def inicioSesion(request):
    return render(request, 'registration/inicioSesion.html', {})

def registro(request):

    data = {

        'form' : CustomUserCreationForm()

    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data = request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username = formulario.cleaned_data["username"], password = formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Te has registrado exitosamente")
            return redirect(to="home")

        data["form"] = formulario

    return render(request, 'registration/registro.html', data)

def carrito(request):
    data = {

    }

    return render(request, 'core/carrito.html', data)
