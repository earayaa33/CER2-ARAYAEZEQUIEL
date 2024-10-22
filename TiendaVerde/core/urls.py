from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    #aqui indica que, al dirigirse a la raiz, se vincule la vista 'home'
    path('catalogo', views.catalogo, name='catalogo'),
    path('formulario', views.formulario, name='formulario'),
    path('inicioSesion', views.inicioSesion, name='inicioSesion'),
    path('registro/', views.registro, name='registro'),
    path('carrito', views.carrito, name='carrito')
    
]