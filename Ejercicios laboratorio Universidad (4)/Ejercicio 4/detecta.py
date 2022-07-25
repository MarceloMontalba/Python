from PIL import Image
import pygame
from pygame.locals import *

pygame.init()
aux= True

imagen=Image.open("figuras.png")
ventana=pygame.display.set_mode(imagen.size)
pygame.display.set_caption("Figuras")

imagen=pygame.image.load("figuras.png")
cantidad=0
c=0

anterior=-1
arch=open("contornos.txt","wb")
colores=[(255,0,255),(255,201,14),(255,128,0),(255,174,201),(0,128,255),(181,230,29)]

while aux:
    ventana.blit(imagen,(0,0))
    for e in pygame.event.get():
      if e.type == QUIT:
          aux = False

    for color in colores:
        mascara = pygame.mask.from_threshold(imagen,color,(10,10,10))
        for Reg in mascara.connected_components(1000):
              xy = Reg.centroid()
              pygame.draw.line(imagen,(255,255,255),(xy[0]-8,xy[1]-8),(xy[0]+8,xy[1]+8))
              pygame.draw.line(imagen,(255,255,255),(xy[0]-8,xy[1]+8),(xy[0]+8,xy[1]-8))

              if(c<6):
                  caja=Reg.get_bounding_rects()
                  pygame.draw.rect(imagen,(255,255,255),caja[0],1)
                  
                  cont = Reg.outline()
                  pygame.draw.polygon(imagen,(255,255,255),cont,1)

                  for i in range(len(cont)):
                      arch.write("("+str(cont[i][0])+","+str(cont[i][1])+")")
                      anterior=i
        if (c<6):
            cantidad+=len(mascara.connected_components(1000))
        if (c==6):
            arch.close()
            print "Existen "+str(cantidad)+" figuras dentro de la imagen."
            
        c+=1
    pygame.display.flip()
