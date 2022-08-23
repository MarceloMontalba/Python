# -*- coding: utf-8 -*-
"""
Created on Sun Aug 21 00:36:46 2022

@author: nehemias
"""

import mysql.connector as mysql
import requests
import json


#Se consulta por todos los datos de la base de datos inicial
bd       = mysql.connect(host="localhost", user="root", password="", database="gps")
cursor   = bd.cursor()
consulta = "SELECT * FROM datos ORDER BY fecha ASC, hora ASC;"

cursor.execute(consulta)
datos_obtenidos = cursor.fetchall() 
bd.close()

#Sentencia SQL que será utilizada para rellenar la nueva bd.
inserta = """INSERT INTO datos(npk, vehiculo, latitud, longitud, calle, velocidad, angulo, fecha, hora) 
             VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s);"""

for auto in datos_obtenidos:
    #Se abre la nueva base de datos para posteriormente insertar información de interes.
    bd      = mysql.connect(host="localhost", user="root", password="", database="gps2")
    cursor  = bd.cursor()
    
    #Parametros utilizados para consultar la API de MapQuest Developer
    parametros = {
        "key" : "Kl30hgme0FYT8dqBumN9ttnuE5zlkNEN",
        "location" : "%s, %s"%(auto[2], auto[3])
    }

    #Se invoca a la API de Geolocalización con los
    #parametros de latitud y longitud dados
    respuesta = requests.get("http://www.mapquestapi.com/geocoding/v1/reverse", params = parametros)
    autos     = json.loads(respuesta.text)["results"]
    calle     = autos[0]["locations"][0]["street"]
    
    #El campo de hora se almacenará en milisegundos
    hora = auto[7].split(":")
    hora = int(hora[0])*3600000 + int(hora[1])*60000 + int(hora[2])*1000

    #Se crea la respectiva tupla que será una nueva fila
    fila  = (auto[0], auto[1], auto[2], auto[3], calle, auto[4], auto[5], auto[6], hora)
    
    cursor.execute(inserta, fila)
    bd.commit()
    bd.close()
    
    print("FILA INSERTADA : ", fila)
    print("===========================================================\n")
