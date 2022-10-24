# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 12:51:57 2022

@author: chelo
"""

import mysql.connector as mysql
import requests, json
    
#Funcion encargada de insertar posicion calles
def insertar_posicion(id_calle, latitud_calle, longitud_calle):
    #Se consulta si la posicion especifica de la calle
    #ya está insertada en la tabla "posicion_calles".   
    bd = mysql.connect(host="localhost", 
                       user="root", 
                       password="", 
                       database="gps_datos")
    cursor   = bd.cursor()
    consulta = '''SELECT * FROM posicion_calles WHERE id_calle=%s AND 
                  latitud=%s AND longitud=%s;'''
                  
    cursor.execute(consulta%(id_calle, latitud_calle, longitud_calle))
    respuesta = cursor.fetchall()
    insertada = len(respuesta)
    bd.close()
    
    if insertada == 0:  
        #Se inserta la posicion de la calle
        bd = mysql.connect(host="localhost", 
                           user="root", 
                           password="", 
                           database="gps_datos")
        cursor   = bd.cursor()
        consulta = """INSERT INTO posicion_calles(id_calle, latitud, longitud) 
                      VALUES(%s, %s, %s)"""
        
        datos = (id_calle, latitud_calle, longitud_calle)
        cursor.execute(consulta, datos)
        bd.commit()
        bd.close()
        
        print("POSICIÓN INSERTADA")
        print("====================================================")
        print("ID CALLE: ", id_calle)
        print("LATITUD: ", latitud_calle)
        print("LONGITUD: ", longitud_calle)
        print("____________________________________________________\n")
        
        #Se consulta por el id de la posicion de la calle
        #para posteriormente retornarlo
        bd = mysql.connect(host="localhost", 
                           user="root", 
                           password="", 
                           database="gps_datos")
        cursor   = bd.cursor()
        consulta = '''SELECT id FROM posicion_calles WHERE 
                      id_calle=%s AND latitud=%s AND longitud=%s'''
                      
        cursor.execute(consulta%(id_calle, latitud_calle, longitud_calle))
        respuesta = cursor.fetchall()[0][0]
        bd.close()
        
        return respuesta
        
    else:
        #Se retorna el id de la posicion que ya estaba creada
        return respuesta[0][0]

#Se crea la nueva base de datos si esque no existe
bd = mysql.connect(host="localhost", 
                   user="root", 
                   password="")

cursor = bd.cursor()
consulta = "CREATE DATABASE IF NOT EXISTS gps_datos"
cursor.execute(consulta)
bd.close()

#Creacion de las tablas de la nueva base de datos llamada "gps_datos"
bd = mysql.connect(host="localhost", 
                   user="root", 
                   password="", 
                   database="gps_datos")

cursor = bd.cursor()
consultas_creacion = ["""
            CREATE TABLE IF NOT EXISTS calles(
                id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY, 
                calle VARCHAR(90), 
                ciudad VARCHAR(50), 
                region VARCHAR(50));
            """,
            """
            CREATE TABLE IF NOT EXISTS posicion_calles(
                id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY, 
                id_calle INT UNSIGNED, 
                latitud DOUBLE, 
                longitud DOUBLE, 
                FOREIGN KEY(id_calle) REFERENCES calles(id));
            """,
            """
            CREATE TABLE IF NOT EXISTS autos(
                id BIGINT UNSIGNED PRIMARY KEY AUTO_INCREMENT, 
                id_auto BIGINT UNSIGNED, 
                id_posicion_calle BIGINT UNSIGNED, 
                latitud DOUBLE, 
                longitud DOUBLE, 
                velocidad SMALLINT UNSIGNED, 
                angulo SMALLINT UNSIGNED, 
                fecha DATETIME, 
                FOREIGN KEY(id_posicion_calle) REFERENCES posicion_calles(id));
           """]

for consulta in consultas_creacion:
    cursor.execute(consulta)
bd.close()

#Se consulta por todos los datos de la tabla original
bd = mysql.connect(host="localhost", 
                   user="root", 
                   password="", 
                   database="gps")
cursor   = bd.cursor()
cursor.execute("SELECT * FROM datos ORDER BY fecha ASC, hora ASC")

datos_obtenidos = cursor.fetchall()
bd.close()

contador = -1
for fila in datos_obtenidos:
    contador +=1
    print("\n****************************************************")
    print("FILA: ",contador)
    print("****************************************************")
    
    #Se consulta por la posicion exacta de dicho punto de latitud y longitud
    parametros = {
        "key" : "lo0ZaA7YgClUpyM8SUFuHN9sIYDk33O5",
        "location" : "%s, %s"%(fila[2],fila[3])
    }
    
    api        = requests.get("http://www.mapquestapi.com/geocoding/v1/reverse", params = parametros)
    resultado  = json.loads(api.text)["results"]
    
    #Datos obtenidos de la coordenada
    calle    = resultado[0]["locations"][0]["street"]
    ciudad   = resultado[0]["locations"][0]["adminArea5"]
    region   = resultado[0]["locations"][0]["adminArea3"]
    latitud_calle  = resultado[0]["locations"][0]["latLng"]["lat"]
    longitud_calle = resultado[0]["locations"][0]["latLng"]["lng"]
    
    
    #Se consulta a la nueva bd si la calle ya fué
    #insertada en la tabla "calles"
    bd = mysql.connect(host="localhost", 
                       user="root", 
                       password="", 
                       database="gps_datos")
    cursor   = bd.cursor()
    consulta = '''SELECT * FROM calles WHERE calle="%s" AND 
                  ciudad="%s" AND region="%s";'''
                  
    cursor.execute(consulta%(calle, ciudad, region))
    
    respuesta_calle = cursor.fetchall()
    insertada = len(respuesta_calle)
    bd.close()
    
    id_calle = 0
    if insertada == 0:
        #Se insertan los datos correspondientes en "calles"
        bd = mysql.connect(host="localhost", 
                           user="root", 
                           password="", 
                           database="gps_datos")
        cursor   = bd.cursor()
        consulta = """INSERT INTO calles(calle, ciudad, region) 
                      VALUES(%s, %s, %s)"""
        
        datos = (calle, ciudad, region)
        cursor.execute(consulta, datos)
        bd.commit()
        bd.close()
        
        print("CALLE INSERTADA")
        print("====================================================")
        print("CALLE: ", calle)
        print("CIUDAD: ", ciudad)
        print("REGIÓN: ", region)
        print("____________________________________________________\n")
        
        #Se consulta por el id de la calle
        bd = mysql.connect(host="localhost", 
                           user="root", 
                           password="", 
                           database="gps_datos")
        cursor   = bd.cursor()
        consulta = '''SELECT id FROM calles WHERE calle="%s" AND 
                      ciudad="%s" AND region="%s"'''
                      
        cursor.execute(consulta%(calle, ciudad, region))
        id_calle = cursor.fetchall()[0][0]
        bd.close()
    else:        
        #Se consulta por el id de la calle
        id_calle = respuesta_calle[0][0]
    
    #Se inserta la posicion de la calle y se consigue el id
    #De la posicion
    id_posicion_calle = insertar_posicion(id_calle, latitud_calle, longitud_calle)
    
    
    #Se consulta a la nueva bd si el auto ya fué
    #insertado en la tabla "autos"
    bd = mysql.connect(host="localhost", 
                       user="root", 
                       password="", 
                       database="gps_datos")
    cursor   = bd.cursor()
    consulta = '''SELECT * FROM autos WHERE id_auto=%s AND 
                  id_posicion_calle=%s AND latitud=%s AND
                  longitud=%s AND velocidad=%s AND 
                  angulo=%s AND fecha="%s";'''
    
    datos = (int(fila[1]), id_posicion_calle, fila[2], fila[3],
             fila[4], fila[5], "%s %s"%(fila[6], fila[7]))
    
    cursor.execute(consulta%datos)
    creada = len(cursor.fetchall())
    bd.close()
    
    if creada == 0:
        #Se insertan los datos correspondientes de los autos
        #en la tabla "autos"
        bd = mysql.connect(host="localhost", 
                           user="root", 
                           password="", 
                           database="gps_datos")
        cursor   = bd.cursor()
        consulta = """INSERT INTO autos(id_auto, id_posicion_calle, latitud,
                      longitud, velocidad, angulo, fecha) 
                      VALUES(%s, %s, %s, %s, %s, %s, %s)"""
    
        cursor.execute(consulta, datos)
        bd.commit()
        bd.close()
        
        print("AUTO INSERTADO")
        print("====================================================")
        print("ID AUTO: ", fila[1])
        print("POSICION CALLE: ", id_posicion_calle)
        print("LATITUD: ", fila[2])
        print("LONGITUD: ", fila[3])
        print("VELOCIDAD: ", fila[4])
        print("ANGULO: ", fila[5])
        print("FECHA: ", fila[6], " ", fila[7])
        print("____________________________________________________\n")
