# Programa para calcular el área de un triángulo

def calcular_area_triangulo(base, altura):
	"""
	Calcula el área de un triángulo dada la base y la altura.

	:param base: La base del triángulo (float)
	:param altura: La altura del triángulo (float)
	:return: El área del triángulo (float)
	"""
	return 0.5 * base * altura


def main():
	print("Programa para calcular el área de un triángulo")
	
	# Solicitar al usuario la base y la altura del triángulo
	base = float(input("Ingresa la base del triángulo: "))
	altura = float(input("Ingresa la altura del triángulo: "))
	
	# Calcular el área
	area = calcular_area_triangulo(base, altura)
	
	# Mostrar el resultado
	print(f"El área del triángulo es: {area}")


# Verificar si el script se está ejecutando directamente
if __name__ == "__main__":
	main()
