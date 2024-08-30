class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.__id = id
        self.__nombre = nombre
        self.__cantidad = cantidad
        self.__precio = precio

    # Métodos para obtener atributos
    def obtener_id(self):
        return self.__id

    def obtener_nombre(self):
        return self.__nombre

    def obtener_cantidad(self):
        return self.__cantidad

    def obtener_precio(self):
        return self.__precio

    # Métodos para establecer atributos
    def establecer_cantidad(self, cantidad):
        self.__cantidad = cantidad

    def establecer_precio(self, precio):
        self.__precio = precio

    def __str__(self):
        return f"ID: {self.__id}, Nombre: {self.__nombre}, Cantidad: {self.__cantidad}, Precio: {self.__precio}"


import json

class Inventario:
    def __init__(self):
        self.productos = {}

    def añadir_producto(self, producto):
        self.productos[producto.obtener_id()] = producto

    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            return True
        return False

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        if id_producto in self.productos:
            if cantidad is not None:
                self.productos[id_producto].establecer_cantidad(cantidad)
            if precio is not None:
                self.productos[id_producto].establecer_precio(precio)
            return True
        return False

    def buscar_producto_por_nombre(self, nombre):
        resultados = [producto for producto in self.productos.values() if producto.obtener_nombre() == nombre]
        return resultados

    def mostrar_todos_los_productos(self):
        for producto in self.productos.values():
            print(producto)

    def guardar_en_archivo(self, nombre_archivo):
        with open(nombre_archivo, 'w') as archivo:
            json.dump({id_producto: vars(producto) for id_producto, producto in self.productos.items()}, archivo)

    def cargar_desde_archivo(self, nombre_archivo):
        with open(nombre_archivo, 'r') as archivo:
            productos_cargados = json.load(archivo)
            for id_producto, datos_producto in productos_cargados.items():
                producto = Producto(**datos_producto)
                self.añadir_producto(producto)

def menu():
    inventario = Inventario()

    while True:
        print("\nGestión de Inventario:")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto por nombre")
        print("5. Mostrar todos los productos")
        print("6. Guardar inventario en archivo")
        print("7. Cargar inventario desde archivo")
        print("8. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_producto = input("ID del producto: ")
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            producto = Producto(id_producto, nombre, cantidad, precio)
            inventario.añadir_producto(producto)

        elif opcion == "2":
            id_producto = input("ID del producto a eliminar: ")
            if inventario.eliminar_producto(id_producto):
                print("Producto eliminado.")
            else:
                print("Producto no encontrado.")

        elif opcion == "3":
            id_producto = input("ID del producto a actualizar: ")
            cantidad = input("Nueva cantidad (dejar en blanco si no cambia): ")
            precio = input("Nuevo precio (dejar en blanco si no cambia): ")
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            if inventario.actualizar_producto(id_producto, cantidad, precio):
                print("Producto actualizado.")
            else:
                print("Producto no encontrado.")

        elif opcion == "4":
            nombre = input("Nombre del producto a buscar: ")
            resultados = inventario.buscar_producto_por_nombre(nombre)
            for producto in resultados:
                print(producto)

        elif opcion == "5":
            inventario.mostrar_todos_los_productos()

        elif opcion == "6":
            nombre_archivo = input("Nombre del archivo para guardar: ")
            inventario.guardar_en_archivo(nombre_archivo)
            print("Inventario guardado en archivo.")

        elif opcion == "7":
            nombre_archivo = input("Nombre del archivo para cargar: ")
            inventario.cargar_desde_archivo(nombre_archivo)
            print("Inventario cargado desde archivo.")

        elif opcion == "8":
            break

        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu()
