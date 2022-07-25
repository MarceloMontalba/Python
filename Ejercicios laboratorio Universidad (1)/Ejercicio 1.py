from PIL import Image
from numpy import array , dot, uint8

def PixToImage(pixel,mode='RGB'):
    if pixel.max()>255:
        pixel *= 255.0 / pixel.max()
    pixel = array(pixel, uint8)
    img=Image.fromarray(pixel,mode)
    return img

def ImageToPix(img):
    img2 = img.convert('RGB')
    h,w=img2.size
    data=img2.getdata()
    pixelist = array(data,uint8)
    pixelist=pixelist.reshape((w,h,3))
    return pixelist

def MaskImg(img,colores):
    aT = array(colores)
    img=dot(img,aT)
    return PixToImage(img)

#Parte 1
fotos=["F1.png","F2.png","F3.png","F4.png","F5.png","F6.png",]
for i in range (len(fotos)):
    imagen= Image.open(fotos[i])
    #Rojo
    c= ImageToPix(imagen)
    imagenFin=MaskImg(c,[
                [1.00,0.00,0.00],
                [0.00,0.00,0.00],
                [0.00,0.00,0.00]
                ])
    imagenFin.save('img_ejer1/Rojo_F'+str(i+1)+'.png')
    #Verde
    c= ImageToPix(imagen)
    imagenFin=MaskImg(c,[
                [0.00,0.00,0.00],
                [0.00,1.00,0.00],
                [0.00,0.00,0.00]
                ])
    imagenFin.save('img_ejer1/Verde_F'+str(i+1)+'.png')
    #Azul
    c= ImageToPix(imagen)
    imagenFin=MaskImg(c,[
                [0.00,0.00,0.00],
                [0.00,0.00,0.00],
                [0.00,0.00,1.00]
                ])
    imagenFin.save('img_ejer1/Azul_F'+str(i+1)+'.png')

#Parte 2
imagen=Image.open("F1.png")
c=ImageToPix(imagen)
imagenFin=MaskImg(c,[
                [0.00,0.00,0.00],
                [1.00,1.00,0.00],
                [0.00,0.00,0.00]
                ])
imagenFin.save("img_ejer1/1.2.png")

#Parte 3
imagen=Image.open("F3.png")
c=ImageToPix(imagen)
imagenFin=MaskImg(c,[
                [0.00,0.00,0.00],
                [1.00,0.50,0.00],
                [0.00,0.00,0.00]
                ])
imagenFin.save("img_ejer1/1.3.png")

#Parte 4
imagen=Image.open("F2.png")
c=ImageToPix(imagen)
imagenFin=MaskImg(c,[
                [0.00,0.00,1.00],
                [0.00,0.00,0.00],
                [0.00,0.00,0.00]
                ])
imagenFin.save("img_ejer1/1.4.png")

#Parte 5
imagen=Image.open("F4.png")
c=ImageToPix(imagen)
imagenFin=MaskImg(c,[
                [1.00,0.00,0.00],
                [1.00,0.00,0.00],
                [1.00,0.00,0.00]
                ])
imagenFin.save("img_ejer1/1.5.png")

#Parte 6
imagen=Image.open("F5.png")
carga=imagen.load()

nueva=Image.new("RGB",(imagen.size[0],imagen.size[1]),"white")
nueva.save("img_ejer1/1.6.png")
nueva=Image.open("img_ejer1/1.6.png")
c_nueva=nueva.load()

for x in range(imagen.size[0]):
    for y in range(imagen.size[1]):
        if (carga[x,y][0]>90 and carga[x,y][2]>90):
            c_nueva[x,y]=(carga[x,y][0],carga[x,y][1],carga[x,y][2])
        else:
            if(x>=132 and y>=78) and (x<=196 and y<=146):
                c_nueva[x,y]=(carga[x,y][0],carga[x,y][1],carga[x,y][2])
nueva.save("img_ejer1/1.6.png")
