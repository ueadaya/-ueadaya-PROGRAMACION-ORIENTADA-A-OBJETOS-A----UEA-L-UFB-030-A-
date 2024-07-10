# Definición de la clase
class MiClase:
	def __init__(self, nombre):
		"""
		Constructor de la clase MiClase.

		Args:
		- nombre: str, nombre que se asignará al objeto al ser creado.
		"""
		self.nombre = nombre  # Inicialización del atributo nombre
		print(f'Se ha creado un objeto {self.nombre}.')
	
	def __del__(self):
		"""
		Destructor de la clase MiClase.
		Se activa cuando el objeto es destruido, ya sea explícitamente con `del` o cuando ya no hay referencias al objeto.
		Realiza una limpieza simulada al liberar recursos o cerrar conexiones.
		"""
		print(f'Se está destruyendo el objeto {self.nombre}.')
	# Aquí podríamos cerrar archivos, conexiones, liberar memoria, etc.
	# En este ejemplo, solo imprimimos un mensaje para simular la acción.


# Creación de objetos y demostración
def main():
	# Creamos dos objetos de la clase MiClase
	objeto1 = MiClase('Objeto1')
	objeto2 = MiClase('Objeto2')
	
	# Eliminamos uno de los objetos explícitamente
	del objeto1


# Al finalizar la función main, objeto2 será destruido automáticamente

if __name__ == "__main__":
	main()