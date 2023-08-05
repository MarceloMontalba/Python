# Ejercicio:
#   Crear una función contar_vocales(), que reciba una 
#   palabra y cuente cuantas letras "a" tiene, cuantas 
#   letras "e" tiene y así hasta completar todas las vocales.
#   Se puede hacer que el usuario sea quien elija la palabra.

def contar_vocales(cadena):
    contadores = [0,0,0,0,0]
    vocales    = "aeiouAEIOU"
    
    for i in cadena:
        if i in vocales and (i == "a" or i == "A"):
            contadores[0] += 1
        elif i in vocales and (i == "e" or i == "E"):
            contadores[1] += 1
        elif i in vocales and (i == "i" or i == "I"):
            contadores[2] += 1
        elif i in vocales and (i == "o" or i == "O"):
            contadores[3] += 1
        elif i in vocales and (i == "u" or i == "U"):
            contadores[4] += 1

    return contadores

palabra   = str(input("Ingresar palabra a analizar : "))
respuesta = contar_vocales(palabra)

print("=================================================================")
print("La palabra '%s' tiene el siguiente numero de vocales : "%palabra)
print("a : %d \ne : %d \ni : %d \no : %d \nu : %d"%tuple(respuesta))