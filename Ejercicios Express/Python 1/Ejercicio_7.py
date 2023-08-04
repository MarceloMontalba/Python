def es_palindromo(cadena):
    cadena_invertida = cadena[::-1]
    if(cadena == cadena_invertida):
        return True
    else: 
        return False

cadena = str(input("Ingresar cadena a analizar : "))
print(es_palindromo(cadena))