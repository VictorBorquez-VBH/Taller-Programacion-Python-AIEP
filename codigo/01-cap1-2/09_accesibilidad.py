class Cuenta:

    def __init__(self):

        self.__saldo = 1000

cuenta = Cuenta()

print(cuenta.__saldo)

# Este ejemplo da error porque el atributo __saldo es privado 
# y no se puede acceder directamente desde fuera de la clase. 
# Para acceder al saldo, se debería crear un método público 
# dentro de la clase que devuelva el valor del saldo.