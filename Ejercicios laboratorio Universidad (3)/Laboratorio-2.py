from __future__ import division
from time import sleep
from visual import *
import math
import numpy as np
import random,time
import networkx as nx

#Definicion de ventana y plano a trabajar
WinM = display(title='Demo',x=050,y=000,width=2000,height=900,center=(0,0,0),background=(255,255,255))
Base = box(pos=(0,0,0),size=(1400,3,1400),color=color.yellow)
Base = box(pos=(0,0,0),size=(1600,2.9,1600),color=color.green)

def CrearNodos((cX,cZ),CLR):
    cilindro=cylinder(pos=(cX,-001.3,cZ), axis=(0,3,0), radius=5,color=CLR)
    
def Get_Pos_XY(a,b,p):
    aX = [] ; aY = []; aXY = [] ; aT = []
    aX1 = np.linspace(-a,b,p) ; aY1 = np.linspace(-a,b,p)
    for e in aX1: aX.append(int(e))
    for e in aY1: aY.append(int(e))

    for i in range(len(aY)):
        for j in range(len(aX)):
            aT.append((aX[j],aY[i]))
        aXY.append(aT)
        aT = []
    return aXY
        
def Crea_Robots((x,y)):
    miframe=frame(pos=(x,7,y))
    robot=box(frame=miframe,pos=(0,0,0),size=(30,15,30),color=color.blue)
    punto=cylinder(frame=miframe,pos=(0,7,0),axis=(0,4,0),radius=8,color=color.red)
    frontal=box(frame=miframe,pos=(0,1,11),size=(32,5,10),color=color.yellow)
    trasero=box(frame=miframe,pos=(0,1,-13),size=(32,5,5),color=color.yellow)
    return miframe

def Crea_Carros((x,y)):
    miframe2=frame(pos=(x,0,y))
    izquierdo1=cylinder(frame=miframe2, pos=(0+19,0,0-17),axis=(0,88,0),color=color.red)
    derecho1=cylinder(frame=miframe2,pos=(0-19,0,0-17),axis=(0,88,0),color=color.red)
    izquierdo2=cylinder(frame=miframe2,pos=(0+19,0,0+17),axis=(0,88,0),color=color.red)
    derecho2=cylinder(frame=miframe2,pos=(0-19,0,0+17),axis=(0,88,0),color=color.red)
    repisa1=box(frame=miframe2,pos=(0,88,0),size=(39,2,35),color=color.red)
    repisa2=box(frame=miframe2,pos=(0,78,0),size=(40,2,35),color=color.red)
    repisa3=box(frame=miframe2,pos=(0,68,0),size=(40,2,35),color=color.red)
    repisa4=box(frame=miframe2,pos=(0,58,0),size=(40,2,35),color=color.red)
    repisa5=box(frame=miframe2,pos=(0,48,0),size=(40,2,35),color=color.red)
    repisa6=box(frame=miframe2,pos=(0,38,0),size=(40,2,35),color=color.red)
    repisa7=box(frame=miframe2,pos=(0,28,0),size=(40,2,35),color=color.red)
    repisa8=box(frame=miframe2,pos=(0,18,0),size=(40,2,35),color=color.red)
    return miframe2

#Funcion que crea una matriz llena con las posiciones representadas "A0,A1,A2...."
def Crea_Pos():
    pos=[[],[],[],[],[],[],[],[],[],[],[]]

    for i in range(0,11):
        for x in range(0,11):
            if i==0:pos[i].append("A"+str(x))
            if i==1:pos[i].append("B"+str(x))
            if i==2:pos[i].append("C"+str(x))
            if i==3:pos[i].append("D"+str(x))
            if i==4:pos[i].append("E"+str(x))
            if i==5:pos[i].append("F"+str(x))
            if i==6:pos[i].append("G"+str(x))
            if i==7:pos[i].append("H"+str(x))
            if i==8:pos[i].append("I"+str(x))
            if i==9:pos[i].append("J"+str(x))
            if i==10:pos[i].append("K"+str(x))
    return pos

#Funcion que crea un diccionario con los movimientos posibles de cada punto
def Crea_Mov():
    pos=Crea_Pos()
    dic={}
    datos=[]
    
    for i in range(0,11):
        for x in range(0,11):
            try: datos.append(pos[i][x-1])
            except:""
            
            try: datos.append(pos[i][x+1])
            except:""

            try: datos.append(pos[i-1][x])
            except:""

            try: datos.append(pos[i+1][x])
            except:""

            dic[pos[i][x]]=datos
            datos=[]
            
    #Este segmento quita las posiciones "K" dentro de los mivimientos posibles de "A"
    for i in range(0,11):
        if(i!=10): dic["A"+str(i)].pop(2)
        else: dic["A"+str(i)].pop(1)

    #Este segmento no deja que de un punto "0" pase al punto "10"
    letras="ABCDEFGHIJK"
    cont=0
    while (cont<11):
        dic[letras[cont:cont+1]+str(0)].pop(0)
        cont+=1

    for i in range(0,11):
        datos=dic["A"+str(i)]
        for x in range(0,11):
            try: datos.remove("A"+str(x))
            except: ""
                  
    return dic

