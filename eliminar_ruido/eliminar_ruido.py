# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 12:30:06 2022

@author: nehemias
"""

from PIL import Image 

def media_pixeles(pixeles, x, y, ancho, alto):
    #Pixeles vecinos (Si no existe el pixel se iguala a -1)
    pixel_izquierdo = pixeles[x-1, y] if x-1 >= 0 else -1
    pixel_derecho   = pixeles[x+1, y] if x+1 < ancho else -1
    
    pixel_superior  = pixeles[x, y-1] if y-1 >= 0 else -1
    pixel_inferior  = pixeles[x, y+1] if y+1 < alto else -1
    
    pixel_superior_izquierdo = pixeles[x-1, y-1] if x-1 >= 0 and y-1>=0 else -1
    pixel_superior_derecho   = pixeles[x+1, y-1] if x+1 < ancho and y-1>=0 else -1
    
    pixel_inferior_izquierdo = pixeles[x-1, y+1] if x-1 >= 0 and y+1< alto else -1
    pixel_inferior_derecho   = pixeles[x+1, y+1] if x+1 < ancho and y+1< alto else -1
    
    pixeles_vecinos = [pixel_superior_izquierdo, pixel_superior, pixel_superior_derecho,
                       pixel_izquierdo, pixel_derecho,
                       pixel_inferior_izquierdo, pixel_inferior, pixel_inferior_derecho]
    
    #Se eliminan los pixeles inexistentes de la lista
    pixeles_vecinos = list(filter(lambda a: a != -1, pixeles_vecinos))
    
    media_r, media_g, media_b = (0, 0, 0)
    
    for vecino in pixeles_vecinos:
        media_r += vecino[0]
        media_g += vecino[1]
        media_b += vecino[2]
        
    media = (int(media_r/len(pixeles_vecinos)), 
             int(media_g/len(pixeles_vecinos)), 
             int(media_b/len(pixeles_vecinos)))
    
    return media

def eliminar_ruido(mi_imagen, tolerancia):
    ancho, alto = mi_imagen.size
    pixeles = imagen.load()
    nueva_imagen = []
    
    for y in range(0, alto):
        for x in range(0, ancho):
            media_vecinos = media_pixeles(pixeles, x, y, ancho, alto)
            pixel_actual  = pixeles[x, y]
            
            #Diferencias entre la media y el pixel en cuestion
            #Con sus correspondientes valores absolutos
            diferencia_r  = abs(media_vecinos[0] - pixel_actual[0])
            diferencia_g  = abs(media_vecinos[1] - pixel_actual[1])
            diferencia_b  = abs(media_vecinos[2] - pixel_actual[2])
            
            #Si el pixel supera la tolerancia dada se igualará a la media
            #de pixeles vecinos
            if(diferencia_r < tolerancia and diferencia_g < tolerancia and  diferencia_b < tolerancia):
                nueva_imagen.append(pixel_actual)
            else:
                nueva_imagen.append(media_vecinos)
                
    return nueva_imagen

#Se pide ingresar por teclado la tolerancia que se tendrá
#al comparar un pixel con la media entre sus vecinos
imagen = Image.open("./imagen1.png")
tolerancia_aceptada = int(input("Ingresar toleracia con respecto a la media entre pixeles: "))

imagen.putdata(eliminar_ruido(imagen, tolerancia_aceptada))

imagen.show()
imagen.close()