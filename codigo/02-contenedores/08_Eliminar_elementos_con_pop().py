#Dada una lista de números, elimine el último elemento utilizando pop() y muestre tanto la lista resultante como el elemento eliminado.
numeros = [10, 20, 30, 40, 50]
print("Lista original:", numeros)
# Eliminar el último elemento utilizando pop()  
numeros.pop()
print("Lista resultante:", numeros)

#Eliminar el segundo elemento utilizando pop() y muestre tanto la lista resultante como el elemento eliminado.
elemento_eliminado = numeros.pop(1)
print("Lista resultante:", numeros)
print("Elemento eliminado:", elemento_eliminado)
