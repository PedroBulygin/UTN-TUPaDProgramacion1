#  Trabajo Práctico Integrador - Programación 1
#  Gestión de Datos de Países en Python

# ---------- IMPORT ----------

import csv                                         # Manejo de csv
import os                                          # Crear archivo si no existe

NOMBRE_ARCHIVO = "paises.csv"

# ---------- ARCHIVO CSV ----------

def cargar_paises(nombre_archivo):                # Funcion que permite leer el archivo CSV o crearlo con datos por default si no existe
    """
    Lee el archivo CSV y devuelve una lista de diccionarios.
    Si el archivo no existe, lo crea con encabezado y datos de ejemplo.
    """
    paises = []

    if not os.path.exists(nombre_archivo):
        print("El archivo no existe. Se creará uno nuevo con datos de ejemplo.")
        archivo = open(nombre_archivo, "w", newline="", encoding="utf-8")
        escritor = csv.writer(archivo)
        escritor.writerow(["nombre", "poblacion", "superficie", "continente"])
        escritor.writerow(["Argentina", "45376763", "2780400", "América"])
        escritor.writerow(["Japón", "125800000", "377975", "Asia"])
        escritor.writerow(["Brasil", "213993437", "8515767", "América"])
        escritor.writerow(["Alemania", "83149300", "357022", "Europa"])
        archivo.close()

    archivo = open(nombre_archivo, "r", encoding="utf-8")
    lector = csv.reader(archivo)
    encabezado = True

    for fila in lector:
        # Ignorar filas vacías o incompletas
        if len(fila) == 0:
            continue
        if len(fila) < 4:
            print(f"Línea ignorada por formato incorrecto: {fila}")
            continue

        # Saltar el encabezado solo una vez
        if encabezado:
            encabezado = False
            continue

        nombre = fila[0].strip()
        poblacion = fila[1].strip()
        superficie = fila[2].strip()
        continente = fila[3].strip()

        # Validar que población y superficie sean numéricas
        if poblacion.isdigit() and superficie.isdigit():
            pais = {
                "nombre": nombre,
                "poblacion": int(poblacion),
                "superficie": int(superficie),
                "continente": continente
            }
            paises.append(pais)
        else:
            print(f"Registro ignorado (valores inválidos): {fila}")

    archivo.close()
    return paises

def guardar_paises(nombre_archivo, paises):       # Funcion que permite guardar en el archivo CSV
    """Guarda toda la lista actualizada en el archivo CSV."""
    archivo = open(nombre_archivo, "w", newline="", encoding="utf-8")
    escritor = csv.writer(archivo)
    escritor.writerow(["nombre", "poblacion", "superficie", "continente"])
    for p in paises:
        escritor.writerow([p["nombre"], p["poblacion"], p["superficie"], p["continente"]])
    archivo.close()

# ---------- VALIDACIONES ----------

def validar_campos_no_vacios(nombre, poblacion, superficie, continente):          # Funcion que permite validar que todos los campos estén completos
    if nombre == "" or poblacion == "" or superficie == "" or continente == "":
        print("Todos los campos son obligatorios.")
        return False
    return True

def validar_numericos(poblacion, superficie):                                     # Funcion que permite validar que los campos numéricos sean números válidos
    if not poblacion.isdigit() or not superficie.isdigit():
        print("La población y la superficie deben ser números.")
        return False
    return True

def validar_existencia(paises, nombre):                                          # Funcion que permite validar si el país ya existe en la lista
    for p in paises:
        if p["nombre"].lower() == nombre.lower():
            print("El país ya existe en la lista.")
            return False
    return True

def validar_pais_en_lista(paises, termino):                                      # Funcion que devuelve una lista con países que contienen el término buscado
    resultados = []
    for p in paises:
        if termino.lower() in p["nombre"].lower():
            resultados.append(p)
    if len(resultados) == 0:
        print("No se encontraron países con ese nombre.")
    return resultados

def validar_pais_existente(paises, nombre_sel):                                 # Funcion que permite verificar si el nombre exacto ingresado existe en la lista
    for p in paises:
        if p["nombre"].lower() == nombre_sel.lower():
            return p
    print("El nombre ingresado no coincide con ningún país listado.")
    return None

# ---------- FUNCIONALIDADES ----------

