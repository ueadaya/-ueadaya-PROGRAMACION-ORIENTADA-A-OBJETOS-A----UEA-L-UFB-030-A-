# Clase Libro
class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.titulo_autor = (titulo, autor)  # Tupla para título y autor
        self.categoria = categoria
        self.isbn = isbn

# Clase Usuario
class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []  # Lista de libros prestados

    def listar_libros_prestados(self):
        if self.libros_prestados:
            print(f"Libros prestados a {self.nombre}:")
            for libro in self.libros_prestados:
                print(f"- {libro.titulo_autor[0]} de {libro.titulo_autor[1]}")
        else:
            print(f"{self.nombre} no tiene libros prestados.")

# Clase Biblioteca
class Biblioteca:
    def __init__(self):
        self.libros_disponibles = {}  # Diccionario con ISBN como clave y objeto Libro como valor
        self.usuarios_registrados = {}  # Diccionario de usuarios con ID de usuario como clave
        self.ids_usuarios = set()  # Conjunto para gestionar IDs de usuarios únicos

    # Añadir libro
    def anadir_libro(self, libro):
        if libro.isbn not in self.libros_disponibles:
            self.libros_disponibles[libro.isbn] = libro
            print(f"Libro '{libro.titulo_autor[0]}' añadido a la biblioteca.")
        else:
            print(f"El libro con ISBN {libro.isbn} ya está en la biblioteca.")

    # Quitar libro
    def quitar_libro(self, isbn):
        if isbn in self.libros_disponibles:
            libro = self.libros_disponibles.pop(isbn)
            print(f"Libro '{libro.titulo_autor[0]}' eliminado de la biblioteca.")
        else:
            print(f"El libro con ISBN {isbn} no está disponible en la biblioteca.")

    # Registrar usuario
    def registrar_usuario(self, usuario):
        if usuario.id_usuario not in self.ids_usuarios:
            self.usuarios_registrados[usuario.id_usuario] = usuario
            self.ids_usuarios.add(usuario.id_usuario)
            print(f"Usuario {usuario.nombre} registrado exitosamente.")
        else:
            print(f"El usuario con ID {usuario.id_usuario} ya está registrado.")

    # Dar de baja usuario
    def eliminar_usuario(self, id_usuario):
        if id_usuario in self.usuarios_registrados:
            usuario = self.usuarios_registrados.pop(id_usuario)
            self.ids_usuarios.remove(id_usuario)
            print(f"Usuario {usuario.nombre} eliminado.")
        else:
            print(f"No se encontró un usuario con el ID {id_usuario}.")

    # Prestar libro
    def prestar_libro(self, id_usuario, isbn):
        if id_usuario in self.usuarios_registrados and isbn in self.libros_disponibles:
            usuario = self.usuarios_registrados[id_usuario]
            libro = self.libros_disponibles.pop(isbn)
            usuario.libros_prestados.append(libro)
            print(f"Libro '{libro.titulo_autor[0]}' prestado a {usuario.nombre}.")
        else:
            print(f"No se puede prestar el libro o el usuario no está registrado.")

    # Devolver libro
    def devolver_libro(self, id_usuario, isbn):
        if id_usuario in self.usuarios_registrados:
            usuario = self.usuarios_registrados[id_usuario]
            libro_a_devolver = next((libro for libro in usuario.libros_prestados if libro.isbn == isbn), None)
            if libro_a_devolver:
                usuario.libros_prestados.remove(libro_a_devolver)
                self.libros_disponibles[isbn] = libro_a_devolver
                print(f"Libro '{libro_a_devolver.titulo_autor[0]}' devuelto por {usuario.nombre}.")
            else:
                print(f"El usuario {usuario.nombre} no tiene prestado el libro con ISBN {isbn}.")

    # Buscar libros por título, autor o categoría
    def buscar_libros(self, termino):
        resultados = [libro for libro in self.libros_disponibles.values()
                      if termino.lower() in libro.titulo_autor[0].lower() or
                         termino.lower() in libro.titulo_autor[1].lower() or
                         termino.lower() in libro.categoria.lower()]
        if resultados:
            print("Libros encontrados:")
            for libro in resultados:
                print(f"- {libro.titulo_autor[0]} de {libro.titulo_autor[1]} (Categoría: {libro.categoria})")
        else:
            print(f"No se encontraron libros con el término '{termino}'.")

# Ejemplo de uso
if __name__ == "__main__":
    # Crear la biblioteca
    biblioteca = Biblioteca()

    # Crear libros
    libro1 = Libro("El Quijote", "Miguel de Cervantes", "Novela", "12345")
    libro2 = Libro("Cien años de soledad", "Gabriel García Márquez", "Ficción", "67890")

    # Añadir libros a la biblioteca
    biblioteca.anadir_libro(libro1)
    biblioteca.anadir_libro(libro2)

    # Crear y registrar usuarios
    usuario1 = Usuario("Juan", "u001")
    biblioteca.registrar_usuario(usuario1)

    # Prestar libro
    biblioteca.prestar_libro("u001", "12345")

    # Listar libros prestados
    usuario1.listar_libros_prestados()

    # Devolver libro
    biblioteca.devolver_libro("u001", "12345")

    # Buscar libros por autor
    biblioteca.buscar_libros("Gabriel García Márquez")
