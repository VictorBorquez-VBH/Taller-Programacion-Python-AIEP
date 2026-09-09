# Sobrecarga de métodos en Python (operadores)
class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, otro):
        return Punto(self.x + otro.x, self.y + otro.y)

    def __str__(self):
        return f"({self.x}, {self.y})"

p1 = Punto(2, 3)
p2 = Punto(4, 5)

print(p1 + p2)