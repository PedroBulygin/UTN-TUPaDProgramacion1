'''
7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
pantalla.

'''
#Creo un diccionario con las vocales
vocal = {'a','e','i','o','u'}

print("Ingrese una frase o palabra:")
#Le pido al usuario que ingrese su frase o palabra
cadena = input()

#A través de la funcion len(), grabo el número de caracteres ingresados por el usuario
num_caracteres = len(cadena)

#Reviso con un if si el último caracter de cadena se encuentra en el diccionario "vocal"
if cadena[-1] in vocal:
    print(f"{cadena}!")
else:
    print(f"{cadena}")