def agregar_pais(paises):                       # Funcion para opción 1: Permite agregar un nuevo país a la lista y al CSV
    print("\nAGREGAR NUEVO PAÍS\n")
    nombre = input("Nombre: ").strip()
    poblacion = input("Población: ").strip()
    superficie = input("Superficie: ").strip()
    continente = input("Continente: ").strip()

    # Validaciones
    if not validar_campos_no_vacios(nombre, poblacion, superficie, continente):
        return
    if not validar_numericos(poblacion, superficie):
        return
    if not validar_existencia(paises, nombre):
        return

    nuevo = {
        "nombre": nombre,
        "poblacion": int(poblacion),
        "superficie": int(superficie),
        "continente": continente
    }

    paises.append(nuevo)
    guardar_paises(NOMBRE_ARCHIVO, paises)
    print(f"\n{nombre} ha sido agregado correctamente.\n")

def actualizar_pais(paises):                    # Funcion para opción 2: Permite actualizar la población y superficie de un país existente
    print("\nACTUALIZAR DATOS DE UN PAÍS")
    termino = input("Ingrese el nombre o parte del nombre: ").strip()

    # Buscar coincidencias total o parcial
    encontrados = validar_pais_en_lista(paises, termino)
    if len(encontrados) == 0:
        return

    mostrar_paises(encontrados)

    # Confirmar país exacto
    nombre_sel = input("Ingrese el nombre exacto del país a actualizar: ").strip()
    pais_objetivo = validar_pais_existente(paises, nombre_sel)
    if pais_objetivo is None:
        return

    # Pedir y validar nuevos datos
    nueva_pob = input("Nueva población: ").strip()
    nueva_sup = input("Nueva superficie: ").strip()

    if not validar_numericos(nueva_pob, nueva_sup):
        return

    # Aplicar actualización
    pais_objetivo["poblacion"] = int(nueva_pob)
    pais_objetivo["superficie"] = int(nueva_sup)
    guardar_paises(NOMBRE_ARCHIVO, paises)
    print(f"\nLos datos de {pais_objetivo["nombre"]} han sido actualizados correctamente.\n")

def buscar_pais(paises, termino):               # Funcion para opción 3: Busca países cuyo nombre contenga el término ingresado
    resultados = []
    for p in paises:
        if termino.lower() in p["nombre"].lower():
            resultados.append(p)
    return resultados

# ---------- FILTROS ----------

def filtrar_por_continente(paises, continente): # Funcion para opción 4: Filtra la lista de países según continente
    filtrados = []
    for p in paises:
        if p["continente"].lower() == continente.lower():
            filtrados.append(p)
    return filtrados

def filtrar_por_rango_poblacion(paises, minimo, maximo): # Funcion para opción 5: Filtra países según un rango de población
    filtrados = []
    for p in paises:
        if p["poblacion"] >= minimo and p["poblacion"] <= maximo:
            filtrados.append(p)
    return filtrados

def filtrar_por_rango_superficie(paises, minimo, maximo): # Funcion para opción 6: Filtra países según un rango de superficie
    filtrados = []
    for p in paises:
        if p["superficie"] >= minimo and p["superficie"] <= maximo:
            filtrados.append(p)
    return filtrados

# ---------- ORDEN ----------

def obtener_nombre(pais):                        # Funcion para obtener el nombre del pais
    return pais["nombre"]

def obtener_poblacion(pais):                     # Funcion para obtener la poblacion del pais
    return pais["poblacion"]

def obtener_superficie(pais):                    # Funcion para obtener la superficie del pais
    return pais["superficie"]

def ordenar_paises(paises, campo, descendente):  # Funcion para opción 7: Ordenar países segun parametros
    if campo == "nombre":
        clave = obtener_nombre
    elif campo == "poblacion":
        clave = obtener_poblacion
    elif campo == "superficie":
        clave = obtener_superficie
    else:
        print("\nUno de los campos ingresados es inválido.\n")
        return None
    return sorted(paises, key=clave, reverse=descendente)

# ---------- ESTADÍSTICAS ----------

