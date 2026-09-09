class Libro:
    biblioteca = "Biblioteca AIEP"

    def __init__(self, titulo, autor, editor, precio, categoria, anio):
        self.titulo = titulo
        self.autor = autor
        self.editor = editor
        self.precio = precio
        self.categoria = categoria
        self.anio = anio

l1 = Libro("El Principito", "Antoine de Saint-Exupéry", "Reynal & Hitchcock", 10.99, "Ficción", 1943)
l2 = Libro("Cien Años de Soledad", "Gabriel García Márquez", "Editorial Sudamericana", 15.99, "Realismo Mágico", 1967)

print("Título:", l1.titulo)
print("Biblioteca:", l1.biblioteca)

l1.biblioteca = "Biblioteca Central"
print("Biblioteca actualizada:", l1.biblioteca)
print("Biblioteca:", l2.biblioteca)
