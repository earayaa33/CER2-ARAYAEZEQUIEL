from django.db import models
from django.contrib.auth.models import User


class Producto(models.Model):
    nombre = models.CharField(max_length=50) #equivalente a VarChar
    precio = models.IntegerField()
    descripcion = models.TextField()
    stock = models.IntegerField()
    imagen = models.ImageField(upload_to="productos", null= True)

    def __str__(self):
        return f'{self.nombre}'

class Pedido(models.Model):
    ESTADO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('completado', 'Completado'),
    ]

    usuario = models.ForeignKey(User, on_delete=models.CASCADE)  # Relacionado con el usuario que hace el pedido
    productos = models.ManyToManyField('Producto', through='PedidoProducto')  # Relación con productos a través de una tabla intermedia
    fecha = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES, default='pendiente')

    def __str__(self):
        return f'Pedido {self.id} por {self.usuario.username}'

class PedidoProducto(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    producto = models.ForeignKey('Producto', on_delete=models.CASCADE)
    cantidad = models.IntegerField()

    def __str__(self):
        return f'{self.producto.nombre}'