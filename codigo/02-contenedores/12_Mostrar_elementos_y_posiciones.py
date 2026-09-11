#Dada una lista de estudiantes, recórrala utilizando un ciclo y muestre cada estudiante junto con la posición que ocupa dentro de la lista.
estudiantes = ["Juan", "María", "Pedro", "Ana", "Luis"]
# Recorrer la lista utilizando un ciclo for con enumerate para obtener el índice y el valor
for i, estudiante in enumerate(estudiantes):
    print(f"Posición {i}: {estudiante}")

for i in range(len(estudiantes)):
    print("Posición:", i, "-", estudiantes[i])
