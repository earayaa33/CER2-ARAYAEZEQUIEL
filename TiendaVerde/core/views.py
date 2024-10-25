from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto, Pedido, PedidoProducto
from .carrito import Carrito
from django.contrib import messages
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

def home(request):
    productos = Producto.objects.all
    carrito = Carrito(request)
    total_productos = carrito.contar_productos()

    data = {
        'productos': productos, 'total_productos' : total_productos
    }

    return render(request, 'core/home.html', data)

def catalogo(request):
    productos = Producto.objects.all()
    carrito = Carrito(request)
    total_productos = carrito.contar_productos()

    data = {
        'productos': productos, 'total_productos' : total_productos
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

def ver_carrito(request):
    carrito = Carrito(request)
    total_productos = carrito.contar_productos()

    return render(request, 'core/carrito.html', {'carrito': carrito, 'total_productos': total_productos})

@login_required
def añadir_a_carrito(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    carrito = Carrito(request)
    carrito.agregar(producto)
    messages.success(request, f'{producto.nombre} añadido al carrito.')
    return redirect('catalogo')  # Redirigir al catálogo en vez del carrito


@login_required
def agregar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    carrito = Carrito(request)
    carrito.agregar(producto)
    return redirect('ver_carrito')

@login_required
def eliminar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    carrito = Carrito(request)
    carrito.eliminar(producto)
    return redirect('ver_carrito')

@login_required
def restar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    carrito = Carrito(request)
    carrito.restar(producto)
    return redirect('ver_carrito')

@login_required
def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect('ver_carrito')

def realizar_pedido(request):
    carrito = Carrito(request)

    if not carrito.carrito:
        return JsonResponse({'status': 'error', 'message': 'El carrito está vacío.'})

    # Crea un nuevo pedido para el usuario actual
    pedido = Pedido.objects.create(usuario=request.user)

    # Itera sobre los items en el carrito
    for item in carrito.carrito.values():
        producto = Producto.objects.get(id=item['producto_id'])
        cantidad = item['cantidad']
        PedidoProducto.objects.create(pedido=pedido, producto=producto, cantidad=cantidad)

    carrito.limpiar()  # Limpia el carrito después de crear el pedido

    messages.success(request, "Pedido realizado exitosamente")
    return redirect(to="catalogo")