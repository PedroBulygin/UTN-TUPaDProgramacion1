'''Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un número
par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso contrario, imprimir
por pantalla "Por favor ingrese un número par". Nota: Investigar el uso del operador módulo '''

print("Por favor, ingrese un número par: ")
numero = int(input())
if numero % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("No ingreso un numero par. Por favor, ingrese un número par")