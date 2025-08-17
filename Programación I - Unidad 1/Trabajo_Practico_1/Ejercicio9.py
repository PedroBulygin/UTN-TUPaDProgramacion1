#Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
#pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia:
#°F=9/5.°C+32

celsius=input("Por favor, ingrese una temperatura en grados Celsius: ")
celsiusFloat=float(celsius)
F=str(9/5*celsiusFloat+32)
print(f"{celsius}°C equivalen a {F}°F")
