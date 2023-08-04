def superposicion(lista_1, lista_2):
    bandera = False
    for i in lista_1:
        for x in lista_2:
            if i == x:
                bandera = True

    return bandera

lista_1 = [1, 35, 64, 6]
lista_2 = [2, 40, 4]

print(superposicion(lista_1, lista_2))