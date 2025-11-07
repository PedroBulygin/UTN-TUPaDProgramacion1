"""
6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
Luego, mostrá el promedio de cada alumno.
"""

# Tengo que hacer un diccionario
# El Key va a ser el nombre del alumno
# El value va a ser una tupla de tres notas

# Este va a ser el diccionario
alumnos_y_notas = {}

# Hago un loop for 3 veces para 3 alumnos
for i in range(1,4):
    # Este va a ser el Key
    alumno = input("Ingrese el nombre del alumno: ")

    # Para cada alumno, voy a generar una lista de 3 notas
    lista_notas = []
    for i in range(1,4):
        nota_individual = int(input("Ingrese las notas: "))
        lista_notas.append(nota_individual)

    # Voy a convertir la lista de notas en una tupla
    tupla_notas = tuple(lista_notas)

    # Ahora voy a agregar al diccionario el alumno y su tupla de notas
    alumnos_y_notas[alumno] = tupla_notas


print(alumnos_y_notas)