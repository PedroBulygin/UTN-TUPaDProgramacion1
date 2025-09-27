"""
Crear una lista con los nombres de 8 estudiantes presentes en clase
Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente
Mostrar la lista final actualizada
"""
alumnos = ["pedro", "marcos", "javier", "micaela", "delfina", "luz", "agustin", "pablo"]

print(alumnos)

print("Quiere eliminar a un estudiante o agregar uno nuevo?")
accion = input("[Eliminar] [Agregar]")

if accion == "Eliminar":
    eliminado = input("A quien desea eliminar de la lista? ")
    alumnos.remove(eliminado)
elif accion == "Agregar":
    agregado = input("A quien desea agregar a la lista? ")
    alumnos.append(agregado)

print(alumnos)