"""
5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
programa debe mostrar cuántos intentos fueron necesarios para acertar el número.
"""

import random

intentos = 0
respuesta = random.randint(0,9)
print("Adivine que numero es entre el 0 y 9:")

while True:
    numero = int(input())
    if numero != respuesta:
        print("Numero equivocado!")
        intentos += 1
    else:
        print(f"Adiniaste! Solo te llevo {intentos} intentos")

