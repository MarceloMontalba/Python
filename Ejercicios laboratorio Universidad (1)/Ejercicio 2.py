# -*- coding: utf-8 -*-
import PIL
import pygame
from pygame.locals import *
import time
from PIL import Image
from numpy import array , dot, uint8

def Map(AZUL):
    return (((AZUL-0)*(25.9-17.1)/(255-0))+17.1)
def Cuadro_negro():
    for i in range(34):
        for j in range(134):
            screen.fill((0,0,0,255), ((j,i),(10,10)))
def ImageToPix(img):
    img = Image.open(img)
    img = img.convert('RGB')
    w,h=img.size
    data=img.getdata()
    pixelist = array(data,uint8)
    pixelist=pixelist.reshape((w,h,3))
    return pixelist


class Text:
    def __init__(self, FontName = None, FontSize = 30):
        pygame.font.init()
        self.font = pygame.font.Font(FontName, FontSize)
        self.size = FontSize

    def render(self, surface, text, color, pos):
        text = unicode(text, "UTF-8")
        x, y = pos
        for i in text.split("\r"):
            surface.blit(self.font.render(i, 1, color), (x, y))
            y += self.size 

def colorpx(screen,color1):
    for i in range(400):
        for j in range(600):
           r,g,b,a = screen.get_at((j,i))
           black=(0,0,0,255)
           if(r<color1[0]+10 and g<color1[1]+10 and b<color1[2]+10 and r>color1[0]-10 and g>color1[1]-10 and b>color1[2]-10 ):
               screen.fill((r,g,b,a),((j+600,i), (1,1)))
           else:
               screen.fill(black,((j+600,i), (1,1)))
            
    
screen = pygame.display.set_mode((1200,400))
pygame.display.set_caption("Ejercicio 2")
text=Text()
img=pygame.image.load('F6.png')
img=pygame.transform.scale(img, (600, 400))
img=img.convert()
screen.blit(img,(0,0))
Cuadro_negro()





while True:
    pygame.display.flip()
    if(pygame.mouse.get_pressed()==(1,0,0)):
        c=ImageToPix('F6.png')
        Cuadro_negro()
        color = screen.get_at(pygame.mouse.get_pos())[1]
        color1= screen.get_at(pygame.mouse.get_pos())
        colorpx(screen,color1)
        text.render(screen,str(round(Map(color),2))+"°",(255,255,255),(10,10))
        time.sleep(1)
    
    for eventos in pygame.event.get():
        if eventos.type == QUIT:
            sys.exit(0)


