import os, shutil

directorio = os.path.dirname(os.path.abspath(__file__))
archivos   = os.listdir(directorio)

#Apartado encargado de sacar los archivos de video en sus respectivos
#directorios individuales y llevarlos al principal, para posteriormente eliminar
#el directorio individual en el que estaba.
for i in archivos:
    if len(i.split(".")) == 1:
        contenido = os.listdir("./%s"%i)

        for x in contenido:
            if len(x.split(".")) == 2:
                #Solo se moveran archivos de video al directorio principal y
                #posteriormente se elimina el directorio individual.
                if x.split(".")[1] in ["mp4","mkv"]:
                    #directorio= directorio_principa, i= directorio_individual, x = archivo
                    shutil.move("%s\%s\%s"%(directorio,i,x), "%s\%s"%(directorio,x))
                    shutil.rmtree("%s\%s"%(directorio,i))

#Directorio encargado de "limpiar" el titulo de cada video.
#Se resetea el directorio raiz para que se actualice con los nuevos archivos.
archivos   = os.listdir(directorio)
for i in archivos:
    #Solo archivos de video seran editados.
    if len(i.split(".")) == 2 and i.split(".")[1] in ["mkv", "mp4"]:
        nuevo_nombre = i.replace(" [720p][Cast+Eng+Jap+Subs]","") 
        os.rename(i, nuevo_nombre)
        
        print("NOMBRE ANTIGUO = %s"%i)
        print("NOMBRE NUEVO   = %s"%nuevo_nombre)
        print("======================================================")
