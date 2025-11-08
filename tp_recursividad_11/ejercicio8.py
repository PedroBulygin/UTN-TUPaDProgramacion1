"""
Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un
número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces
aparece ese dígito dentro del número.
"""

def contar_digito(numero, digito):
    num_str = str(numero)
    digito_str = str(digito)
    if len(num_str) == 0:
        return 0
    conteo = 0
    if num_str[0] == digito_str:
        conteo = 1
    resto_cadena = num_str[1:]
    return conteo + contar_digito(resto_cadena, digito)

numero = int(input("Ingrese el numero: "))
digito = int(input("Ingrese el digito: "))

print(f"El digito {digito} aparece {contar_digito(numero, digito)} veces en el numero {numero}")