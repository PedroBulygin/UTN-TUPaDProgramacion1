"""
8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock.
Permití al usuario:
• Consultar el stock de un producto ingresado.
• Agregar unidades al stock si el producto ya existe.
• Agregar un nuevo producto si no existe.

"""

inventario = {
    'Clavos': 60,
    'martillos': 3,
    'destornilladores': 10
}

print("Menu")
print("[1] Consultar Stock")
print("[2] Agregar unidades")
print("[3] Agregar producto nuevo")

accion = int(input("Que accion desea realizar? "))

match accion:
    case 1:
        producto = input("De que producto desea consultar stock? ")
        if producto in inventario:
            print(f"Hay {inventario[producto]} unidades de {producto}")
        else:
            print(f"El producto {producto} no se encuentra incluido en el inventario")

    case 2:
        print(inventario.keys())
        producto = input("De que producto desea agregar unidades? ")
        if producto in inventario:
            cantidades = int(input("Cuantas unidades desea ingresar? "))
            inventario[producto] += cantidades
        else:
            print(f"El producto {producto} no se encuentra incluido en el inventario")

    case 3:
        producto = input("Que producto desea ingresar? ")
        if producto in inventario:
            print(f"El {producto} ya se encuentra en el inventario")
        else:
            cantidades = int(input("Cuantas unidades desea ingresar? "))
            inventario[producto] = cantidades