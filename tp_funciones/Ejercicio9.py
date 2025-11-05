"""
9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
una temperatura en grados Celsius y devuelva su equivalente en
Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
resultado usando la función.

"""

def celsius_a_fahrenheit(celsius):
    F = (celsius * 1.8) + 32
    print(f"{celsius} grados C equivalen a {F} grados F")

#Programa principal

celsius = float(input("Ingrese los grados °C: "))
celsius_a_fahrenheit(celsius)