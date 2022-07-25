from Tkinter import *
from PIL import Image,ImageOps
from PIL import ImageTk
import sqlite3 as sq,StringIO

def aumenta():
    global cantidad
    global size
    global cont
    cont+=1

    if cont >cantidad:
        cont=cantidad

    con=sq.connect("./../Ejercicio 1/Imagenes.db")
    cur=con.cursor()

    consulta="SELECT img,r,g,b,gris FROM Fotos WHERE id="+str(cont)
    e=cur.execute(consulta)
    e=e.fetchone()
        
    img =e[0]
    r=e[1]
    g=e[2]
    b=e[3]
    gris=e[4]

    img=StringIO.StringIO(img)
    r=StringIO.StringIO(r)
    g=StringIO.StringIO(g)
    b=StringIO.StringIO(b)
    gris=StringIO.StringIO(gris)

    img = Image.open(img)
    r= Image.open(r)
    g= Image.open(g)
    b= Image.open(b)
    gris= Image.open(gris)
    negada=ImageOps.invert(img)
    
    Imagen=[]
    for i in range(6):
        Imagen.append(img)
        Imagen.append(r)
        Imagen.append(g)
        Imagen.append(b)
        Imagen.append(gris)
        Imagen.append(negada)
    for i in range(6):
        Imagen[i]=Imagen[i].resize(size)
        Imagen[i]=ImageTk.PhotoImage(Imagen[i])
            
    muestra.create_image (size[0]/2,size[1]/2,image=Imagen[0])
    muestra2.create_image(size[0]/2,size[1]/2,image=Imagen[4])
    muestra3.create_image(size[0]/2,size[1]/2,image=Imagen[5])
    muestra4.create_image(size[0]/2,size[1]/2,image=Imagen[1])
    muestra5.create_image(size[0]/2,size[1]/2,image=Imagen[2])
    muestra6.create_image(size[0]/2,size[1]/2,image=Imagen[3])
    ventana.mainloop()
        
def disminuye():
    global size
    global cont
    cont-=1

    if cont <1:
        cont=1
    con=sq.connect("./../Ejercicio 1/Imagenes.db")
    cur=con.cursor()

    consulta="SELECT img,r,g,b,gris FROM Fotos WHERE id="+str(cont)
    e=cur.execute(consulta)
    e=e.fetchone()
        
    img =e[0]
    r=e[1]
    g=e[2]
    b=e[3]
    gris=e[4]

    img=StringIO.StringIO(img)
    r=StringIO.StringIO(r)
    g=StringIO.StringIO(g)
    b=StringIO.StringIO(b)
    gris=StringIO.StringIO(gris)

    img = Image.open(img)
    r= Image.open(r)
    g= Image.open(g)
    b= Image.open(b)
    gris= Image.open(gris)
    negada=ImageOps.invert(img)
    
    Imagen=[]
    for i in range(6):
        Imagen.append(img)
        Imagen.append(r)
        Imagen.append(g)
        Imagen.append(b)
        Imagen.append(gris)
        Imagen.append(negada)
    for i in range(6):
        Imagen[i]=Imagen[i].resize(size)
        Imagen[i]=ImageTk.PhotoImage(Imagen[i])
            
    muestra.create_image (size[0]/2,size[1]/2,image=Imagen[0])
    muestra2.create_image(size[0]/2,size[1]/2,image=Imagen[4])
    muestra3.create_image(size[0]/2,size[1]/2,image=Imagen[5])
    muestra4.create_image(size[0]/2,size[1]/2,image=Imagen[1])
    muestra5.create_image(size[0]/2,size[1]/2,image=Imagen[2])
    muestra6.create_image(size[0]/2,size[1]/2,image=Imagen[3])
    ventana.mainloop()

cont=1
   
ventana=Tk()
ventana.title("Visor")
ventana.config(bg="orange")
ventana.geometry("580x500")

size=(150,190)

con=sq.connect("./../Ejercicio 1/Imagenes.db")
cur=con.cursor()

c="Select count(*) From Fotos"
cantidad=cur.execute(c)
cantidad=int(cantidad.fetchone()[0])

consulta="SELECT img,r,g,b,gris FROM Fotos WHERE id="+str(cont)
e=cur.execute(consulta)
e=e.fetchone()

img =e[0]
r=e[1]
g=e[2]
b=e[3]
gris=e[4]

img=StringIO.StringIO(img)
r=StringIO.StringIO(r)
g=StringIO.StringIO(g)
b=StringIO.StringIO(b)
gris=StringIO.StringIO(gris)

img = Image.open(img)
r= Image.open(r)
g= Image.open(g)
b= Image.open(b)
gris= Image.open(gris)

abrir=img.resize(size)
imagen=ImageTk.PhotoImage(abrir)
muestra=Canvas(ventana,width=size[0],height=size[1])
muestra.create_image(size[0]/2,size[1]/2,image=imagen)
muestra.place(x=10,y=10)
    
abrir2=gris.resize(size)
imagen2=ImageTk.PhotoImage(abrir2)
muestra2=Canvas(ventana,width=size[0],height=size[1])
muestra2.create_image(size[0]/2,size[1]/2,image=imagen2)
muestra2.place(x=200,y=10)

abrir3=ImageOps.invert(img)
abrir3=abrir3.resize(size)
imagen3=ImageTk.PhotoImage(abrir3)
muestra3=Canvas(ventana,width=size[0],height=size[1])
muestra3.create_image(size[0]/2,size[1]/2,image=imagen3)
muestra3.place(x=390,y=10)

abrir4=r.resize(size)
imagen4=ImageTk.PhotoImage(abrir4)
muestra4=Canvas(ventana,width=size[0],height=size[1])
muestra4.create_image(size[0]/2,size[1]/2,image=imagen4)
muestra4.place(x=10,y=220)

abrir5=g.resize(size)
imagen5=ImageTk.PhotoImage(abrir5)
muestra5=Canvas(ventana,width=size[0],height=size[1])
muestra5.create_image(size[0]/2,size[1]/2,image=imagen5)
muestra5.place(x=200,y=220)

abrir6=b
abrir6=abrir6.resize(size)
imagen6=ImageTk.PhotoImage(abrir6)
muestra6=Canvas(ventana,width=size[0],height=size[1])
muestra6.create_image(size[0]/2,size[1]/2,image=imagen6)
muestra6.place(x=390,y=220)
#--------------------------------------------------------------------------------

p=Button(ventana,text="Anterior",height = 2, width = 12,command=disminuye)
p.place(x=260,y=450)

n=Button(ventana,text="Siguiente",height = 2, width = 12,command=aumenta)
n.place(x=360,y=450)

c=Button(ventana,text="Cerrar",height = 2, width = 12, command=ventana.destroy)
c.place(x=460,y=450)

ventana.mainloop()
    
