from PIL import Image
import matplotlib.pyplot as plt

def graficos(imagen,titulo):
    histograma=imagen.histogram()
    x=range(len(histograma))

    plt.figure("Histograma GREY")
    plt.subplot(2,1,1)
    plt.xticks([0, 50, 100, 150, 200, 255])
    plt.bar(x,histograma, align='center')
    plt.title("Histograma Normal/Acumulativo "+titulo)
    plt.xlabel('Valores de intensidad')
    plt.ylabel('Numero de pixeles')

    h_acumulativo=[]
    sumatoria=0
    for valor in histograma:
        sumatoria+=valor
        h_acumulativo.append(sumatoria)
    
    plt.subplot(2,1,2)
    plt.xticks([0, 50, 100, 150, 200, 255])
    plt.bar(x,h_acumulativo, align='center')
    plt.xlabel('Valores de intensidad')
    plt.ylabel('Numero de pixeles')
    plt.show()

def mostrar(imagenes):
    for i in range(0,len(imagenes)):
        imagen=Image.open(imagenes[i]).convert('L')
        graficos(imagen,imagenes[i])

imagenes=["F1.png","F2.png","F3.png","F4.png","F5.png","F6.png",]
mostrar(imagenes)
