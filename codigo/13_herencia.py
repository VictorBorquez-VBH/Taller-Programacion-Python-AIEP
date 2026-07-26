class Animal:
    def comer(self):
        print("Estoy comiendo")

class Perro(Animal):
    def ladrar(self):
        print("Guau")

p = Perro()

p.comer()
p.ladrar()