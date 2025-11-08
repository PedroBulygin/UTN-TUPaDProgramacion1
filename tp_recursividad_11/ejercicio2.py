"""
2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición
indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario
especifique.
"""
def fiboRecur(posicion):
    if posicion == 0:
        return 0
    elif posicion == 1:
        return 1
    else:
        return fiboRecur(posicion-1)+fiboRecur(posicion-2)
    
posicion = int(input("Ingrese la posicion: "))

for i in range(posicion + 1):
    print(fiboRecur(i))