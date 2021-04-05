from tkinter import *
from tkinter import filedialog
from tkinter import messagebox as MessageBox
import tkinter as tk
from tkinter import ttk
from xml.dom import minidom
import xml.etree.ElementTree as ET
import webbrowser
import os
from lista_circular import ListaCircular
from lista_orto import ListaOrtogonal
from datetime import datetime

###########INTERFAZ############
Ventana = Tk()
Ventana.title("Principal") #Titulo
Ventana.geometry("1000x500") #AnchoxAlto
Ventana.configure(background = "#212F3D") #Color
###########INTERFAZ############
Label(Ventana,text="Original").place(x=25, y=390)
Label(Ventana,text="Modificada").place(x=495, y=390)
image1 = tk.PhotoImage(file="inicio.png")
image2 = tk.PhotoImage(file="inicio.png")
label = tk.Label(Ventana, image = image1)
label2 = tk.Label(Ventana, image = image2)
label.place(x=20, y=20)
label2.place(x=490, y=20)

html = False
datosRepo = ""
nombres = ""
nombre = ""
ListaC = ListaCircular()
def cargarArchivo():
    global datosRepo, html, nombres
    ruta = filedialog.askopenfilename (title = "Abrir") 
    try:
        tree = ET.parse(ruta)
        root = tree.getroot()
        i = 0
        names = tree.findall("matriz")
        for elem in root:
            nueva = True
            if elem.tag == "matriz":
                #nombre
                nombre = names[i].find("nombre").text
                a = nombres.split(sep = ",")
                for nom in range(0,len(a)):
                    if a[nom] == nombre:
                        print("error, la matriz "+nombre+" ya existe")
                        nueva = False
                        i = i + 1
                if nueva == True:
                    #filas
                    n = names[i].find("fila").text
                    #columnas
                    m = names[i].find("columna").text
                    print(nombre+" "+n+" "+m)
                    #imagen
                    imagen = names[i].find("imagen").text
                    lineas = imagen.split(sep = None, maxsplit = -1)
                    j = 0
                    mas = False
                    if len(lineas) == int(n):
                        while j < int(n):
                            columnas = list(lineas[j])
                            if len(columnas) != int(m):
                                mas = True
                                break
                            j = j + 1
                        if mas:
                            print("error, la matriz "+nombre+" excede el numero de columnas indicado")
                        if mas == False:
                            nombres = nombres + nombre +","
                            caracter = ""
                            l = 0
                            vacio = 0
                            lleno = 0
                            for linea in lineas:
                                l = l + 1
                                columnas = list(linea)
                                c = 0
                                for col in columnas:
                                    c = c + 1
                                    if l == len(lineas) and c == len(columnas):
                                        if col == "-":
                                            caracter = caracter +" "
                                            vacio += 1
                                        elif col == "*":
                                            caracter = caracter +"*"
                                            lleno += 1
                                    else:
                                        if col == "-":
                                            caracter = caracter +" ,"
                                            vacio += 1
                                        elif col == "*":
                                            caracter = caracter +"*,"
                                            lleno += 1
                            Datos = caracter.split(",")
                            ListaO = ListaOrtogonal()
                            ListaO.CrearMatriz(int(n),int(m),Datos)
                            ListaC.Agregar(ListaO,nombre)
                            now = datetime.now()
                            datosRepo = datosRepo + str(now.day)+"/" + str(now.month)+"/" + str(now.year) +" - "+ str(now.time())  + " - "+ nombre +" - Espacios llenos: "+str(lleno)+" - Espacios vacíos: " +str(vacio) + ","
                    else:
                        print("error, la matriz "+nombre+" excede el numero de filas indicado")
                    i = i + 1
        MessageBox.showinfo("Cargar Archivo", "El archivo se cargo correctamente")
        html = True
    except:
        MessageBox.showerror("Error", "Carge el archivo de nuevo")
