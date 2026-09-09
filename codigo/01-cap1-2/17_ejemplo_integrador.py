class Persona:

    def __init__(self,nombre):
        self.nombre = nombre

    def hablar(self):
        print("Hola")

class Profesor(Persona):

    def enseñar(self):
        print("Estoy enseñando Python")

class Estudiante(Persona):

    def estudiar(self):
        print("Estoy estudiando")

profe = Profesor("Carlos")
alumno = Estudiante("Ana")

profe.hablar()
profe.enseñar()

alumno.hablar()
alumno.estudiar()