#Funcion que crea un diccionario con las coordenadas de cada uno de los puntos
dCooLet={}
def Crea_Coo():
    global dCooLet
    pos=Crea_Pos()

    dic={}
    for i in range(0,11):
        for x in range(0,11):
            dic[pos[i][x]]=aMapa[i][x]
            dCooLet[aMapa[i][x]]=pos[i][x]
    return dic

def Ruta(movimientos):
    G=nx.Graph()
    letras="ABCDEFGHIJK"
    cont=0

    while cont<11:
        for i in range(0,11):
            mover=movimientos[letras[cont:cont+1]+str(i)]
            for x in mover:
                G.add_edge(letras[cont:cont+1]+str(i),x)
        cont+=1
    return G

aMapa = Get_Pos_XY(600,600,11)

for i in range(len(aMapa)):
    for j in range(len(aMapa[i])):
        if i==0 and j>=2 and j<=8: 
            CrearNodos(aMapa[i][j],color.blue)
        if i!=0:
            CrearNodos(aMapa[i][j],color.red)

r1= Crea_Robots(aMapa[0][2]); r2=Crea_Robots(aMapa[0][3]); r3=Crea_Robots(aMapa[0][4])
r4= Crea_Robots(aMapa[0][5]); r5=Crea_Robots(aMapa[0][6]); r6=Crea_Robots(aMapa[0][7])
r7=Crea_Robots(aMapa[0][8])


#llena la matriz ocupado con las posiciones que los esten o no, para saber cuales estan en uso
ocupado=[[],[],[],[],[],[],[],[],[],[],[]]
for i in range(0,11):
    for x in range(0,11):
        ocupado[i].append([aMapa[i][x],"NO"])

#Crear Carros
cont=0
while(cont<7):
    fila=random.randint(1,10)
    columna=random.randint(0,10)

    if (cont==0):
        if(ocupado[fila][columna][1]=="NO"):c1=Crea_Carros(aMapa[fila][columna]);ocupado[fila][columna][1]="SI"; cont+=1
    if (cont==1):
        if (ocupado[fila][columna][1]=="NO"):c2=Crea_Carros(aMapa[fila][columna]);ocupado[fila][columna][1]="SI"; cont+=1
    if (cont==2):
        if (ocupado[fila][columna][1]=="NO"):c3=Crea_Carros(aMapa[fila][columna]);ocupado[fila][columna][1]="SI"; cont+=1
    if (cont==3):
        if (ocupado[fila][columna][1]=="NO"):c4=Crea_Carros(aMapa[fila][columna]);ocupado[fila][columna][1]="SI"; cont+=1
    if (cont==4):
        if (ocupado[fila][columna][1]=="NO"):c5=Crea_Carros(aMapa[fila][columna]);ocupado[fila][columna][1]="SI"; cont+=1
    if (cont==5):
        if (ocupado[fila][columna][1]=="NO"):c6=Crea_Carros(aMapa[fila][columna]);ocupado[fila][columna][1]="SI"; cont+=1
    if (cont==6):
        if (ocupado[fila][columna][1]=="NO"):c7=Crea_Carros(aMapa[fila][columna]);ocupado[fila][columna][1]="SI"; cont+=1

def dirigir(robots,carros):
    R_elegidos=[]
    C_elegidos=[]
    
    for i in range(0,len(robots)):
        R_elegidos.append(i)
    for i in range(0,len(carros)):
        C_elegidos.append(i)

    random.shuffle(R_elegidos)
    random.shuffle(C_elegidos)

    pares=[]
    for i in range(0,len(R_elegidos)):
        for x in range(0,len(C_elegidos)):
            if(R_elegidos[i]==C_elegidos[x]):
                pares.append([robots[i],carros[x]])
    return pares

def Nuevas_Rutas(robots,grafo,dic_let):
    letras="ABCDEFGHIJK"
    
    m_carro=[]
    for i in range(0,len(robots)):
        aleatorio=random.randint(1,10)
        aleatorio2=random.randint(1,10)
        m_carro.append(nx.shortest_path(grafo,dic_let[(robots[i].pos[0],robots[i].pos[2])],letras[aleatorio2:(aleatorio2+1)]+str(aleatorio)))

    return m_carro

def Busca_carro(N_robots,N_carros,grafo):
    eleccion=dirigir(N_robots,N_carros)
    rutas=[]
    for i in range(0,len(eleccion)):
        robot=dCooLet[(eleccion[i][0].pos[0],eleccion[i][0].pos[2])]
        carro=dCooLet[(eleccion[i][1].pos[0],eleccion[i][1].pos[2])]
        rutas.append(nx.shortest_path(grafo,robot,carro))
    return rutas

