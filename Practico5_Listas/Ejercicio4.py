"""
Dada una lista con valores repetidos:
Crear una nueva lista sin elementos repetidos
Mostrar el resultado
"""

datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]

datos_sin_repetidos = []

for elemento in datos:
    if elemento not in datos_sin_repetidos:
        datos_sin_repetidos.append(elemento)

print(datos_sin_repetidos)