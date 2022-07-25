# -*- coding: utf-8 -*-
from PIL import Image
import math
import os

a=os.listdir('./vocales')

def momento(Imagen, p, q):
    Mpq = 0.0
    height, width = Imagen.size
    for v in range(height):
        for u in range(width):
            if (Imagen.getpixel((v,u)) != background):
                Mpq += math.pow(v, p) * math.pow(u, q)
    return Mpq


def momentocentral(Imagen ,p , q):
    m00  = momento(Imagen, 0, 0)
    xCtr = momento(Imagen, 1, 0) /m00
    yCtr = momento(Imagen, 0, 1) /m00
    cMpq = 0.0
    height, width = Imagen.size
    for v in range(height):
        for u in range(width):
            if (Imagen.getpixel((v,u)) != background):
                cMpq += math.pow(v - yCtr, p) * math.pow(u - xCtr, q)
    return cMpq
    
def U(Imagen, p, q):
    m00 = momento(Imagen,0 , 0)
    norm = math.pow(m00, (p + q + 2)/ 2)
    valor= momentocentral(Imagen, p , q)/ norm
    return valor

for i in a:
    Imagen = Image.open('./vocales/'+i)
    background = 0
    
    H1 = U(Imagen,2,0) + U(Imagen,0,2)
    H2 = (U(Imagen,2,0)-U(Imagen,0,2))**2 + 4*(U(Imagen,1,1))**2
    H3 = (U(Imagen,3,0) - 3*(U(Imagen,1,2)))**2  + (3*U(Imagen,2,1) - U(Imagen,0,3))**2
    H4 = ((U(Imagen,3,0) + U(Imagen,1,2))**2 + (U(Imagen,2,1) + U(Imagen,0,3))**2)
    H5 = (U(Imagen,3,0) - 3*U(Imagen,1,2)) * (U(Imagen,3,0) + U(Imagen,1,2)) * ((U(Imagen,3,0) + U(Imagen,1,2))**2 - 3*(U(Imagen,2,1)+U(Imagen,0,3))**2) + (3*U(Imagen,2,1) - U(Imagen,0,3)) * (U(Imagen,2,1) + U(Imagen,0,3)) * (3*(U(Imagen,3,0) + U(Imagen,1,2))**2 - (U(Imagen,2,1) - U(Imagen,0,3))**2)
    H6 = (U(Imagen,2,0)- U(Imagen,0,2)) * ((U(Imagen,3,0) + U(Imagen,1,2))**2 -(U(Imagen,2,1)+U(Imagen,0,3))**2) +4*U(Imagen,1,1) * (U(Imagen,3,0) + U(Imagen,1,2))* (U(Imagen,2,1) +U(Imagen,0,3))
    H7 = (3*U(Imagen,2,1) - U(Imagen,0,3)) * (U(Imagen,3,0) + U(Imagen,1,2)) * ((U(Imagen,3,0) + U(Imagen,1,2))**2 + 3*(U(Imagen,2,1) + U(Imagen,0,3))**2 ) + (3*U(Imagen,1,2) - U(Imagen,3,0)) * (U(Imagen,2,1) + U(Imagen,0,3)) * (3*(U(Imagen,3,0) + U(Imagen,1,2))**2 - (U(Imagen,2,1) +U(Imagen,0,3))**2)

    print i[0]+i[1]
    print "-----------------------"
    print H1
    print H2
    print H3
    print H4
    print H5
    print H6
    print H7
    print "-----------------------"












