"""
Crear una matriz (lista anidada) de 7x2 con las temperaturas
minimas y maximas de una semana
Calcular el promedio de las minimas y el de las maximas
Mostrar en que dia se registro la mayor amplitud termica
"""

dia = [[21,10], [25, 9], [18, 12], [22, 7], [11, 4], [10, 2], [14, 7]]
sumatoria_maximas = 0
sumatoria_minimas = 0


for temperaturas_dia in dia:
    sumatoria_maximas = temperaturas_dia[0] + sumatoria_maximas
    sumatoria_minimas = temperaturas_dia[1] + sumatoria_minimas


promedio_maximas = sumatoria_maximas / len(dia)
promedio_minimas = sumatoria_minimas / len(dia)

print(f"El promedio de temperaturas maximas fue de {promedio_maximas} mientras que el de las temperaturas minimas fue de {promedio_minimas}")

mayor_amplitud = 0

for i in range(len(dia)):
    temp_maxima = dia[i][0]
    temp_minima = dia[i][1]
    amplitud_diaria = temp_maxima - temp_minima
    if amplitud_diaria > mayor_amplitud:
        mayor_amplitud = amplitud_diaria
        dia_semana = i

print(f"El día de mayor amplitud termica fue el {dia[dia_semana]}")
