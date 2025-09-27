"""
Generar una lista con 15 numeros enteros al azar entre 1 y 100
Crear una lista con los pares y otra con los impares
Mostrar cuantos números tiene cada lista
"""

import random

numeros_random = []
numeros_par = []
numeros_impar = []

for i in range(15):
    numero = random.randint(1, 100)
    numeros_random.append(numero)
print(numeros_random)

for i in range(len(numeros_random)):
    if numeros_random[i] % 2 == 0:
        numeros_par.append(numeros_random[i])
    else:
        numeros_impar.append(numeros_random[i])

print(f"Cantidad de numeros pares: {len(numeros_par)}")
print(f"Cantidad de numeros impares: {len(numeros_impar)}")
        