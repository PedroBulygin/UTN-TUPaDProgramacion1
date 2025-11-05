"""
10.Crear una función llamada calcular_promedio(a, b, c) que reciba
tres números como parámetros y devuelva el promedio de ellos.
Solicitar los números al usuario y mostrar el resultado usando esta
función.
"""

def calcular_promedio( a, b, c):
    promedio = (a+b+c)/3
    print(f"El promedio de las notas ingresadas es: {promedio}")

#Programa Principal
a = int(input("Ingrese la primer nota: "))
b = int(input("Ingrese la segunda nota: "))
c = int(input("Ingrese la tercera nota: "))

calcular_promedio(a,b,c)