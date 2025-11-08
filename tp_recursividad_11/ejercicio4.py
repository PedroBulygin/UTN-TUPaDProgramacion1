"""
4) Crear una función recursiva en Python que reciba un número entero positivo en base
decimal y devuelva su representación en binario como una cadena de texto.

"""


def binario(num):
    if num == 0:
        return ""
    else:
        resto = str(num % 2)
        cociente = num // 2
        return binario(cociente) + resto

num = int(input("Ingrese un numero: "))
print(binario(num))
