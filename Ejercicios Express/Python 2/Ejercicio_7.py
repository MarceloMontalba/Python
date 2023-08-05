# Ejercicio:
#   Definir una tupla con 10 edades de personas.
#   Imprimir la cantidad de personas con edades superiores a 20.
#   Puedes variar el ejercicio para que sea el usuario quien ingrese las edades.

def buscar_mayores(edades):
    contador = 0
    for i in edades:
        if i>20:
            contador += 1
    return contador

edades = []
for i in range(0, 10):
    edad = int(input("Ingresar edad de la persona %s : "%str(i+1)))
    edades.append(edad)

print("%d personas tienen edades mayores a los 20 años."%buscar_mayores(edades))