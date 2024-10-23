from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    #aqui indica que, al dirigirse a la raiz, se vincule la vista 'home'
    path('catalogo', views.catalogo, name='catalogo'),
    path('formulario', views.formulario, name='formulario'),
    path('inicioSesion', views.inicioSesion, name='inicioSesion'),
    path('registro/', views.registro, name='registro'),
    path('ver_carrito', views.ver_carrito, name='ver_carrito'),
    path('añadir_a_carrito/<int:producto_id>/', views.añadir_a_carrito, name='añadir_a_carrito'),
    path('agregar_producto/<int:producto_id>/', views.agregar_producto, name='agregar_producto'),
    path('restar_producto/<int:producto_id>/', views.restar_producto, name='restar_producto'),
    path('realizar_pedido', views.realizar_pedido, name='realizar_pedido')
    
]