def Crea_frame(robots,carros):
    for i in range(0,len(carros)):
        for x in range(0,len(robots)):
            if (carros[i].pos[0],carros[i].pos[2])==(robots[x].pos[0],robots[x].pos[2]):
                carros[i].pos=(0,0,0)
                carros[i].frame=robots[x]

def Volver(robots,grafo,rutas):
    dic_coo=Crea_Coo()
    
    ruta_larga=0
    for x in rutas:
        if len(x)>ruta_larga:
            ruta_larga=len(x)

    for x in range(0,ruta_larga):
        contador=4
        i=0
        while i<len(robots):
            try:seguir=rutas[i][x]
            except:seguir=rutas[i][len(rutas[i])-1]
            
            coordenada=dic_coo[seguir]
        
            if(robots[i].pos[0]!=coordenada[0] and robots[i].pos[0]<coordenada[0]):
                robots[i].pos=(robots[i].pos[0]+30,robots[i].pos[1],robots[i].pos[2])
                sleep(0.0001)

            if(robots[i].pos[2]!=coordenada[1] and robots[i].pos[2]<coordenada[1]):
                robots[i].pos=(robots[i].pos[0],robots[i].pos[1],robots[i].pos[2]+30)
                sleep(0.0001)
                 
            if(robots[i].pos[0]!=coordenada[0] and robots[i].pos[0]>coordenada[0]):
                robots[i].pos=(robots[i].pos[0]-30,robots[i].pos[1],robots[i].pos[2])
                sleep(0.0001)

            if(robots[i].pos[2]!=coordenada[1] and robots[i].pos[2]>coordenada[1]):
                robots[i].pos=(robots[i].pos[0],robots[i].pos[1],robots[i].pos[2]-30)
                sleep(0.0001)

            i+=1
            if(i==len(robots) and contador!=0):
                contador-=1
                i=0
    
contador_b=0
def baterias(robots,grafo):
    global contador_b
    contador_b+=1
    rutas=[]
    rutas2=[]
    print contador_b
    if(contador_b==30):
        for i in range(len(robots)):
            rutas.append(nx.shortest_path(grafo,dCooLet[(robots[i].pos[0],robots[i].pos[2])],"A"+str(i+2)))
            rutas2.append(nx.shortest_path(grafo,"A"+str(i+2),dCooLet[(robots[i].pos[0],robots[i].pos[2])]))

        Volver(robots,grafo,rutas)
        sleep(3)
        Volver(robots,grafo,rutas2)
        contador_b=0

mueve_carro=0
def Mover_Robot(robots,carros,rutas,grafo):
    global mueve_carro
    dic_coo=Crea_Coo()
    
    ruta_larga=0
    for x in rutas:
        if len(x)>ruta_larga:
            ruta_larga=len(x)

    for x in range(0,ruta_larga):
        contador=4
        i=0
        while i<len(robots):
            try:seguir=rutas[i][x]
            except:seguir=rutas[i][len(rutas[i])-1]
            
            coordenada=dic_coo[seguir]
        
            if(robots[i].pos[0]!=coordenada[0] and robots[i].pos[0]<coordenada[0]):
                robots[i].pos=(robots[i].pos[0]+30,robots[i].pos[1],robots[i].pos[2])
                sleep(0.0001)

            if(robots[i].pos[2]!=coordenada[1] and robots[i].pos[2]<coordenada[1]):
                robots[i].pos=(robots[i].pos[0],robots[i].pos[1],robots[i].pos[2]+30)
                sleep(0.0001)
                 
            if(robots[i].pos[0]!=coordenada[0] and robots[i].pos[0]>coordenada[0]):
                robots[i].pos=(robots[i].pos[0]-30,robots[i].pos[1],robots[i].pos[2])
                sleep(0.0001)

            if(robots[i].pos[2]!=coordenada[1] and robots[i].pos[2]>coordenada[1]):
                robots[i].pos=(robots[i].pos[0],robots[i].pos[1],robots[i].pos[2]-30)
                sleep(0.0001)

            i+=1
            if(i==len(robots) and contador!=0):
                contador-=1
                i=0
        baterias(robots,grafo)

    Crea_frame(robots,carros)

    if mueve_carro==0:
        mueve_carro+=1
        nueva_r=Nuevas_Rutas(robots,grafo,dCooLet)
        Mover_Robot(robots,carros,nueva_r,grafo)

    if mueve_carro==1:
        mueve_carro=0
        for i in range(0,len(carros)):
            carros[i].pos=(robots[i].pos[0],0,robots[i].pos[2])
            carros[i].frame=frame()
        rutas=Busca_carro(N_robots,N_carros,grafo)
        Mover_Robot(N_robots,N_carros,rutas,grafo)

                
mov=Crea_Mov()
coo=Crea_Coo()
grafo=Ruta(mov)

N_robots=[r1,r2,r3,r4,r5,r6,r7]
N_carros=[c1,c2,c3,c4,c5,c6,c7]

rutas=Busca_carro(N_robots,N_carros,grafo)
Mover_Robot(N_robots,N_carros,rutas,grafo)

while true:
    rate(300)

