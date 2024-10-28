from django.contrib import admin

from .models import Producto, Pedido, PedidoProducto

# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display = ["nombre", "precio", "descripcion", "stock"]
    list_editable = ["precio"]
    search_fields = ["nombre"]
    list_filter = ["precio"]

class PedidoProductoInline(admin.TabularInline):
    model = PedidoProducto
    readonly_fields = ["producto","cantidad", "precio_total"]

    def precio_total(self, obj):
        return obj.producto.precio * obj.cantidad  

    precio_total.short_description = "Precio Total"


class PedidoAdmin(admin.ModelAdmin):
    list_display = ["id", "usuario", "estado", "fecha"]
    list_editable = ["estado"]
    list_filter = ["estado"]
    inlines = [PedidoProductoInline]

class PedidoProductoAdmin(admin.ModelAdmin):
    list_display = ["producto", "pedido", "cantidad", "precio_total"]  
    search_fields = ["producto__nombre", "pedido__id"]  

    def precio_total(self, obj):
        return obj.producto.precio * obj.cantidad 

    precio_total.short_description = "Precio Total"

admin.site.register(Producto, ProductoAdmin)
admin.site.register(Pedido, PedidoAdmin)
admin.site.register(PedidoProducto, PedidoProductoAdmin)

