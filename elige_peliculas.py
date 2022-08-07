# -*- coding: utf-8 -*-
"""
Created on Sat Aug  6 19:29:17 2022

@author: nehemias
"""
from random import choice, shuffle

dreamworks = ["Shrek 2", "Shrek 3", "Shrek 4", "Megamente", "Pollitos en Fuga",
              "El camino hacia El Dorado", "El Espantatiburones", 
              "Spirit: El Corcel Indomable", "Wallace y Gromit: La batalla de los vegetales", 
              "Como entrenar a tu dragón 1", "Como entrenar a tu dragón 2",
              "Como entrenar a tu dragón 3", "El Origen de los guardianes",
              "Monstruos Vs Aliens", "Vecinos invasores"]

anime= ["Mi Vecino Totoro", "Perfect Blue", "El Castillo Ambulante", "Ghost in the Shell",
        "Vampire Hunter D", "Maquia: Una historia de amor inmortal", "Susurros del corazón",
        "El tiempo contigo", "El viento se levanta", "En este rincón del mundo"]

terror = ["Psicosis", "La Cabaña del terror", "Nosferatu", "El proyecto de la bruja de Blair",
          "Pesadilla en la calle Elm", "El Exorcista", "Los Extraños", "El Conjuro"]

peliculas = dreamworks + anime + terror


#Desordena la lista de peliculas 4 veces
for i in range(0, 4):
    shuffle(peliculas)

#Elige al azar 3 peliculas de la lista
while True:
    input("Presione 'Enter' para elegir.")
    print(''' 
    ======================================================================
        Peliculas Seleccionadas:
            1.%s.
            2.%s.
            3.%s.
    ======================================================================
          
    '''%(choice(peliculas), choice(peliculas), choice(peliculas)))
