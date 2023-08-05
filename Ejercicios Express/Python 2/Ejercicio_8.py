# Ejericio:
#   Definir una lista con un conjunto de nombres, imprimir la 
#   cantidad de comienzan con la letra a.
#   También se puede hacer elegir al usuario la letra a buscar.  
#   (Un poco mas emocionante)

def buscar_inicial(lista, inicial):
    contador = 0
    for i in lista:
        if i[0:1] == inicial:
            contador += 1
    
    return contador

lista   = ["pedro", "lucas", "juan", "maria", "marcos"]
inicial = str(input("Ingresar la inicial a buscar : "))[0:1]

print("Existe/n %d nombre/s que tiene/n la inicial %s."%(buscar_inicial(lista, inicial), inicial))