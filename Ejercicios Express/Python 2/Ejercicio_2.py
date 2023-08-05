# Ejercicio: 
#   Escribir una función mas_larga() que tome una lista 
#   de palabras y devuelva la mas larga.

def mas_larga(lista):
    cadena_elegida = lista[0]
    for i in lista:
        if len(i) > len(cadena_elegida):
            cadena_elegida = i
    return cadena_elegida

lista = ["pelota", "hola", "mundo", "aerodronomo", "computador"]
print(mas_larga(lista))