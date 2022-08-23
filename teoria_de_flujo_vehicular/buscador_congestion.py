# -*- coding: utf-8 -*-
"""
Created on Sun Aug 21 20:05:33 2022

@author: nehemias
"""

import mysql.connector as mysql

def convertir_milisegundos_horas(milisegundos):
    horas    = int(milisegundos/3600000)           
    minutos  = int((milisegundos - horas*3600000)/60000)
    segundos = int((milisegundos - horas*3600000 - minutos*60000)/1000)
    
    #Se convertira cada variable a tipo cadena.
    #Si solo tienen un digito se les antepone un 0.
    horas    = str(horas) if len(str(horas))>1 else "0"+str(horas)
    minutos  = str(minutos) if len(str(minutos))>1 else "0"+str(minutos)
    segundos = str(segundos) if len(str(segundos))>1 else "0"+str(segundos)
    
    #Se retorna la hora en formato HH:MM:SS
    return "%s:%s:%s"%(horas, minutos, segundos)

fecha_interes = str(input("Ingresar el dia que desea Examinar (AAAA-MM-DD): "))

#Se analizan las 24 horas
horas = 0
while(horas<24):
    #Parte desde el minuto 0 y va saltando 15 minutos hasta cumplir
    #una hora (Todo en milisegundos). Se analizan tramos de 15 minutos.
    
    #milisegundo_inicio parte con 0 milisegundos, pero cuando se cumpla una hora
    #se debe pasar a la siguente, como ejemplo inicialmente de 00:00:00 se pasa a
    #01:00:00, es por ello que se suma el numero de horas * 36000000 milisegundos.
    #Esto mismo aplica para la misma suma realizada en el ciclo for.
    
    transito = []
    milisegundo_inicio = 0 + horas*3600000
    for milisegundo_fin in range(900000+horas*(3600000), 4500000+horas*(3600000), 900000):
        
        #Se consulta a la bd por vehiculos que transiten entre el periodo de tiempo y fecha
        #indicados. Lo que hace es un conteo de vehiculos por calle,sin repetir un mismo 
        #vehiculo en el conteo, sin embargo este mismo si puede estar presente
        #en el conteo de otra calle en este periodo de tiempo.
        
        bd       = mysql.connect(host="localhost", user="root", password="", database="gps2")
        cursor   = bd.cursor()
        consulta = """SELECT calle, COUNT(DISTINCT vehiculo) as flujo FROM datos 
                      WHERE fecha='%s' AND hora BETWEEN %s AND %s
                      GROUP BY calle;"""%(fecha_interes, milisegundo_inicio, milisegundo_fin)
        cursor.execute(consulta)
        
        #flujos almacena el volumen de vehiculos en las distintas calles cada 15 minutos.
        flujos = cursor.fetchall() 
        bd.close()

        #Se crea un diccionario con todas las calles disponibles en la base de datos.
        #Todas se inicializan con un numero de vehiculos 0.
        bd       = mysql.connect(host="localhost", user="root", password="", database="gps2")
        cursor   = bd.cursor()
        consulta = "SELECT DISTINCT calle, 0 from datos;"
        cursor.execute(consulta)
        calles   = dict((x,y) for x, y in cursor.fetchall())
        bd.close()
        
        #Se recorre cada una de las calles registradas en el tramo de tiempo X
        #para registrar ese valor en el diccionario de calles.
        for calle_registrada in flujos:
            calles[calle_registrada[0]] = calle_registrada[1]
        
        transito.append([milisegundo_inicio, milisegundo_fin, calles])

        milisegundo_inicio = milisegundo_fin

    #El arreglo transito tiene 4 diccionarios que son 4 tramos de tiempo de 
    #15 minutos. En donde cada diccionario tiene cada calle registrada en la bd
    #con el valor correspondiente de vehiculos en dicho tramo de tiempo.
    
    #Es aqui donde se utiliza la teoria de flujo vehicular en cada calle.
    for calle in transito[0][2]:
        #Se obtiene el volumne horario de la calle
        Q = 0
        for tramo in transito:
            Q += tramo[2][calle]
        
        #Solo me interesa ver los datos de una calle que fue recorrida en 
        #alguno de sus tramos de tiempo.
        if(Q != 0):
            print("_______________________________________________________________")
            print(calle)
            print("---------------------------------------------------------------")
            print("INTERVALOS DE TIEMPO DE FLUJOS:")
            
            for tramo in transito:
                print("    *%s-%s = %s Veh."%(convertir_milisegundos_horas(tramo[0]),
                                           convertir_milisegundos_horas(tramo[1]),
                                           tramo[2][calle]))
                
            print("VOLUMEN HORARIO(Q) = %s Veh/h."%Q)
            
            flujo_promedio = Q/(len(transito))
            print("FLUJO PROMEDIO = %s Veh/h."%flujo_promedio)            
            print("---------------------------------------------------------------")
            
            
            print("INTERVALOS CON CONGESTIÓN:")
            for tramo in transito:
                if(tramo[2][calle]>flujo_promedio):
                    print("    *%s-%s."%(convertir_milisegundos_horas(tramo[0]),
                                         convertir_milisegundos_horas(tramo[1])))
            
            print("\n")
    
    horas += 1