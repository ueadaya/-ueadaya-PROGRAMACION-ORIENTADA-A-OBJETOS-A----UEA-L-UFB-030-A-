# Definiendo la clase base
class Animal:
    def __init__(self, name, age):
        self._name = name  # Atributo protegido
        self._age = age  # Atributo protegido

    def make_sound(self):
        raise NotImplementedError("Subclass must implement abstract method")

    def get_info(self):
        return f"Name: {self._name}, Age: {self._age}"

# Definiendo la clase derivada
class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.__breed = breed  # Atributo privado

    # Sobrescribiendo el método make_sound
    def make_sound(self):
        return "Woof!"

    # Encapsulación: método para acceder al atributo privado __breed
    def get_breed(self):
        return self.__breed

    # Ejemplo de polimorfismo mediante sobrescritura de método
    def get_info(self):
        base_info = super().get_info()
        return f"{base_info}, Breed: {self.__breed}"


if __name__ == "__main__":
    # Creando una instancia de la clase base
    animal = Animal("Generic Animal", 5)

    # Creando una instancia de la clase derivada
    dog = Dog("Buddy", 3, "Golden Retriever")

    # Demostrando encapsulación
    print(f"Dog's breed: {dog.get_breed()}")

    # Demostrando polimorfismo
    print(f"Animal Info: {animal.get_info()}")
    print(f"Dog Info: {dog.get_info()}")

    # Demostrando herencia y método sobrescrito
    try:
        print(f"Animal Sound: {animal.make_sound()}")
    except NotImplementedError as e:
        print(e)

    print(f"Dog Sound: {dog.make_sound()}")