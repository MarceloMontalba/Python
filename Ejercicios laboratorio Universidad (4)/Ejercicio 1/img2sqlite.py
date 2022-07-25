def separa(i,foto):
    z= './fotos/' + foto
    imagen = Image.open(z)
    carga=imagen.load()

    rojo =   Image.new('RGB', (imagen.size[0],imagen.size[1]), "white")
    verde =  Image.new('RGB', (imagen.size[0],imagen.size[1]), "white")
    azul =   Image.new('RGB', (imagen.size[0],imagen.size[1]), "white")

    gris=imagen.convert("L")

    rojo.save("./rojo/rojo"+str(i)+".png")
    verde.save("./verde/verde"+str(i)+".png")
    azul.save("./azul/azul"+str(i)+".png")
    gris.save("./gris/gris"+str(i)+".png")

    rojo=Image.open("./rojo/rojo"+str(i)+".png")
    carga_r=rojo.load()

    verde=Image.open("./verde/verde"+str(i)+".png")
    carga_v=verde.load()

    azul=Image.open("./azul/azul"+str(i)+".png")
    carga_a=azul.load()


    for x in range(imagen.size[0]):
        for y in range(imagen.size[1]):
            carga_r[x,y]=(carga[x,y][0],0,0)
            carga_v[x,y]=(0,carga[x,y][1],0)
            carga_a[x,y]=(0,0,carga[x,y][2])

    rojo.save("./rojo/rojo"+str(i)+".png")
    verde.save("./verde/verde"+str(i)+".png")
    azul.save("./azul/azul"+str(i)+".png")

from PIL import Image
import serial,time
import pygame
from pygame.locals import *
import sqlite3 as sq

pygame.init()
s=serial.Serial(2,9600)
#---------------------------------------
crear_t=''' CREATE TABLE Fotos(
            id INTEGER PRIMARY KEY,
            fecha date,
            hora time,
            img blob,
            r blob,
            g blob,
            b blob,
            gris blob)
'''

conecta=sq.connect("Imagenes.db")
conecta.execute(crear_t)

cur=conecta.cursor()

#---------------------------------------

c=0
while 1:
    r=s.readline()[:-1].split("separa")
    
    imagen= r[4]
    imagen=imagen.replace("salto","\n")
    imagen=pygame.image.fromstring(imagen,(int(r[0]),int(r[1])),"RGB")

    pygame.image.save(imagen,"./fotos/"+r[5])

    separa(c,r[5])

    nueva=open("./fotos/"+r[5],"rb")
    nueva=nueva.read()
    
    rojo=open("./rojo/rojo"+str(c)+".png","rb")
    rojo=rojo.read()
    
    azul=open("./azul/azul"+str(c)+".png","rb")
    azul=azul.read()
    
    verde=open("./verde/verde"+str(c)+".png","rb")
    verde=verde.read()
    
    gris=open("./gris/gris"+str(c)+".png","rb")
    gris=gris.read()

    datos=[r[2],r[3],sq.Binary(nueva),sq.Binary(rojo),sq.Binary(verde),sq.Binary(azul),sq.Binary(gris)]
    insertar='''INSERT INTO Fotos (fecha, hora , img , r , g, b, gris)
                VALUES (?,?,?,?,?,?,?)''';
    cur.execute(insertar,datos)

    conecta.commit()
    c+=1
