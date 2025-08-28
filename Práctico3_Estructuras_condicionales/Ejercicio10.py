#Ejercicio10

print("Ingrese en que hemisferio se encuentra: [N/S]")
hemis = input()
print("Ingrese en que numer de mes se encuentra: ")
mes = int(input())
print("Ingrese que numero de día: ")
dia = int(input())

norte_invierno = (mes == 12 and (dia >= 21)) or ((mes >= 1 and mes < 3) or (mes == 3 and dia <= 20))
norte_primavera = (mes == 3 and (dia >= 21)) or ((mes >= 4 and mes < 6) or (mes == 6 and dia <= 20))
norte_verano = (mes == 6 and (dia >= 21)) or ((mes >= 7 and mes < 9) or (mes == 9 and dia <= 20))
norte_otoño = (mes == 9 and (dia >= 21)) or ((mes >= 10 and mes < 12) or (mes == 12 and dia <= 20))


if hemis.lower() == "n":
    #Reviso si es Invierno, desde el 21 de diciembre hasta el 20 de marzo incluidos
    if norte_invierno:
        print(f"Es invierno")
    #Reviso si es primavera desde el 21 de marzo hasta el 20 de junio incluidos
    elif norte_primavera:
        print("Es primavera")
    elif norte_verano:
        print("Es verano")
    elif norte_otoño:
        print("Es otoño")
    
