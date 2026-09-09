class Alumno:

    def __init__(self,nombre):
        self.nombre = nombre

    def estudiar(self):
        print(self.nombre,"está estudiando")

a = Alumno("Carlos")

a.estudiar()