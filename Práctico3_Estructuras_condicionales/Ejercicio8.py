'''
Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
dependiendo de la opción que desee:
1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el
usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(),
lower() y title() de Python para convertir entre mayúsculas y minúsculas.

'''

print('Ingrese su nombre: ')
nombre = input()
print("Seleccione la opcion deseada: ")
print("[1] Si desea su nombre en mayusculas")
print("[2] Si desea su numbre en minúsculas")
print("[3] Si desea su nombre con la primera letra mayuscula")
opcion = int(input())

if opcion == 1:
    print(f"{nombre.upper()}")
elif opcion == 2:
    print(f"{nombre.lower()}")
elif opcion == 3:
    print(f"{nombre.title()}")

