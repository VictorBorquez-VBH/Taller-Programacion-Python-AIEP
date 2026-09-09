class Persona:

    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar(self):
        print(self.nombre,self.edad)

    def mostrar_nombre(self):
        print(self.nombre)

p1 = Persona("Juan", 30)
p2 = Persona("Ana", 25)

p1.mostrar()
p2.mostrar()

p1.mostrar_nombre()
p2.mostrar_nombre()

