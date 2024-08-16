class Producto:
    def _init_(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def get_id(self):
        return self.id

    def get_nombre(self):
        return self.nombre

    def get_cantidad(self):
        return self.cantidad

    def get_precio(self):
        return self.precio

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def set_precio(self, precio):
        self.precio = precio


class Inventario:
    def _init_(self):
        self.productos = []

    def añadir_producto(self, producto):
        for p in self.productos:
            if p.get_id() == producto.get_id():
                print("El ID ya existe")
                return
        self.productos.append(producto)

    def eliminar_producto(self, id):
        for p in self.productos:
            if p.get_id() == id:
                self.productos.remove(p)
                print("Producto eliminado")
                return
        print("Producto no encontrado")

    def actualizar_producto(self, id, cantidad=None, precio=None):
        for p in self.productos:
            if p.get_id() == id:
                if cantidad:
                    p.set_cantidad(cantidad)
                if precio:
                    p.set_precio(precio)
                print("Producto actualizado")
                return
        print("Producto no encontrado")

    def buscar_producto(self, nombre):
        resultado = [p for p in self.productos if p.get_nombre() == nombre]
        return resultado

    def mostrar_productos(self):
        for p in self.productos:
            print(f"ID: {p.get_id()}, Nombre: {p.get_nombre()}, Cantidad: {p.get_cantidad()}, Precio: {p.get_precio()}")


