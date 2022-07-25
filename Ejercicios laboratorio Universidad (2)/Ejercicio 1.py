import win32api
import os,time,ctypes

ruta=win32api.GetFullPathName("IMAGENES")
d=os.listdir(ruta)

cont=0
while True:
    ctypes.windll.user32.SystemParametersInfoA(20,0,ruta+"\\"+d[cont],0)

    if(cont!=len(d)-1):
        cont+=1
    else:
        cont=0
    time.sleep(3)

