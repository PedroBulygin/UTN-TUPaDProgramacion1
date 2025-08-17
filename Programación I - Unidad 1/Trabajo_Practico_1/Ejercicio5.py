#Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a
#cuántas horas equivale.

print("Por favor, ingrese una cantidad de segundos y se definiran cuantas horas equivalen: ")
segundos=int(input())
horas=segundos//60

print(f"{segundos} segundos son {horas} horas")