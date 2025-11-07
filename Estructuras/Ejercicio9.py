"""
Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.
Permiti consultar que actividad hay en cierto día
"""

agenda = {
    ("lunes", "10:00"): "Entrevista",
    ("Martes", "17:00"): "Festejo cumpleaños",
    ("Miercoles", "15:30"): "Consulta Medica"
}

consulta_dia = input("Que día queres consultar?" )
consulta_hora = input("Que hora queres consultar? ")

consulta = (consulta_dia, consulta_hora)

if consulta in agenda:
    print(agenda[consulta])
else:
    print(f"No hay actividades a las {consulta_hora} horas del {consulta_dia}")