def estadisticas(paises):                       # Funcion para opción 8: Muestra estadísticas de los países
    if len(paises) == 0:
        print("No hay datos cargados.")
        return

    pais_mayor = paises[0]
    pais_menor = paises[0]
    suma_poblacion = 0
    suma_superficie = 0
    continentes = {}

    for p in paises:
        if p["poblacion"] > pais_mayor["poblacion"]:
            pais_mayor = p
        if p["poblacion"] < pais_menor["poblacion"]:
            pais_menor = p
        suma_poblacion += p["poblacion"]
        suma_superficie += p["superficie"]

        cont = p["continente"]
        continentes[cont] = continentes.get(cont, 0) + 1

    prom_pob = suma_poblacion / len(paises)
    prom_sup = suma_superficie / len(paises)

    print("\nESTADÍSTICAS:")
    print("País con mayor población:", pais_mayor["nombre"], "-", pais_mayor["poblacion"])
    print("País con menor población:", pais_menor["nombre"], "-", pais_menor["poblacion"])
    print("Promedio de población:", int(prom_pob))
    print("Promedio de superficie:", int(prom_sup))
    print("Cantidad de países por continente:")
    for cont in continentes:
        print(f"  {cont}: {continentes[cont]}")        

# ---------- FORMATO DE TABLA ----------

    ### FORMATO DE TABLA PARA LOS DATOS ###

    # 'Nombre':<20 => imprime el nombre alineado a la izquierda en un ancho de 20
    # 'Población':>12 => imprime la población alineada a la derecha en un ancho de 12
    # 'Superficie':>12 => imprime la superficie alineada a la derecha en un ancho de 12
    # 'Continente':>12 => imprime la continente alineada a la derecha en un ancho de 12

def mostrar_paises(lista):                      # Funcion para mostrar en pantalla resultados o informar que no hay 
    if len(lista) == 0:
        print("\nNo se encontraron resultados.\n")
        return
    
    print(f"\n{'Nombre':<20} {'Población':>12} {'Superficie':>12} {'Continente':>12}")
    print("-" * 60)
    for p in lista:
        print(f"{p['nombre']:<20} {p['poblacion']:>12} {p['superficie']:>12} {p['continente']:>12}")
    print()

# ---------- MENU ----------

def menu():
    print("""
------------------------------
  GESTIÓN DE DATOS DE PAÍSES
------------------------------
1. Agregar nuevo país
2. Actualizar datos de un país
3. Buscar país por nombre
4. Filtrar por continente
5. Filtrar por rango de población
6. Filtrar por rango de superficie
7. Ordenar países
8. Mostrar estadísticas
0. Salir
""")

def main():
    paises = cargar_paises(NOMBRE_ARCHIVO)
    if len(paises) == 0:
        print("No se pudieron cargar datos. Verifique el archivo.")
        return

    opcion = ""
    while opcion != "0":
        menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_pais(paises)
        elif opcion == "2":
            actualizar_pais(paises)
        elif opcion == "3":
            termino = input("Ingrese el nombre o parte del nombre: ")
            mostrar_paises(buscar_pais(paises, termino))
        elif opcion == "4":
            cont = input("Ingrese el continente: ")
            mostrar_paises(filtrar_por_continente(paises, cont))
        elif opcion == "5":
            minimo = input("Población mínima: ")
            maximo = input("Población máxima: ")
            if minimo.isdigit() and maximo.isdigit():
                mostrar_paises(filtrar_por_rango_poblacion(paises, int(minimo), int(maximo)))
            else:
                print("Debe ingresar números válidos.")
        elif opcion == "6":
            minimo = input("Superficie mínima: ")
            maximo = input("Superficie máxima: ")
            if minimo.isdigit() and maximo.isdigit():
                mostrar_paises(filtrar_por_rango_superficie(paises, int(minimo), int(maximo)))
            else:
                print("Debe ingresar números válidos.")
        elif opcion == "7":
            campo = input("Ordenar por (nombre/poblacion/superficie): ").lower()
            orden = input("¿Descendente? (s/n): ").lower()

            if orden not in ["s", "n"]:
                print("\nValor inválido. Debe ingresar 's' para Sí o 'n' para No.\n")
                continue 

            resultado = ordenar_paises(paises, campo, orden == "s")

            if resultado is not None:         # <-- solo muestra si el campo fue válido
                mostrar_paises(resultado)

        elif opcion == "8":
            estadisticas(paises)
        elif opcion == "0":
            print("Fin del programa. Gracias por utilizar nuestra aplicacion.")
        else:
            print("\nLa opcion seleccionada no es valida.")

# ---------- EJECUCION ----------

main()
