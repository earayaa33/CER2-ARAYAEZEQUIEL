from django.contrib import admin

from .models import Producto, Pedido, PedidoProducto

# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display = ["nombre", "precio", "descripcion"]
    list_editable = ["precio"]
    search_fields = ["nombre"]
    list_filter = ["precio"]

admin.site.register(Producto)
admin.site.register(Pedido)
admin.site.register(PedidoProducto)

