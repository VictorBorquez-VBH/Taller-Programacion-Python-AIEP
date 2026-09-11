#Una asignatura posee un conjunto de notas. Almacene las notas en una lista y determine la cantidad de notas, la suma total y el promedio.
notas = [5.8, 7, 4.9,5.1, 6]
cantidad = len(notas)
suma = sum(notas)
promedio = suma / cantidad if cantidad > 0 else 0
print("Cantidad de notas:", cantidad)
print("Suma total:", suma)
print("Promedio:", promedio)
