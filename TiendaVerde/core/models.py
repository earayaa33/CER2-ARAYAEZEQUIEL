from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=50) #equivalente a VarChar
    precio = models.IntegerField()
    descripcion = models.TextField()
    stock = models.IntegerField()
    imagen = models.ImageField(upload_to="productos", null= True)

    def __str__(self):
        return f'{self.nombre}->{self.precio}'
