"""
5) Solicita al usuario una frase e imprime:
• Las palabras únicas (usando un set).
• Un diccionario con la cantidad de veces que aparece cada palabra.
"""

frase = input("Ingrese una frase: ")

lista_de_palabras = frase.split()
#print(lista_de_palabras)

palabras_unicas = set(lista_de_palabras)
#print(palabras_unicas)

recuento = {}
for palabra in lista_de_palabras:
    if palabra in recuento:
        recuento[palabra] += 1
    else:
        recuento[palabra] = 1

print(f"Las palabras unicas son {palabras_unicas}")
print(f"El recuento de palabras es {recuento}")