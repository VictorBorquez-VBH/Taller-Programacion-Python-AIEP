# Ejemplo de métodos de instancias
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")

p1 = Persona("Alice", 30)
p1.saludar()  # Llamada al método saludar

persona = [Persona("Bob", 25), Persona("Charlie", 35), Persona("Diana", 28)]

for p in persona:
    p.saludar()  # Llamada al método saludar para cada objeto en la lista   

persona[1].saludar()  # Llamada al método saludar para el segundo objeto en la lista

# Ejemplo de métodos de clase (classmethod)
class Circulo:
    pi = 3.14159

    def __init__(self, radio):
        self.radio = radio

    @classmethod
    def area(cls, radio):
        return cls.pi * (radio ** 2)

c1 = Circulo(5)
print("Área del círculo:", c1.area(5))

# Ejemplo de métodos estáticos (staticmethod)
class Calculadora:
    @staticmethod
    def sumar(a, b):
        return a + b

    @staticmethod
    def restar(a, b):
        return a - b

print("Suma:", Calculadora.sumar(5, 3))
print("Resta:", Calculadora.restar(5, 3))

# funcion normal
def multiplicar(a, b):
    return a * b

print("Multiplicación:", multiplicar(5, 3))