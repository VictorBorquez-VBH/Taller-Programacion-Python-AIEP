#Desarrolle un programa que utilice una lista para administrar el inventario de una pequeña tienda. El programa debe permitir mostrar los productos, agregar un producto, eliminar un producto, consultar si un producto existe y determinar la cantidad total de productos.
inventario = ["manzanas", "bananas", "naranjas"]

print("Productos en inventario:")
for producto in inventario:
    print("-", producto)

nuevo_producto = "uvas"
inventario.append(nuevo_producto)
print(f"\nProducto agregado: {nuevo_producto}")

producto_a_eliminar = "bananas"
if producto_a_eliminar in inventario:
    inventario.remove(producto_a_eliminar)
    print(f"\nProducto eliminado: {producto_a_eliminar}")

print(f"\nCantidad total de productos: {len(inventario)}")
