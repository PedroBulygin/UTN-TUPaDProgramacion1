"""Crear una lista con las notas de 10 estudiantes
Mostrar la lista completa
Calcular y mostrar el promedio
indicar la nota mas alta y la mas baja"""

lista_notas = [2, 7, 10, 6, 5, 4, 3, 4, 8, 6]
print(lista_notas)

sumatoria = 0

for i in lista_notas:
    sumatoria = sumatoria + i
promedio = sumatoria / 10
print(f"El promedio es {promedio}")

cantidad_notas = len(lista_notas)

for indice_pasada in range(cantidad_notas - 1):
    for indice_actual in range(cantidad_notas - 1 - indice_pasada):
        if lista_notas[indice_actual] > lista_notas[indice_actual + 1]:
            lista_notas[indice_actual], lista_notas[indice_actual + 1] = lista_notas[indice_actual + 1], lista_notas[indice_actual]
print("Lista ordenada de menor a mayor: ")
print(lista_notas)