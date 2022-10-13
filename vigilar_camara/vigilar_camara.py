# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 15:29:27 2022

@author: chelo
"""

import cv2
from datetime import datetime
import os, time

while True: 
    #Se crea el directorio del dia si no existe
    momento = datetime.now()
    dia     = momento.strftime("%d-%m-%Y")
    
    #Se crea el directorio del dia si no existe
    if not os.path.exists("./capturas/%s"%dia):
        os.makedirs("./capturas/%s"%dia)
    
    #Se abre la camara 0
    camara = cv2.VideoCapture(0)
    
    #Dimensiones de la imagen
    camara.set(cv2.CAP_PROP_FRAME_WIDTH, 2560)   #Ancho
    camara.set(cv2.CAP_PROP_FRAME_HEIGHT, 1440)  #Alto
    
    #Capturar imagen
    ret, frame = camara.read()
    
    #Guardar imagen que está almacenada en frame con el nombre
    #de la hora en que se registró
    hora = momento.strftime("%H%M%S")
    cv2.imwrite("./capturas/%s/%s.jpg"%(dia,hora), frame)
    
    #Libera la camara
    camara.release()
    
    #Un sleep de 5 segundos
    time.sleep(3)