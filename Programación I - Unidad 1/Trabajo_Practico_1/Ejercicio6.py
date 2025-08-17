#Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
#multiplicar de dicho número.

numero = int(input("Ingrese un número: "))

for i in range(1,11):
    resultado=i*numero
    print(str(i) + " x" + str(numero) + " = " + str(resultado))