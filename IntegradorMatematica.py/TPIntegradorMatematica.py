"""
Contador Binario:
Escriban un programa que, usando un ciclo, cuente desde 0 hasta 15 y muestre cada número en su representación binaria.
Extensión: Utilicen un retardo (por ejemplo, con time.sleep) para simular el conteo de un circuito.
"""

import time


lista_resto = []
numero = 0
resto = 0
numero_binario = ""

print("Inicio del conteo")

for numero in range (16):
    lista_resto = [] # Reseteo de lista de restos para cada iteracion
    numero_binario = "" #Reseteo de la variable
    temp_numero = numero #Para no modificar el contador

    if temp_numero == 0: #Para el primer caso, que es 0, ya que sino el bucle while lo saltea
        lista_resto = [0]

    else:
        while temp_numero > 0: #Generacion de numero binario
            resto = temp_numero % 2
            lista_resto.insert(0, resto) #Inserta el resto en el primer lugar de la lista de restos
            temp_numero = temp_numero // 2 #El cociente se transforma en temp_numero y es lo que termina haciendo salir del bucle

    for digito in lista_resto: #Convierto los elementos de la lista_resto en el numero binario correspondiente
        numero_binario = numero_binario +str(digito)

    print(f"{numero} - {numero_binario}")
    time.sleep(1)

print("Finalizacion del conteo")


ejecucion = True
while ejecucion:
    input()
    ejecucion = False
