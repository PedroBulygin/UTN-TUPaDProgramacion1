"""
10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.
"""

num_str = input("Ingresa un número entero: ")

num_invertido_str = ""

for i in range(len(num_str) - 1, -1, -1):
    num_invertido_str += num_str[i]

num_invertido = int(num_invertido_str)

print(f"El número invertido es: {num_invertido}")