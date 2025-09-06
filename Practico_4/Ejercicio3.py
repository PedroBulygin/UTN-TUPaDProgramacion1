print("Ingrese el primer numero: ")
num1 = int(input())
print("Ingrese el segundo número: ")
num2 = int(input())
contador = 0
for i in range (num1+1, num2):
    contador += i

print(contador)
