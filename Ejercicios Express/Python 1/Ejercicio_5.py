def sum(lista):
    acumulador = 0
    for i in lista:
        acumulador += i
    
    return acumulador

def multip(lista):
    acumulador = lista[0]
    for i in range(1, len(lista)):
        acumulador *= lista[i]
    
    return acumulador

lista = [3, 3, 4, 9, 23]

print("Resultado Suma: ", sum(lista))
print("Resultado Multiplicación", multip(lista))