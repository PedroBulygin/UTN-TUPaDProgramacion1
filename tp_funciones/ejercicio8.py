"""
8. Crear una función llamada calcular_imc(peso, altura) que reciba el
peso en kilogramos y la altura en metros, y devuelva el índice de
masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.
"""

def calcular_imc(peso, altura):
    imc = peso/altura**2
    print(f"El indice de masa corporal es {imc:.2f}")

#Programa principal
peso = float(input("Ingrese el peso: "))
altura = float(input("Ingrese la altura: "))
calcular_imc(peso, altura)