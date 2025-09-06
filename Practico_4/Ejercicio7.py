"""Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
número entero positivo indicado por el usuario."""

num = int(input("Ingrese un número entero positivo "))
sumatoria = 0

if num > 0:
    for i in range (0, num+1):
        sumatoria += i
    print(sumatoria)
else:
    print("Tenía que ser numero entero positivo")