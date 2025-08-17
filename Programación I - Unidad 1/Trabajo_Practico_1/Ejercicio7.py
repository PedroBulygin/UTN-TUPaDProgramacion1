#Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
#pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.

print("Por favor, ingrese dos numeros distintos al 0")
primerNumero = input("Ingrese el primer número: ")
segundoNumero = input("Ingrese el segundo número: ")

primerNumeroInt=int(primerNumero)
segundoNumeroInt=int(segundoNumero)

if primerNumeroInt and segundoNumeroInt != 0:
    #Suma
    suma=primerNumeroInt+segundoNumeroInt
    sumaStr=str(suma)
    print(f"El resultado de la suma entre {primerNumero} y {segundoNumero} es {sumaStr}")

    #Division
    division=str(primerNumeroInt/segundoNumeroInt)
    print(f"El resultado de la división entre {primerNumero} y {segundoNumero} es {division}")

    #Multiplicacion
    multiplicacion=str(primerNumeroInt*segundoNumeroInt)
    print(f"El resultado de multiplicar {primerNumero} por {segundoNumero} es {multiplicacion}")

    #resta
    resta=str(primerNumeroInt-segundoNumeroInt)
    print(f"El resultado de restar {primerNumero} - {segundoNumero} es {resta}")
else:
    print("Usted ingreso un número igual a 0, reinicie el programa.")




