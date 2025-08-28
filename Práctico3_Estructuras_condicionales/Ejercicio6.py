'''
Teniendo en cuenta lo antes mencionado, escribir un programa que tome la lista
numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si
hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.

'''
from statistics import mode, median, mean
import random
numeros_aleatorios = [random.randint(1, 100) for i in range (50)]

mi_moda = mode(numeros_aleatorios)
mi_mediana = median(numeros_aleatorios)
mi_mean = mean(numeros_aleatorios)

print(f"La media es {mi_mean}, la Mediana es {mi_mediana} y la moda es {mi_moda}")

if mi_mean > mi_mediana and mi_mediana > mi_moda:
    print("Hay sesgo positivo o a la derecha")
elif mi_mean < mi_mediana and mi_mediana < mi_moda:
    print("Hay sesgo negativo o a la izquierda")
else:
    print("No hay sesgo")