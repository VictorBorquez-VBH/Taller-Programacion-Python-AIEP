class CuentaBancaria:
    def __init__(self):
        self.__saldo = 0

    def depositar(self, monto):
        if monto > 0:
            self.__saldo += monto

    def retirar(self, monto):
        if 0 < monto <= self.__saldo:
            self.__saldo -= monto

    def consultar_saldo(self):
        return self.__saldo

cuenta = CuentaBancaria()

cuenta.depositar(500)
cuenta.retirar(100)

print(cuenta.consultar_saldo())