def elegir(lista,a):
    global datosRepo,nombre,image1,image2,label,label2
    nombre = lista.get()
    if a == 1:
        ListaC.buscarMat(nombre,a)
        image2 = tk.PhotoImage(file=nombre+"rotH.png")
        now = datetime.now()
        datosRepo = datosRepo + str(now.day)+"/" + str(now.month)+"/" + str(now.year) +" - "+ str(now.time())  + " - Rotacion horizontal de una imagen - Matriz (o matrices) usadas: " +nombre + ","
    elif a == 2:
        ListaC.buscarMat(nombre,a)
        image2 = tk.PhotoImage(file=nombre+"rotV.png")
        now = datetime.now()
        datosRepo = datosRepo + str(now.day)+"/" + str(now.month)+"/" + str(now.year) +" - "+ str(now.time())  + " - Rotacion vertical de una imagen - Matriz (o matrices) usadas: " +nombre + ","
    elif a == 3:
        ListaC.buscarMat(nombre,a)
        image2 = tk.PhotoImage(file=nombre+"tran.png")
        now = datetime.now()
        datosRepo = datosRepo + str(now.day)+"/" + str(now.month)+"/" + str(now.year) +" - "+ str(now.time())  + " - Transpuesta de una imagen - Matriz (o matrices) usadas: " +nombre + ","
    image1 = tk.PhotoImage(file=nombre+".png")
    image1 = image1.subsample(1,1)
    image2 = image2.subsample(1,1)
    label = tk.Label(Ventana, image = image1)
    label2 = tk.Label(Ventana, image = image2)
    label.place(x=20, y=20)
    label2.place(x=490, y=20)

def destruir(ventana):
    ventana.destroy()

def rotar(op):
    global datosRepo, html
    a = int(op)
    if html: 
        ventana = Toplevel()
        ventana.title("Operaciones") 
        ventana.geometry("300x90")
        op = Label(ventana,text="Seleccione una matriz para realizar la operación") 
        op.pack()
        lista = ttk.Combobox(ventana,width=17, state="readonly")
        nom = ListaC.Nombres().split(",")
        lista["values"] = nom
        lista.set(nom[0])
        lista.place(x=30, y=40)
        button = Button(ventana,text="Aceptar",bg="gold",command=lambda:[elegir(lista,a),destruir(ventana)])
        button.place(x=170,y=40)
        ventana.mainloop()
    else:
        MessageBox.showinfo("Operaciones", "Debe cargar un archivo de entrada")

def limpiar():    
    global datosRepo, html
    if html: 
        ventana = Toplevel()
        ventana.title("Operaciones") 
        ventana.geometry("300x300")
        Label(ventana,text="Seleccione una matriz para realizar la operación") .pack()
        lista = ttk.Combobox(ventana,width=17, state="readonly")
        nom = ListaC.Nombres().split(",")
        lista["values"] = nom
        lista.set(nom[0])
        lista.pack()
        Label(ventana,text="Coordenada inicial").pack()
        Label(ventana,text="Fila").place(x=20,y=60)
        f1 = tk.Entry(ventana,width=10,justify=tk.LEFT)
        f1.place(x=50,y=60)
        Label(ventana,text="Columna").place(x=150,y=60)
        c1 = tk.Entry(ventana,width=10,justify=tk.LEFT)
        c1.place(x=210,y=60)
        Label(ventana,text="Coordenada final").place(x=103,y=80)
        Label(ventana,text="Fila").place(x=20,y=100)
        f2 = tk.Entry(ventana,width=10,justify=tk.LEFT)
        f2.place(x=50,y=100)
        Label(ventana,text="Columna").place(x=150,y=100)
        c2 = tk.Entry(ventana,width=10,justify=tk.LEFT)
        c2.place(x=210,y=100)
        button = Button(ventana,text="Aceptar",bg="gold",command=lambda:[destruir(ventana)])
        button.place(x=120,y=130)
        ventana.mainloop()
    else:
        MessageBox.showinfo("Operaciones", "Debe cargar un archivo de entrada")


def agregarH():
    global datosRepo, html
    if html:
        nombre = "mat"
        now = datetime.now()
        datosRepo = datosRepo + str(now.day)+"/" + str(now.month)+"/" + str(now.year) +" - "+ str(now.time())  + " - Agregar línea horizontal a una imagen - Matriz (o matrices) usadas: " +nombre + ","
    else:
        MessageBox.showinfo("Operaciones", "Debe cargar un archivo de entrada")

