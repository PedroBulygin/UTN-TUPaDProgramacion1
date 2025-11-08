"""
1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa
función para calcular y mostrar en pantalla el factorial de todos los números enteros
entre 1 y el número que indique el usuario
"""

def recurFact(num):
    return 1 if num == 0 else num * recurFact(num-1)

num = int(input("Ingrese un numero: "))

for i in range(1, num+1):
    print(recurFact(i))


