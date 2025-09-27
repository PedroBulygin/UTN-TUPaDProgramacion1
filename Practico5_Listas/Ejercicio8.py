"""
Crear una matriz con las notas de 5 estudiantes en 3 materias
Mostrar el promedio de cada estudiante
Mostrar el promedio de cada materia
"""

alumnos_y_notas = [
    ["pedro", 6, 7, 8], 
    ["javier", 10, 8, 9], 
    ["carlos", 7, 4, 5], 
    ["josefina", 7, 6, 8], 
    ["micaela", 8, 6, 5]
    ]

# Promedio de cada estudiante

for estudiante in alumnos_y_notas:
    nombre = estudiante[0]
    nota1 = estudiante[1]
    nota2 = estudiante[2]
    nota3 = estudiante[3]
    promedio = (nota1+nota2+nota3)/3
    print(f"El promedio del almuno {nombre} es de {promedio}")

for i in range(1, len(alumnos_y_notas[0])):
    sumatoria = 0
    for estudiante in alumnos_y_notas:
        sumatoria += estudiante[i]
    
    promedio_materia = sumatoria / 5
    print(f"El promedio de la materia es de {promedio_materia}")
