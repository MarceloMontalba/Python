import os
import Tkinter
from PIL import Image,ImageTk
import sqlite3 as sq

def avanza(lista):
    global imagen,cont

    if(cont!=len(lista)-1): cont+=1
    else: cont=0

    canvas.delete("all")
    img=Image.open("./IMAGENES/"+lista[cont])
    t_canvas=(330,320)
    f_size=min(float(t_canvas[0])/float(img.size[0]),(float(t_canvas[1])/float(img.size[1])))
    t=(int(img.size[0]*f_size),int(img.size[1]*f_size))

    img=img.resize(t)
    img=ImageTk.PhotoImage(img)
    imagen=canvas.create_image(t_canvas[0]/2,t_canvas[1]/2,anchor=Tkinter.CENTER,image=img)
    ventana.mainloop()

def retrocede(lista):
    global imagen,cont

    if(cont!=0): cont-=1
    else: cont=len(lista)-1

    canvas.delete("all")
    img=Image.open("./IMAGENES/"+lista[cont])
    t_canvas=(330,320)
    f_size=min(float(t_canvas[0])/float(img.size[0]),(float(t_canvas[1])/float(img.size[1])))
    t=(int(img.size[0]*f_size),int(img.size[1]*f_size))

    img=img.resize(t)
    img=ImageTk.PhotoImage(img)
    imagen=canvas.create_image(t_canvas[0]/2,t_canvas[1]/2,anchor=Tkinter.CENTER,image=img)
    ventana.mainloop()

def db(lista):
    global cont
    img=Image.open("./IMAGENES/"+lista[cont])
    t=((img.size[0]*25)/100,(img.size[1]*25)/100)
    img=img.resize(t)
    img.save("./RESIZE/"+lista[cont])

    img=open("./RESIZE/"+lista[cont],"rb")
    img=img.read()
    
    insertar="INSERT INTO Fotos(imagen) VALUES(?)";
    cur.execute(insertar,[sq.Binary(img)])
    conecta.commit()
    
ventana=Tkinter.Tk()
fotos=os.listdir("./IMAGENES")

crear="CREATE TABLE Fotos(id INTEGER PRIMARY KEY AUTOINCREMENT,imagen blob)"
conecta=sq.connect("Imagenes.db")
conecta.execute(crear)

cur=conecta.cursor()

cont=0
#Muestra primera Imagen al cargar ventana
img=Image.open("./IMAGENES/"+fotos[cont])
t_canvas=(330,320)
f_size=min(float(t_canvas[0])/float(img.size[0]),(float(t_canvas[1])/float(img.size[1])))
t=(int(img.size[0]*f_size),int(img.size[1]*f_size))

img=img.resize(t)
img=ImageTk.PhotoImage(img)
canvas=Tkinter.Canvas(ventana,width=330,height=320,background="black")
imagen=canvas.create_image(t_canvas[0]/2,t_canvas[1]/2,anchor=Tkinter.CENTER,image=img)
canvas.pack()
#------------------------------------------

ventana.configure(background="GRAY")
ventana.geometry("600x310")
ventana.title("Visor de Imagenes")

retroceder=Tkinter.Button(ventana,text="Retroceder",command=lambda:retrocede(fotos),width=10,height=3)
avanzar=Tkinter.Button(ventana,text="Avanzar",command=lambda:avanza(fotos),width=10,height=3)
inserta=Tkinter.Button(ventana,text="Insertar",command=lambda:db(fotos),width=10,height=3)
cerrar=Tkinter.Button(ventana,text="Cerrar",command=ventana.destroy,width=10,height=3)

retroceder.place(x=10,y=90)
avanzar.place(x=500,y=90)
inserta.place(x=10,y=200)
cerrar.place(x=500,y=200)

ventana.resizable(False,False)
ventana.mainloop()
