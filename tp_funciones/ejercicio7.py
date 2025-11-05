"""
7. Crear una función llamada operaciones_basicas(a, b) que reciba
dos números como parámetros y devuelva una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara.

"""

def operaciones_basicas(a, b):
    suma = a + b
    print(f"la suma de {a} + {b} es {suma}")
    resta = a - b
    print(f"La resta de {a} - {b} es {resta}")
    multiplicacion = a * b
    print(f"La multiplicacion entre {a} y {b} es {multiplicacion}")
    division = a / b
    print(f"La division entre {a} y {b} es {division}")

    return (suma, resta, multiplicacion, division)

# Programa Principal

a = int(input("Ingrese el primer numero: "))
b = int(input("Ingrese el segundo número: "))

operaciones_basicas(a,b)