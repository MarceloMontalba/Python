def max(uno, dos):
    if uno>dos:
        return uno
    else:
        return dos
    
uno = int(input("Ingresar primer número  : "))
dos = int(input("Ingresar segundo número : "))

if(uno!=dos):
    print("El mayor número es :", max(uno, dos))
else:
    print("Ambos números ingresados son iguales y su valor es: ", uno)