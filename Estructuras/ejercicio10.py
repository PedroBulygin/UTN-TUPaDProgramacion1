"""
10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo
diccionario donde:
• Las capitales sean las claves.
• Los países sean los valores
"""

original = {
    "Argentina": "Buenos Aires",
    "Chile": "Santiago",
    "Estados Unidos": "Washington"
    }

invertida = {}
lista_keys = []
lista_values = []

for key in original.keys():
    lista_keys.append(key)
for values in original.values():
    lista_values.append(values)

contador = 0
for i in lista_values:
    invertida[i] = lista_keys[contador]
    contador += 1


print(original)
print(invertida)