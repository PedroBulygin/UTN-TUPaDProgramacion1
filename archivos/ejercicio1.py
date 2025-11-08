"""
1. Crear archivo inicial con productos: Crear un archivo de texto llamado
productos.txt con tres productos. Cada línea debe tener: nombre,precio,cantidad
"""

with open("productos.txt", "w") as archivo:
    archivo.write("Bateria, 200, 4\n")
    archivo.write("Camara, 500, 5\n")
    archivo.write("Celular, 1000, 10\n")

"""
2. Leer y mostrar productos: Crear un programa que abra productos.txt, lea cada
línea, la procese con .strip() y .split(","), y muestre los productos en el siguiente
formato:

"""
print("-" * 10, "Segundo ejercicio", "-" * 10)
inventario = {"Nombre": 0, "Precio": 0, "Cantidad": 0}

with open("productos.txt", "r") as archivo:
    for linea in archivo:
        contenido = linea.strip()
        cSeparado = contenido.split(",")
        # cSeparado es una lista que tiene individualizada cada item
        inventario["Nombre"] = cSeparado[0]
        inventario["Precio"] = cSeparado[1]
        inventario["Cantidad"] = cSeparado[2]
        print(f"Producto: {inventario['Nombre']} | Precio: ${inventario['Precio']} | Cantidad: {inventario['Cantidad']}")

"""
3. Agregar productos desde teclado: Modificar el programa para que luego de mostrar
los productos, le pida al usuario que ingrese un nuevo producto (nombre, precio,
cantidad) y lo agregue al archivo sin borrar el contenido existente
"""
print("-" * 10, "Tercer ejercicio", "-" * 10)

nuevo_producto = []
nombre = input("Por favor, ingrese el nombre del nuevo producto: ")
precio = input("Ingrese el precio: ")
cantidad = input("Ingrese la cantidad: ")
nueva_linea = nombre + "," + precio + "," + cantidad + "\n"

with open("productos.txt", "a") as archivo:
    archivo.write(nueva_linea)

"""
4. Cargar productos en una lista de diccionarios: Al leer el archivo, cargar los datos en
una lista llamada productos, donde cada elemento sea un diccionario con claves:
nombre, precio, cantidad.
"""
print("-" * 10, "Cuarto ejercicio", "-" * 10)

with open("productos.txt", "r") as archivo:
    lista_productos = []
        
    for linea in archivo:
        diccionario = {}
        productos = linea.strip().split(",")
        diccionario["nombre"] = productos[0]
        diccionario["precio"] = productos[1]
        diccionario["cantidad"] = productos[2]
        lista_productos.append(diccionario)
    
    print(lista_productos)

"""
5. Buscar producto por nombre: Pedir al usuario que ingrese el nombre de un
producto. Recorrer la lista de productos y, si lo encuentra, mostrar todos sus datos. Si
no existe, mostrar un mensaje de error.

"""
print("-" * 10, "Quinto ejercicio", "-" * 10)

producto_deseado = input("Ingrese el producto que desea buscar: ")

for producto in lista_productos:
        if producto["nombre"] == producto_deseado:
            print(producto)
            break

else:
    print("El producto no fue encontrado")

"""
6. Guardar los productos actualizados: Después de haber leído, buscado o agregado
productos, sobrescribir el archivo productos.txt escribiendo nuevamente todos los
productos actualizados desde la lista.
"""
print("-" * 10, "Sexto ejercicio", "-" * 10)


with open("productos.txt", "w") as archivo:
    for item in lista_productos:
        linea_a_escribir = item["nombre"] + "," + item["precio"] + "," + item["cantidad"] + "\n"
        archivo.write(linea_a_escribir)

print("'productos.txt' fue actualizado")

