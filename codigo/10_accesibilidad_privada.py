class Cuenta:

    def __init__(self):
        self.__saldo = 1000

    def consultar_saldo(self):
        return self.__saldo

    def depositar(self, monto):
        if monto > 0:
            self.__saldo += monto

cuenta = Cuenta()
print(cuenta.consultar_saldo())
cuenta.depositar(500)
print(cuenta.consultar_saldo())