def agregarV():
    global datosRepo, html
    if html: 
        nombre = "mat"
        now = datetime.now()
        datosRepo = datosRepo + str(now.day)+"/" + str(now.month)+"/" + str(now.year) +" - "+ str(now.time())  + " - Agregar línea vertical a una imagen - Matriz (o matrices) usadas: " +nombre + ","
    else:
        MessageBox.showinfo("Operaciones", "Debe cargar un archivo de entrada")

def agregarR():    
    pass  

def agregarT():    
    pass 

def reporte():
    global datosRepo, html
    if html:
        datos = datosRepo.split(",")
        fichero = open("Reporte.html","w")
        fichero.write("""<!doctype html>
                    <html lang="en">
                    <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1">
                    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-eOJMYsd53ii+scO/bJGFsiCZc+5NDVN2yr8+0RDqr0Ql0h+rP48ckxlpbzKgwra6" crossorigin="anonymous">
                    <title>Reporte</title>
                    </head>
                    <body>
                     <h1>Reporte</h1>
                    <table class="table">
                    <tbody>""")
        for s in datos:
            fichero.write("<tr><td>"+s+"</td></tr>\n")
        fichero.write("""</tbody>
                    </table>
                    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/js/bootstrap.bundle.min.js" integrity="sha384-JEW9xMcG8R+pH31jmWH6WWP0WintQrMb4s7ZOdauHnUtxwoG2vI5DkLtS3qm9Ekf" crossorigin="anonymous"></script>
                    </body>
                    </html>""")
        fichero.close()
        webbrowser.open_new_tab("Reporte.html")
    else:
        MessageBox.showinfo("Reporte HTML", "Debe cargar un archivo de entrada")

def datosEstudiante():
    Ventana = Tk()
    Ventana.title("Información del estudiante") #Titulo
    Ventana.geometry("200x110") #AnchoxAlto
    nombre = Label(Ventana,text="Katheryn Darleny Yuman Oscal") 
    nombre.pack()
    carnet = Label(Ventana,text="201902209") 
    carnet.pack()
    carrera = Label(Ventana,text="Ingenieria en ciencias y sistemas") 
    carrera.pack()
    semestre = Label(Ventana,text="5to. semestre") 
    semestre.pack()
    curso = Label(Ventana,text="IPC - 2, \"B\"") 
    curso.pack()
    Ventana.mainloop()

def Docu():
    webbrowser.open_new_tab("Documentación\Ensayo.pdf")

###########INTERFAZ############
Barra = Menu(Ventana)
#Cargar Archivo
CargarArchivo = Menu(Barra)
CargarArchivo.add_command(label = "Cargar archivo de entrada",command=cargarArchivo)

#Operaciones
Operaciones = Menu(Barra)
Operaciones.add_command(label = "Rotacion horizontal de una imagen",command=lambda:[rotar(1)])
Operaciones.add_command(label = "Rotacion vertical de una imagen",command=lambda:[rotar(2)])
Operaciones.add_command(label = "Transpuesta de una imagen",command =lambda:[rotar(3)])
Operaciones.add_command(label = "Limpiar zona de una imagen",command=limpiar)
Operaciones.add_command(label = "Agregar línea horizontal a una imagen",command=agregarH)
Operaciones.add_command(label = "Agregar línea vertical a una imagen",command=agregarV)
Operaciones.add_command(label = "Agregar rectángulo",command=agregarR)
Operaciones.add_command(label = "Agregar triángulo rectángulo",command=agregarT)
Operaciones.add_command(label = "Unión A, B")
Operaciones.add_command(label = "Intersección A, B")
Operaciones.add_command(label = "Diferencia A, B")
Operaciones.add_command(label = "Diferencia simétrica A, B")

#Reportes
Reportes = Menu(Barra)
Reportes.add_command(label = "Reporte HTML",command=reporte)

#Ayuda
Ayuda = Menu(Barra)
Ayuda.add_command(label = "Información del estudiante",command=datosEstudiante)
Ayuda.add_command(label = "Documentación del programa",command=Docu)

Barra.add_cascade(label = "Cargar archivo", menu = CargarArchivo)
Barra.add_cascade(label = "Operaciones", menu = Operaciones)
Barra.add_cascade(label = "Reportes", menu = Reportes)
Barra.add_cascade(label = "Ayuda", menu = Ayuda)

Ventana.config(menu = Barra)
Ventana.mainloop()