from PIL import Image
import os,time,sys
import pygame
from pygame.locals import *
import serial

pygame.init()
foto = os.listdir('./Imagenes/')

se=serial.Serial(2,9600)

for i in range(len(foto)):
    s="separa"
    f= time.strftime("%d-%m-%y")
    h= time.strftime("%H:%M:%S")

    imagen=Image.open("./Imagenes/"+foto[i])
    t=str(imagen.size[0])+s+str(imagen.size[1])

    imagen=pygame.image.load("./Imagenes/"+foto[i])
    imagen=pygame.image.tostring(imagen,"RGB")
    imagen=t+s+f+s+h+s+imagen+s+foto[i]
    
    imagen=imagen.replace("\n","salto")
    imagen=imagen+"\n"
    
    se.write(imagen)
    print "Imagen "+foto[i]+" enviada."

