"""
9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
poder procesar 100 números cambiando solo un valor)
"""
sumatoria = 0
for i in range (100):
    num = int(input("Ingrese un número entero: "))
    if num != int:
        print("No pusiste un número entero")
        break
    else:
        sumatoria += num
media = sumatoria / 100
print(f"La media de los valores es de {media}")