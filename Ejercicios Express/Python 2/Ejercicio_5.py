# Ejercicio:
#   Construir un pequeño programa que convierta números binarios en enteros.
def convertir_binarios(binario):
    numero   = str(binario)[::-1]
    contador = 1
    entero   = 0

    for i in numero:
        entero   += int(i)*contador
        contador += contador
    return entero

numero = 11101
print(convertir_binarios(numero))
