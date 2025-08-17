#Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de
#dichos números.

print("Por favor, ingrese 3 numeros:")
primerNumero=int(input("Primer Numero: "))
segundoNumero=int(input("Segundo Número: "))
tercerNumero=int(input("Tercer Número: "))

promedio=str((primerNumero+segundoNumero+tercerNumero)/3)

print(f"El promedio de las 3 notas ingresadas es: {promedio}")

