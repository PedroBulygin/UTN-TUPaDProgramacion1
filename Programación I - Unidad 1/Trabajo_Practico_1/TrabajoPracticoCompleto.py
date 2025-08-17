#Ejercicio1
print("Hola Mundo!")

#Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
#el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
#por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para
#realizar la impresión por pantalla

print("Por favor, ingrese su nombre:")
nombre = input()
print(f"Hola {nombre}, espero te encuentres muy bien!")

#Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
#imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
#“Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
#años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar
#la impresión por pantalla

nombre = input("Por favor, ingrese su nombre: ")
apellido = input("Ahora su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su lugar de residencia: ")

print(f"Soy {nombre} {apellido}, tengo {edad} años, y vivo en {residencia}")

#Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y
#su perímetro.

radio = input("Ingrese el radio del Círculo: ")
area = 3.14*int(radio)**2
perimetro = 2*3.14*int(radio)

print(f"El area del circulo es: {area} y el perimetro es: {perimetro}")

#Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a
#cuántas horas equivale.

print("Por favor, ingrese una cantidad de segundos y se definiran cuantas horas equivalen: ")
segundos=int(input())
horas=segundos//60

print(f"{segundos} segundos son {horas} horas")

#Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
#multiplicar de dicho número.

numero = int(input("Ingrese un número: "))

for i in range(1,11):
    resultado=i*numero
    print(str(i) + " x" + str(numero) + " = " + str(resultado))

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

#Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
#de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente
#modo: IMC=Peso en kg/ (altura en m)al cuadrado

altura=float(input("Por favor, ingrese su altura en metros: "))
peso=float(input("Por favor, ingrese su peso en Kg: "))
IMC=str(peso/altura**2)

print(f"Su indice de masa corporal es de {IMC}")

#Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
#pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia:
#°F=9/5.°C+32

celsius=input("Por favor, ingrese una temperatura en grados Celsius: ")
celsiusFloat=float(celsius)
F=str(9/5*celsiusFloat+32)
print(f"{celsius}°C equivalen a {F}°F")

#Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de
#dichos números.

print("Por favor, ingrese 3 numeros:")
primerNumero=int(input("Primer Numero: "))
segundoNumero=int(input("Segundo Número: "))
tercerNumero=int(input("Tercer Número: "))

promedio=str((primerNumero+segundoNumero+tercerNumero)/3)

print(f"El promedio de las 3 notas ingresadas es: {promedio}")






