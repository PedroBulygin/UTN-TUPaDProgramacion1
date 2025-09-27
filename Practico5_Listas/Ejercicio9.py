"""
Representa un tablero de Ta-te-ti como una lista de 3x3
Inicializarlo con guines "-" representando casillas vacias
Permitir que dos jugadores ingresen posiciones (fila, columna) para colocar "X" o "O"
Mostrar el tablero despues de cada jugada
"""

tablero = [
    ["-", "-", "-"], 
    ["-", "-", "-"],
    ["-", "-", "-"]
    ]

jugador_actual = 0
juego_ejecucion = True
turno = 0

while juego_ejecucion == True:

    for fila_tablero in tablero:
        print(fila_tablero)

    if turno % 2 == 0:
        jugador_actual = "X"
        print("Es el turno del jugador X")
        turno += 1

    else:
        jugador_actual = "O"
        print("Es el turno del jugador O")
        turno += 1
    


    fila = int(input("Ingrese la fila en la que quiere realizar su jugada: "))
    columna = int(input("Ingrese la columna en la que quiere realizar su jugada: "))
    tablero [fila][columna] = jugador_actual
    

  
    
