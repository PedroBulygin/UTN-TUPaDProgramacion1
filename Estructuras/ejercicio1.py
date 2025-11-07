"""
1) Dado el diccionario precios_frutas
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':
1450}
Añadir las siguientes frutas con sus respectivos precios:
● Naranja = 1200
● Manzana = 1500
● Pera = 2300
"""

precio_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
precio_frutas['Naranja'] = 1200
precio_frutas['Manzana'] = 1500
precio_frutas['Pera'] = 2300

#print(precio_frutas)

"""
2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
● Banana = 1330
● Manzana = 1700
● Melón = 2800
"""
precio_frutas['Banana'] = 1330
precio_frutas['Manzana'] = 1700
precio_frutas['Melón'] = 2800

#print(precio_frutas)

"""
3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los
precios
"""

solo_frutas = []

for fruta in precio_frutas:
    solo_frutas.append(fruta)

#print(solo_frutas)
