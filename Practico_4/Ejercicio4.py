"""
Elabora un programa que permita al usuario ingresar números enteros y los sume en
secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
un 0.
"""

num1 = 1
sumatoria=0
while num1 != 0:
    print("Ingrese un número entero: ")
    numero = int(input())
    sumatoria += numero
    if numero == 0:
        print(sumatoria)
        num1=0