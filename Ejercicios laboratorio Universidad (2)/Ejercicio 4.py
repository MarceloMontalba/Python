from PIL import Image, ImageTk
import Tkinter
import sys,os,smtplib,mimetypes
import tkFileDialog , tkMessageBox

from email.MIMEMultipart import MIMEMultipart
from email.MIMEImage import MIMEImage
from email.Encoders import encode_base64
from email.mime.text import MIMEText
from email.MIMEBase import MIMEBase 
from email import encoders

def EnviarMensaje(MiMensaje):
    MiEmail = miemail.get()
    MiPass  = mipass.get()
    EmailDest= emaildest.get()
    MiMsje=mimensaje.get()
    MiMensaje['From'] = MiEmail
    MiMensaje['To'] = EmailDest
    MiMensaje.attach(MIMEText(MiMsje,'plain'))
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login(MiEmail,MiPass)
    server.sendmail(MiEmail, EmailDest, MiMensaje.as_string())
    server.close()

def AdjuntarArchivo(Tk,mensaje):
    searchFile = tkFileDialog.askopenfilename(title="Adjuntar",initialdir="/",filetypes = (("jpeg files","*.jpg"),("jpeg files","*.jpeg*"),("ico files","*.ico"),("png files","*.png"),("all files","*.*")))
    DirFile = str(os.path.split(searchFile)[0]+'/'+str(os.path.split(searchFile)[1]))
    fileName= str(os.path.split(searchFile)[1])
    File = open(DirFile,'rb')
    encriptar= MIMEBase('multipart','encrypted')
    encriptar.set_payload(File.read())
    File.close()
    encoders.encode_base64(encriptar)
    encriptar.add_header('Content-Disposition', 'attachment', filename=fileName)
    mensaje.attach(encriptar)
    var = Tkinter.Label(Tk,font='Tahoma',bg='gray',text=fileName).place(x=480,y=70)


#***Creacion de ventana***#
Tk = Tkinter.Tk()
Tk.config(bg='gray')
Tk.title('Programa de correos')
Tk.geometry('600x230')
#***Contenido de Ventana***#
miemail=Tkinter.StringVar()
mipass=Tkinter.StringVar()
emaildest=Tkinter.StringVar()
mimensaje=Tkinter.StringVar()

mensajeCompleto=MIMEMultipart()

Mi_Email=Tkinter.Label(Tk,bg='gray',font='Tahoma',text='De: ').place(x=20,y=10)
Mi_Email_ranura=Tkinter.Entry(Tk,textvariable=miemail).place(width=330,height=21,x=105,y=13)
Mi_Pass=Tkinter.Label(Tk,bg='gray',font='Tahoma',text='Password: ').place(x=20,y=40)
Mi_Pass_ranura=Tkinter.Entry(Tk,textvariable=mipass,show='*').place(width=330,height=21,x=105,y=43)
Email_Dest=Tkinter.Label(Tk,bg='gray',font='Tahoma',text='Para: ').place(x=20,y=70)
Email_Dest_ranura=Tkinter.Entry(Tk,textvariable=emaildest).place(width=330,height=21,x=105,y=73)
Mi_Mensaje=Tkinter.Label(Tk,bg='gray',font='Tahoma',text='Mensaje: ').place(x=20,y=100)
Mi_Mensaje_ranura=Tkinter.Entry(Tk,textvariable=mimensaje).place(width=330,height=100,x=105,y=103)
btn1=Tkinter.Button(Tk,text='Adjuntar Archivo',command=lambda:AdjuntarArchivo(Tk,mensajeCompleto),width=14,height=1,anchor='center').place(x=480,y=130)
btn2=Tkinter.Button(Tk,text='Enviar',command=lambda:EnviarMensaje(mensajeCompleto),width=14,height=1,anchor='center').place(x=480,y=180)


#***Actualiza Ventana***#
Tk.mainloop()
