# -*- coding: utf-8 -*-

#Programa que dado un tiempo por el usuario en mili segundos , es capaz
#de sumar o restar este tiempo al ya establecido en un archivo SRT de
#subtítulos, de manera que ajusta estos tiempos acorde al video del que
#se dispone, quitando un posible desfase de aparición de estos con
#respecto a la imagen que se muestra.

def deHoraAMilisegundo(horas):
    return ((horas*(60.0/1.0))*(60.0/1.0))*(1000.0/1.0)

def deMinutoAMilisegundo(minutos):
    return (minutos*(60.0/1.0))*(1000/1.0)

def deSegundoAMilisegundo(segundos):
    return segundos*(1000.0/1.0)

def convertirAFormatoDeHoras(tiempoTotal):
    milisegundos=0
    segundos=0
    minutos=0
    horas=0

    #Se obtienen milisegundos y segundos en sus respectivos formatos
    #en sus respectivas variables.
    
    cont=0
    while cont<1:
        if tiempoTotal-1000>=0:
            segundos+=1
            tiempoTotal-=1000
        else:
            milisegundos=int(tiempoTotal)
            cont=1

    #Se obtienen los minutos y se almacenan en su respectiva variable
    #descontando este tiempo de la variable segundos.
    cont=0
    while cont<1:
        if segundos-60>=0:
            minutos+=1
            segundos-=60
        else:
            cont=1

    #Se obtienen las horas y se almacenan en su respectiva variable
    #descontando este tiempo de la variable minutos.
    cont=0
    while cont<1:
        if minutos-60>=0:
            horas+=1
            minutos-=60
        else:
            cont=1

    #Retornar tiempo a formato HH:MM:SS,mm   
    milisegundos=str(milisegundos)
    cont=0
    while cont<1:
        if len(milisegundos)<3:
            milisegundos="0"+milisegundos
        else:
            cont=1

    segundos=str(segundos)
    if len(segundos)<2:
        segundos="0"+segundos

    minutos=str(minutos)
    if len(minutos)<2:
        minutos="0"+minutos

    horas=str(horas)
    if len(horas)<2:
        horas="0"+horas
        
    return(horas+":"+minutos+":"+segundos+","+milisegundos)

ruta=input("Ingresar ruta del archivo SRT: ")    
operacion=input("Ingresar la operacion que quiere realizar(+ o -): ")
tiempoExtra=int(input("Ingresar tiempo en milisegundos: "))
print("===================================================================")

#Si el archivo no está codificado en formato utf-8, se procede a abrir
#con esta codificación.
try: 
    archivo=open(ruta,"r")
    arregloDatos=archivo.read().split("\n")
except:
    archivo=open(ruta,"r", encoding="utf-8")
    arregloDatos=archivo.read().split("\n") 
archivo.close()

contSubtitulos=0
for i in range(0,len(arregloDatos)):
    if len(arregloDatos[i])==29 and arregloDatos[i][13:16]=="-->":
        #Se obtienen Horas, Minutos, Segundos y Milisegundos desde que inicia
        #hasta que termina de mostrarse el subtitulo. Estos datos son convertidos
        #a milisegundos.
        inicioHoras        =deHoraAMilisegundo(float(arregloDatos[i][0:2]))
        inicioMinutos      =deMinutoAMilisegundo(float(arregloDatos[i][3:5]))
        inicioSegundos     =deSegundoAMilisegundo(float(arregloDatos[i][6:12].split(",")[0]))
        inicioMilisegundos =float(arregloDatos[i][6:12].split(",")[1])

        finHoras        =deHoraAMilisegundo(float(arregloDatos[i][17:19]))
        finMinutos      =deMinutoAMilisegundo(float(arregloDatos[i][20:22]))
        finSegundos     =deSegundoAMilisegundo(float(arregloDatos[i][23:29].split(",")[0]))
        finMilisegundos =float(arregloDatos[i][23:29].split(",")[1])

        #Nuevo tiempo inicial total dado en milisegundos restando o sumando
        #tiempo dependiendo de lo que eligió el usuario.
        if operacion=="+":
            tiempoInicio = inicioHoras+inicioMinutos+inicioSegundos+inicioMilisegundos+tiempoExtra
        if operacion=="-":
            tiempoInicio = inicioHoras+inicioMinutos+inicioSegundos+inicioMilisegundos-tiempoExtra

        #Nuevo tiempo final total dado en milisegundos restando o sumando
        #tiempo dependiendo de lo que eligió el usuario.
        if operacion=="+":
            tiempoFin = finHoras+finMinutos+finSegundos+finMilisegundos+tiempoExtra
        if operacion=="-":
            tiempoFin = finHoras+finMinutos+finSegundos+finMilisegundos-tiempoExtra

        arregloDatos[i]=convertirAFormatoDeHoras(tiempoInicio)+" --> "+convertirAFormatoDeHoras(tiempoFin)
        contSubtitulos+=1

#Guardando nuevo archivo
try: 
    archivo=open(ruta,"w")
    archivo.write("\n".join(arregloDatos))
except: 
    archivo=open(ruta,"w", encoding="utf-8")
    archivo.write("\n".join(arregloDatos))  
archivo.close()

print("Listo!")
print("Subtitulos Modificados: ",contSubtitulos)
