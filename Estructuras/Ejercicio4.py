"""
4) Escribí un programa que permita almacenar y consultar números telefónicos.
• Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
• Luego, pedí un nombre y mostrale el número asociado, si existe.

"""

agenda = {}

for i in range (1, 6):
    clave = input("Ingrese el nombre del contacto: ")
    valor = input("Ingrese el número telefonico: ")
    agenda[clave] = valor

contacto = input("Que contacto desea buscar? ")

if contacto in agenda:
    print(agenda[contacto])
else:
    print("El contacto no esta agendado")