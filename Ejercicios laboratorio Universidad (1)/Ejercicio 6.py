from PIL import Image
import matplotlib.pyplot as plt

def graficos(imagen,titulo):
    histograma=imagen.histogram()

    h_acumulativo=[]
    sumatoria=0
    for valor in histograma:
        sumatoria+=valor
        h_acumulativo.append(sumatoria)

    aux=255.0/float(imagen.size[0]*imagen.size[1])
    e_histograma=[]
    foto=imagen.getdata()
    e_histograma=[]
    for i in foto:
        e_histograma.append(round(h_acumulativo[i]*aux))

    foto_ecualizada=Image.new("L",imagen.size)
    foto_ecualizada.putdata(e_histograma)
    foto_ecualizada.save("EC_"+titulo)

    n_histograma=foto_ecualizada.histogram()
    x=range(len(n_histograma))

    e_histograma=[]
    sumatoria=0
    for valor in n_histograma:
        sumatoria+=valor
        e_histograma.append(sumatoria)
    
    plt.plot()
    plt.title("Ecualizacion Histograma Lineal "+titulo)
    plt.xticks([63,127,191,255])
    plt.bar(x,e_histograma, align='center')
    plt.xlabel('Valores de intensidad')
    plt.ylabel('Numero de pixeles')
    plt.show()


imagenes=["F1.png","F2.png","F3.png","F4.png","F5.png","F6.png",]
for i in range(0,len(imagenes)):
    imagen=Image.open(imagenes[i]).convert('L')
    graficos(imagen,imagenes[i])

