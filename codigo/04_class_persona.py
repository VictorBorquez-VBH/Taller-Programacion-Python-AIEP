class Persona:

    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar(self):
        print(self.nombre,self.edad)