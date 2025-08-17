#Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
#de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente
#modo: IMC=Peso en kg/ (altura en m)al cuadrado

altura=float(input("Por favor, ingrese su altura en metros: "))
peso=float(input("Por favor, ingrese su peso en Kg: "))
IMC=str(peso/altura**2)

print(f"Su indice de masa corporal es de {IMC}")