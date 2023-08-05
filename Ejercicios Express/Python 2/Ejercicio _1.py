# Ejercicio:
#   La función max() del ejercicio 1 (primera parte) y la función 
#   max_de_tres() del ejercicio 2 (primera parte), solo van a funcionar 
#   para 2 o 3 números. Supongamos que tenemos mas de 3 números o no sabemos 
#   cuantos números son. Escribir una función max_in_list() que tome una 
#   lista de números y devuelva el mas grande.

def max_in_list(lista):
    if len(lista) <= 3:
        max = lista[0]
        for i in lista:
            if max<i:
                max = i
        return max
    else:
        return "Lista con demasiados elementos"

lista = [30, 40, 10]
print(max_in_list(lista))