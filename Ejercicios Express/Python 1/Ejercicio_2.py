def max_de_tres(uno, dos, tres):
    numeros = [uno, dos, tres]
    max     = numeros[0]
    for i in numeros:
        if max<i:
            max = i
    return max

uno  = int(input("Ingresar primer numero: "))
dos  = int(input("Ingresar segundo numero: "))
tres = int(input("Ingresar tercer numero: "))

print(max_de_tres(uno, dos, tres))