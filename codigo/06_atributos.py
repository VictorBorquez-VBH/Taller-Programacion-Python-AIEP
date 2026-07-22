class Alumno:

    def __init__(self,nombre,edad,carrera):

        self.nombre = nombre
        self.edad = edad
        self.carrera = carrera

a1 = Alumno("Juan",20,"Informática")

print(a1.nombre)
print(a1.edad)
print(a1.carrera)

