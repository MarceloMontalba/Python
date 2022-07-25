import numpy
from numpy import array, matrix
import pygame as py, random as ra
from pygame.locals import *
from PIL import Image

nMIN_X1 = 45 ; nMAX_X1 = 337 ; nMIN_Y1 = 35; nMAX_Y1 = 267
nCLR_X1 = 520 ; nCLR_X2 = 570 ; nCLR_Y1 = 0; nCLR_Y2 = 70

class Mapper(object):

    def __init__(self,((IR_x1,IR_y1),(IR_x2,IR_y2),(IR_x3,IR_y3),(IR_x4,IR_y4)),\
                      ((SC_x1,SC_y1),(SC_x2,SC_y2),(SC_x3,SC_y3),(SC_x4,SC_y4))):

        A = array([
                   [IR_x1,IR_y1,1,0,0,0,-SC_x1*IR_x1,-SC_x1*IR_y1],
                   [0,0,0,IR_x1,IR_y1,1,-SC_y1*IR_x1,-SC_y1*IR_y1],
                   [IR_x2,IR_y2,1,0,0,0,-SC_x2*IR_x2,-SC_x2*IR_y2],
                   [0,0,0,IR_x2,IR_y2,1,-SC_y2*IR_x2,-SC_y2*IR_y2],
                   [IR_x3,IR_y3,1,0,0,0,-SC_x3*IR_x3,-SC_x3*IR_y3],
                   [0,0,0,IR_x3,IR_y3,1,-SC_y3*IR_x3,-SC_y3*IR_y3],
                   [IR_x4,IR_y4,1,0,0,0,-SC_x4*IR_x4,-SC_x4*IR_y4],
                   [0,0,0,IR_x4,IR_y4,1,-SC_y4*IR_x4,-SC_y4*IR_y4]
                  ])

        XP = array([SC_x1,SC_y1,SC_x2,SC_y2,SC_x3,SC_y3,SC_x4,SC_y4])
        p = numpy.linalg.solve(A,XP)
        self.H = matrix([
                         [ p[0],p[1],p[2] ],
                         [ p[3],p[4],p[5] ],
                         [ p[6],p[7],  1  ]
                        ])

    def Mapea(self,(x,y)):
        pt = [ [x],[y],[1] ]
        re = self.H * pt
        ze = re[2,0]
        return re[0,0]/ze,re[1,0]/ze

#---------------------------------------------------------------------
# Carga imagenes y convierte formato pygame
#---------------------------------------------------------------------
def Load_Image(sFile,transp=False):
    try: image = py.image.load(sFile)
    except py.error,message:
           raise SystemExit,message
    image = image.convert()
    if transp:
       color = image.get_at((0,0))
       image.set_colorkey(color,RLEACCEL)
    return image

#---------------------------------------------------------------------
# Pinta y Mapea los (X,Y) IR a (X,Y) PC
#---------------------------------------------------------------------
def Pinta_IR(mx,my,xp,yp):
    if mx > nMIN_X1 and mx < nMAX_X1:
       if my > nMIN_Y1 and my < nMAX_Y1:
          sc.blit(f2,(mx,my))
          sc.blit(f3,(xp,yp))
    return

#---------------------------------------------------------------------
# Dibuja y Mapea los (X,Y) IR a (X,Y) PC
#---------------------------------------------------------------------
def Draw_IR(imagen,w):
    a,f=imagen.get_size()
    for i in range(f):
        for j in range(a):
            color=imagen.get_at((j,i))
            xm,ym=w.Mapea((j,i))
            sc.fill(color,((xm,ym),(1,1)))
    return




#---------------------------------------------------------------------
# Main
#---------------------------------------------------------------------
py.init()
size = (900,600)
sc = py.display.set_mode(size)
py.display.set_caption("Demo coordenadas")
P1 = Load_Image('plantilla.jpg');P2 = Load_Image('plantilla.jpg')
f1 = Load_Image('tigre.jpg')
lOK = True
wi0=Mapper(
            ((0,0),(260-1,0),(260-1,195-1),(0,195-1)),
            ((45,34),(337,34),(337,267),(45,267))
			)
wi = Mapper(
            ((0,0),(260-1,0),(260-1,195-1),(0,195-1)),
            ((617,34),(648,34),(820,248),(458,248))
			)
wi2 = Mapper(
            ((0,0),(260-1,0),(260-1,195-1),(0,195-1)),
            ((82,340),(296,340),(345,507),(45,507))
	                )
wi3 =Mapper(
            ((0,0),(260-1,0),(260-1,195-1),(0,195-1)),
            ((423,335),(513,335),(849,507),(511,507))
	                )
while lOK:
 
 Mx,My = py.mouse.get_pos()
 Mx,My=wi0.Mapea((Mx,My))
 Xp,Yp = wi.Mapea((Mx,My))
 Xp2,Yp2=wi2.Mapea((Mx,My))
 Xp3,Yp3=wi3.Mapea((Mx,My))
 #print(Mx,My)
 #print(Xp,Yp)
 for e in py.event.get():
  if e.type == py.QUIT: lOK = False
 sc.blit(P2,(0,0))
 Draw_IR(f1,wi0)
 Draw_IR(f1,wi)
 Draw_IR(f1,wi2)
 Draw_IR(f1,wi3)
 py.display.flip()
py.quit()


