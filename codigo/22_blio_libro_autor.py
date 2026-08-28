class Autor:
    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return self.nombre

class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def mostrar_informacion(self):
        print(f"Libro: {self.titulo}")
        print(f"Autor: {self.autor}")

class Biblioteca:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def listar_libros(self):
        print(f"\nBiblioteca: {self.nombre}")

        for libro in self.libros:
            print(f"- {libro.titulo}" f"({libro.autor})")
