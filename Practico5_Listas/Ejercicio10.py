"""
Una tienda registra las ventas de 4 productos durante 7 dias, en una matriz de 4x7
Mosotrar el total vendido por cada producto
Mostrar el dia con mayores ventas totales
Indicar cual fue el producto mas vendido en la semana
"""

productos = ["agua", "gaseosa", "fruta", "harina"]

ventas_semana = [
    [13, 23, 25, 23, 35, 11, 26],
    [1, 3, 2, 5, 8, 22, 10],
    [ 7, 10, 26, 19, 20, 31, 9],
    [3, 5, 19, 25, 15, 20, 22]
]

dias_semana = [
    "Lunes",
    "Martes",
    "Miercoles",
    "Jueves",
    "Viernes",
    "Sabado",
    "Domingo",
]

# Total vendido de cada producto

totales_productos = []

for i in range(len(ventas_semana)):
    ventas_totales = 0
    for venta_dia in ventas_semana[i]:
        ventas_totales += venta_dia
    totales_productos.append(ventas_totales)
    print(f"Total de ventas de {productos[i]}: {ventas_totales}")

# Dia con mayores ventas

totales_por_dia = []

for indice_dia in range(len(ventas_semana[0])):
    suma_dia = 0
    for indice_producto in range(len(ventas_semana)):
        suma_dia += ventas_semana[indice_producto][indice_dia]
    totales_por_dia.append(suma_dia)

mayor_venta_dia = totales_por_dia[0]
dia_mayor_venta_indice = 0
for i in range(len(totales_por_dia)):
    if totales_por_dia[i] > mayor_venta_dia:
        mayor_venta_dia = totales_por_dia[i]
        dia_mayor_venta_indice = i

print(f"El dia con mayores ventas totales fue el {dias_semana[dia_mayor_venta_indice]}, con un total de {mayor_venta_dia} ventas")

# Producto mas vendido

mayor_venta_producto = totales_productos[0]
producto_mas_vendido_indice = 0
for i in range(len(totales_productos)):
    if totales_productos[i] > mayor_venta_producto:
        mayor_venta_producto = totales_productos[i]
        producto_mas_vendido_indice = i
print(f"El producto mas vendido en la semana fue {productos[producto_mas_vendido_indice]} con un total de {mayor_venta_producto} ventas")