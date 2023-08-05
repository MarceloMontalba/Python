# Ejercicio:
#   Escriba una función es_bisiesto() que determine si un 
#   año determinado es un año bisiesto.Un año bisiesto es 
#   divisible por 4, pero no por 100. También es divisible 
#   por 400
def es_bisiesto(year):
    if year%4 == 0 and year%400 == 0:
        return "El año ingresado es bisiesto"
    else:
        return "El año ingresado no es bisiesto"

year = int(input("Ingresar año a analizar : "))
print(es_bisiesto(year))