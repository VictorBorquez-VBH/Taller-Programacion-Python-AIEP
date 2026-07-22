class Auto:

    def __init__(self):

        self.velocidad = 0

    def acelerar(self):

        self.velocidad += 20

auto = Auto()

print(auto.velocidad)

auto.acelerar()

print(auto.velocidad)