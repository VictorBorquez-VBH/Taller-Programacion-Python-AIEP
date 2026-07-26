class Perro:
    def hablar(self):
        print("Guau")

class Gato:
    def hablar(self):
        print("Miau")

animales = [Perro(), Gato()]

for animal in animales:
    animal.hablar()