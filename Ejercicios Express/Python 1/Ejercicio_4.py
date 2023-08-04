def encuentra_vocales(caracter):
    vocales = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"] 
    if(caracter in vocales):
        return True
    else:
        return False

#Si es una cadena de mas de 1 caracter la truncara solo al primero
caracter = str(input("Ingresar un caracter: "))[0:1]
print(encuentra_vocales(caracter))