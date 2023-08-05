# Ejercicio:
#   Escribir un programa que le diga al usuario que ingrese una cadena. 
#   El programa tiene que evaluar la cadena y decir cuantas letras 
#   mayúsculas tiene.
def contar_mayusculas(cadena):
    letras_mayusculas = "QWERTYUIOPASDFGHJKLÑZXCVBNM"
    contador          = 0

    for i in cadena:
        if i in letras_mayusculas:
            contador += 1   
    return contador

cadena = str(input("Ingresar cadena : "))
print("La cadena tiene %s letra/s mayuscula/s."%contar_mayusculas(cadena))