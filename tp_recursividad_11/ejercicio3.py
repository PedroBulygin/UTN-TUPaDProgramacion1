"""
3) Crea una función recursiva que calcule la potencia de un número base elevado a un
exponente, utilizando la fórmula. 
Prueba esta función en un algoritmo general
"""

def potencia(base, numPotencia):
    return 1 if numPotencia == 0 else base * potencia(base, numPotencia-1)

base = int(input("Ingrese el numero base: "))
numPotencia = int(input("Ingrese el numero potencia: "))

print(f"{base} elevado a la potencia {numPotencia} es {potencia(base,numPotencia)}")
