"""
Dada una lista con 7 numeros, rotar todos los elementos una
posicion hacia la derecha (el ultimo pasa a ser el primero)
"""

numeros = [1, 2, 3, 4, 5, 6, 7]

print(numeros)

ultimo_numero = numeros[6]
numeros.remove(numeros[6])
numeros.insert(0, ultimo_numero)

print(numeros)