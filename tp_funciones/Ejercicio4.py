"""
4. Crear dos funciones: calcular_area_circulo(radio) que 
reciba el radio como parámetro y devuelva el área del círculo.
 calcular_perimetro_circulo(radio) que reciba el radio como 
 parámetro y devuelva el perímetro del círculo. 
 Solicitar el radio al usuario y llamar ambas funciones para
 mostrar los resultados
"""
import math

def calcular_area_circulo(radio):
    return print (math.pi * (radio**2))

def calcular_perimetro_circulo(radio):
    return print(2*math.pi*radio)

# Programa Principal

radio = int(input("Ingrese el radio: "))
calcular_area_circulo(radio)
calcular_perimetro_circulo(radio)