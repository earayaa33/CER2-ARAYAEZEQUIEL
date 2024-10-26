class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get("carrito")
        if not carrito:
            self.session["carrito"] = {}
            self.carrito = self.session["carrito"]
        else:
            self.carrito = carrito

    def agregar(self, producto):
        id = str(producto.id)
        if id not in self.carrito.keys():
            self.carrito[id] = {
                "producto_id" : producto.id,
                "nombre" : producto.nombre,
                "precio_unitario:" : producto.precio,
                "acumulado" : producto.precio,
                "cantidad" : 1,
                'imagen_url': producto.imagen.url

            }
        else:
            self.carrito[id]["cantidad"] += 1
            self.carrito[id]["acumulado"] += producto.precio
        
        self.carrito[id]["precio_unitario"] = self.carrito[id]["acumulado"] / self.carrito[id]["cantidad"]
        
        self.guardar_carrito()

    def contar_productos(self):
        return sum(item['cantidad'] for item in self.carrito.values())

    def guardar_carrito(self):
        self.session["carrito"] = self.carrito
        self.session.modified = True

    def eliminar(self, producto):
        id = str(producto.id)
        if id in self.carrito:
            del self.carrito[id]
            self.guardar_carrito()

    def restar(self, producto):
        id = str(producto.id)
        if id in self.carrito.keys():
            self.carrito[id]["cantidad"] -= 1
            self.carrito[id]["acumulado"] -= producto.precio
            if self.carrito[id]["cantidad"] <= 0 : self.eliminar(producto)
            self.guardar_carrito()

    def limpiar(self):
        self.session["carrito"] = {}
        self.session.modified = True

    def total_precio(self):
        return sum(item['acumulado'] for item in self.carrito.values())
                