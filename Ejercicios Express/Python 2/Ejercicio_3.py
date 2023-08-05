# Ejercicio:
#   Escribir una función filtrar_palabras() que tome una lista 
#   de palabras y un entero n, y devuelva las palabras que tengan 
#   mas de n caracteres.

def filtrar_palabras(lista, n):
    nueva_lista = []
    for i in lista:
        if len(i) > n:
            nueva_lista.append(i)

    return nueva_lista

lista = ["hola", "mundo", "television", "gatos", "perros"]
print(filtrar_palabras(lista, 5))