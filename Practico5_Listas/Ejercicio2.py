"""
Pedir al usuario que cargue 5 productos en una lista.
Mostrar la lista ordenada alfabeticamente. Metodo sorted()
Preguntar al usuario que producto desea eliminar y actualizar la lista
"""
lista = []
print("Por favor, ingrese 5 productos: ")
for i in  range(5):
    item = input()
    lista.append(item)

lista_ordenada = sorted(lista)
print(lista_ordenada)

itemAEliminar = input("Que item desea eliminar? ")

lista_ordenada.remove(itemAEliminar)

print(lista_ordenada)