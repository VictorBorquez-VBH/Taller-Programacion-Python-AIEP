class Vehiculo:
    def __init__(self, velocidad):
        self.velocidad = velocidad
        
    def encender(self):
        print("El vehículo ha sido encendido.")

    def acelerar(self):
        self.velocidad += 10
        print(f"El vehículo está acelerando a {self.velocidad} km/h.")

    def frenar(self):
        self.velocidad = 0
        print("El vehículo se ha detenido.")

    def apagar(self):
        print("El vehículo ha sido apagado.")

auto = Vehiculo(0)
auto.encender()
auto.acelerar()