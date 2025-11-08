"""
7) Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n
bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al
último nivel con un solo bloque.

"""

def contar_bloques(n):
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n-1)

n = int(input("Ingrese un numero: "))
print(contar_bloques(n))