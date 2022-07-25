from PIL import Image
import colorsys

def HSVColor(img):
    r,g,b = img.split()
    Hdat = []
    Sdat = []
    Vdat = [] 
    for rd,gn,bl in zip(r.getdata(),g.getdata(),b.getdata()) :
        h,s,v = colorsys.rgb_to_hsv(rd/255.,gn/255.,bl/255.)
        Hdat.append(int(h*255))
        Sdat.append(int(s*255))
        Vdat.append(int(v*255))
    r.putdata(Hdat)
    g.putdata(Sdat)
    b.putdata(Vdat)
    return Image.merge('RGB',(r,g,b))

def Separa(modo,cont,imagen,carga,ruta,titulo):
    v1=Image.new(modo,imagen.size,"white");
    v2=Image.new(modo,imagen.size,"white");
    v3=Image.new(modo,imagen.size,"white")

    v1.save(ruta+modo[0:1]+"_"+titulo);
    v2.save(ruta+modo[1:2]+"_"+titulo);
    v3.save(ruta+modo[2:3]+"_"+titulo)

    v1=Image.open(ruta+modo[0:1]+"_"+titulo);
    v2=Image.open(ruta+modo[1:2]+"_"+titulo);
    v3=Image.open(ruta+modo[2:3]+"_"+titulo)

    c_v1=v1.load(); c_v2=v2.load(); c_v3=v3.load();

    if (cont==4):
        v4=Image.new(modo,imagen.size,"white")
        v4.save(ruta+modo[3:4]+"_"+titulo)
        v4=Image.open(ruta+modo[3:4]+"_"+titulo)
        c_v4=v4.load()
        
    for x in range(imagen.size[0]):
        for y in range(imagen.size[1]):
            if(cont==3):
                c_v1[x,y]=(carga[x,y][0],0,0)
                c_v2[x,y]=(0,carga[x,y][1],0)
                c_v3[x,y]=(0,0,carga[x,y][2])
            else:
                c_v1[x,y]=(carga[x,y][0],0,0,190)
                c_v2[x,y]=(0,carga[x,y][1],0,190)
                c_v3[x,y]=(0,0,carga[x,y][2],190)
                c_v4[x,y]=(0,0,0,carga[x,y][3])
                
    v1.save(ruta+modo[0:1]+"_"+titulo)
    v2.save(ruta+modo[1:2]+"_"+titulo)
    v3.save(ruta+modo[2:3]+"_"+titulo)
    if cont==4: v4.save(ruta+modo[3:4]+"_"+titulo)

fotos=["F1.png","F2.png","F3.png","F4.png","F5.png","F6.png"]

#GREY
for i in range(len(fotos)):
    imagen= Image.open(fotos[i]).convert("L")
    imagen.save("img_ejer3/GREY_"+fotos[i])
#RGB
for i in range(len(fotos)):
    imagen=Image.open(fotos[i])
    carga=imagen.load()
    Separa("RGB",3,imagen,carga,"img_ejer3/RGB/",fotos[i])
    imagen.save("img_ejer3/RGB/RGB_"+fotos[i])
    
#RGBA
for i in range(len(fotos)):
    imagen=Image.open(fotos[i])
    carga=imagen.load()
    Separa("RGBA",4,imagen,carga,"img_ejer3/RGBA/",fotos[i])
    imagen.save("img_ejer3/RGBA/RGBA_"+fotos[i])

#CMYK    
for i in range(len(fotos)):
    imagen= Image.open(fotos[i]).convert("CMYK")
    carga=imagen.load()
    Separa("CMYK",4,imagen,carga,"img_ejer3/CMYK/",fotos[i][0:3]+"jpg")
    imagen.save("img_ejer3/CMYK/CMYK_"+fotos[i][0:3]+"jpg")
#HSV
for i in range(len(fotos)):
    imagen= Image.open(fotos[i]).convert("RGB")
    imagen=HSVColor(imagen)
    carga=imagen.load()
    Separa("RGB",3,imagen,carga,"img_ejer3/HSV/",fotos[i])
    imagen.save("img_ejer3/RGB/HSV_"+fotos[i])
