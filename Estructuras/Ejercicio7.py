"""
7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1
y Parcial 2:
• Mostrá los que aprobaron ambos parciales.
• Mostrá los que aprobaron solo uno de los dos.
• Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).
"""




aprobado_primero = {1, 2, 3, 6, 45, 21}
aprobado_segundo = {2, 3, 100, 56, 9, 10}

print(f"Los alumnos que aprobaron ambos parciales son: ", aprobado_primero & aprobado_segundo)
print(f"Los alumnos que parobaron uno solo de los dos son: ", aprobado_primero ^ aprobado_segundo)
print(f"Los alumnos que aprobaron al menos uno de los dos son: ", aprobado_primero | aprobado_segundo)
      