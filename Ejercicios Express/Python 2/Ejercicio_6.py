# Ejercicio:
#   Escribir un pequeño programa donde:
#   Se ingresa el año en curso.
#   Se ingresa el nombre y el año de nacimiento de tres personas.
#   Se calcula cuántos años cumplirán durante el año en curso.
#   Se imprime en pantalla.

year_actual = int(input("Ingresar año actual : "))

personas = []
for i in range(0, 3):
    nombre          = str(input("Ingresar nombre de la persona %s : "%str(i+1)))
    year_nacimiento = int(input("Ingresar fecha nacimiento de la persona %s : "%str(i+1)))
    personas.append([nombre, year_nacimiento])

print("====================================================================================")
for i in personas:
    print("%s tendrá la edad de %s años, el año %s."%(i[0], year_actual - i[1], year_actual))