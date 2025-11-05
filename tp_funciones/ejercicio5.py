"""
5. Crear una función llamada segundos_a_horas(segundos) que reciba
una cantidad de segundos como parámetro y devuelva la cantidad
de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función
"""

def segundos_a_horas(segundos):
    horas = segundos / 60
    print(f"{segundos} segundos son {horas} horas")

# Programa Principal
segundos = int(input("Ingrese los segundos: "))
segundos_a_horas(segundos)