# Sobrecarga de métodos en Python (parametros por defecto)
class Calculadora:
    def sumar(self, a, b=0, c=0):
        return a + b + c

calc = Calculadora()

print(calc.sumar(5))
print(calc.sumar(5, 3))
print(calc.sumar(5, 3, 2))

