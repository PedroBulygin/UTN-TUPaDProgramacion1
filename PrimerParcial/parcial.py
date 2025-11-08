titulos = []
ejemplares = []


# El menú estará disponible hasta que el usuario decida salir, eligiendo la opcion de salida

ejecucion = True

while ejecucion:
    print("===============MENU===============")
    print("Bienvenidos a la biblioteca escolar")
    print("[1] Ingresar títulos")
    print("[2] Ingresar ejemplares")
    print("[3] Mostrar catálogo")
    print("[4] Consultar disponibilidad")
    print("[5] Listar agotados")
    print("[6] Agregar título")
    print("[7] Actualizar ejemplares (prestamos/devolucion)")
    print("[8] Salir")
    opcion = input("Que acción desea realizar? ")

    match opcion:
        case "1": #Ingresar Titulos
            ingreso = True
            while ingreso:
                print("¿Que Titulos desea ingresar?")
                pelicula = input()
                print("¿Cuantos ejemplares desea ingresar?")
                numero_ejemplares = int(input())
                if numero_ejemplares >= 0:
                    titulos.append(pelicula)
                    ejemplares.append(numero_ejemplares) 
                    print(f"Muy bien, se han ingresado {numero_ejemplares} de ejemplares del título: {pelicula}")
                    continuar = input("Desea ingresar otro título? si/no: ")
                    if continuar == "no":
                        ingreso = False
                else:
                    print("Tiene que ingresar un número positivo")
                

        case "2": #Ingresar ejemplares
            print("¿De que título desea ingresar ejemplares?")
            nombre_titulo = input()
            if nombre_titulo in titulos: # Reviso que el título del que se quiere ingresar ejemplares se encuentre en la lista de títulos
                print(f"¿Cuantos ejemplares de {nombre_titulo} desea ingresar?")
                cantidad_ejemplares = int(input())
                if cantidad_ejemplares > 0:
                    indice_titulo = titulos.index(nombre_titulo) #Encuentro el indice del titulo
                    nuevo_stock = ejemplares[indice_titulo] + cantidad_ejemplares
                    ejemplares[indice_titulo] = nuevo_stock #Actualizo el nuevo numero de stock
                    print(f"Se han ingresado {cantidad_ejemplares} ejemplares nuevos de {nombre_titulo}")
                else:
                    print("Debe ingresar una cantidad mayor a 0")


            else: # Si el título no existe, le informo al usuario que primero debe ingresar el título
                print(f"El título {nombre_titulo}, no se encuentra en la biblioteca. Primero debes ingresarlo")
                # Agregaría aqui una opcion para que el usuario pueda ingresar directamente el título, pero no me quiero alejar de la consigna


        case "3": #Mostrar catalogo
            if titulos:
                for i in range(len(titulos)):
                    print(f"Titulo: {titulos[i]} - Ejemplares: {ejemplares[i]}")
            else:
                print("El catálogo esta vacío")

        case "4": #Mostrar disponibilidad
            print("Ingrese el título para consultar disponibilidad: ")
            nombre_titulo = input()
            if nombre_titulo in titulos: #Reviso que el titulo consultado existe en la lista de titulos
                indice_titulo = titulos.index(nombre_titulo) #Busco el indice correspondiente al titulo consultado

                if ejemplares[indice_titulo] > 0: #En la lista de ejemplares, con el indice especifico para el titulo, reviso si esta disponible o no hay stock
                    print(f"Se encuentran disponibles {ejemplares[indice_titulo]} ejemplares del título {nombre_titulo}")
                else:
                    print(f"No hay stock de {nombre_titulo}")


            else:
                print(f"Nunca se ha ingresado el titulo {nombre_titulo} a la biblioteca")

        case "5": #Listar Agotados
            if titulos:
                agotados_encontrados = False #Esta flag la voy a utilizar en caso de que haya disponibilidad de todos los titulos
                for i in range(len(ejemplares)):
                    if ejemplares[i] == 0:
                        print(f"{titulos[i]} se encuentra agotado")
                        agotados_encontrados = True
                if agotados_encontrados == False:
                    print("Todos los ejemplares cuentan con stock")
                    
            else: #Esto es en caso de que aún no se haya ingresado ningun titulo
                print("No existen títulos en la biblioteca")


        case "6": #Permite Añadir un nuevo titulo y sus ejemplares disponibles, respetando la sincronia de los indices en las listas
            print("¿Que titulo desea ingresar?")
            nuevo_titulo = input()

            if nuevo_titulo in titulos:
                print("El titulo ya se encuentra ingresado en la biblioteca. Para ingresar nuevos ejemplares utilice la opcion [2]")
            else:
                print("¿Cuantas cantidades de ejemplares?")
                cantidad_nuevo_titulo = int(input())
                titulos.append(nuevo_titulo)
                ejemplares.append(cantidad_nuevo_titulo)
                print(f"Se han agregado {cantidad_nuevo_titulo} ejemplares de {nuevo_titulo}")
                        
        case "7": #Actualizar ejemplares (préstamo/devolucion)
            print("¿Que acción desea realizar?")
            print("[1] Solicitar Prestamo [2] Devolver ejemplar")
            accion = str(input())
            match accion:
                case "1": #Solicitar ejemplar en prestamo
                    print("¿Que título desear solicitar en prestamo?")
                    prestamo = str(input())
                    if prestamo in titulos: #Revisar que el titulo se encuentre en la lista
                        indice_titulo = titulos.index(prestamo) #Encuentro el indice del titulo en la lista titulo
                        if ejemplares[indice_titulo] > 0: #Reviso si hay ejemplares del titulo
                            print(f"Existen {ejemplares[indice_titulo]} numero de ejemplares disponibles")
                            print("¿Cuantos desea retirar?")
                            prestamo_numero = int(input()) #Especifico el numero de ejemplares que desea retirar
                            if ejemplares[indice_titulo] < prestamo_numero: #Reviso que el numero de ejemplares a retirar no sea mayor al numero de ejemplares disponibles
                                print("No puede retirar un número mayor del solicitado")
                            else:
                                print(f"Usted retirara {prestamo_numero} ejemplares del titulo {prestamo}")
                                nuevo_stock = ejemplares[indice_titulo] - prestamo_numero
                                ejemplares[indice_titulo] = nuevo_stock #Actualizo el numero de ejemplares restando los ejemplares retirados
                        else: #En caso de que no haya stock
                            print(f"En este momento no hay disponibilidad del titulo {prestamo}")
                    else: #Si el titulo no se encuentra en la biblioteca
                        print("El titulo no se encuentra en la biblioteca")

                case "2": #Devolver ejemplar
                    print("¿Que titulo desea devolver?")
                    titulo_devolucion = str(input())

                    if titulo_devolucion in titulos: #Reviso que el titulo exista previamente en la biblioteca
                        indice_titulo = titulos.index(titulo_devolucion) #Encuentro el indice del titulo en la lista titulo
                        print("¿Cuantos ejemplares desea devolver?")
                        devolucion_ejemplares = int(input())
                        nuevo_stock = ejemplares[indice_titulo] + devolucion_ejemplares
                        ejemplares[indice_titulo] = nuevo_stock
                        print(f"Usted a devuelto {devolucion_ejemplares} ejemplares del título {titulo_devolucion}")
                        print(f"Nuevo stock disponible de {titulo_devolucion}: {ejemplares[indice_titulo]}")
                    
                    else: #El titulo no es de esta biblioteca
                        print("El titulo que desea devolver no corresponde a esta biblioteca")


                case _:
                    print("No eligio una opcion valida")

        case "8":
            ejecucion = False
        case _:
            print("Ingreso una opcion no válida. Intente de nuevo")