def generar_n_caracteres(entero, caracter):
    auxiliar = caracter * entero
    return auxiliar

entero   = int(input("Ingresar entero : "))

#Nos aseguramos de solo tomar un caracter de una cadena
caracter = str(input("Ingresar caracter : "))[0:1]
print(generar_n_caracteres(entero, caracter))