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
Ventana.configure(background = "#17202A") #Color
ori = Label(Ventana,text="Original", fg = "#E74C3C")
ori.place(x=25, y=390)
mod = Label(Ventana,text="Modificada", fg = "#E74C3C")
mod.place(x=495, y=390)
image1 = tk.PhotoImage(file="inicio.png")
image2 = tk.PhotoImage(file="inicio.png")
label = tk.Label(Ventana, image = image1)
label2 = tk.Label(Ventana, image = image2)
label.place(x=20, y=20)
label2.place(x=490, y=20)
ori.config(bg = "#17202A")
mod.config(bg = "#17202A")
###########INTERFAZ############

html = False
datosRepo = ""
nombres = ""
nombre = ""
ListaC = ListaCircular()
def cargarArchivo():
    global datosRepo, html, nombres, ListaC
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
                        now = datetime.now()
                        datosRepo = datosRepo + str(now.day)+"/" + str(now.month)+"/" + str(now.year) +" - "+ str(now.time())  + " - Cargar Archivo - Error la matriz "+ nombre +" ya existe,"   
                        nueva = False
                        i = i + 1
                if nueva == True:
                    #filas
                    n = names[i].find("fila").text
                    #columnas
                    m = names[i].find("columna").text
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
                                now = datetime.now()
                                datosRepo = datosRepo + str(now.day)+"/" + str(now.month)+"/" + str(now.year) +" - "+ str(now.time())  + " - Cargar Archivo - Error la matriz "+ nombre +" exede el numeo de columnas indicado,"
                                break
                            j = j + 1
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
                        now = datetime.now()
                        datosRepo = datosRepo + str(now.day)+"/" + str(now.month)+"/" + str(now.year) +" - "+ str(now.time())  + " - Cargar Archivo - Error la matriz "+ nombre +" exede el numeo de filas indicado,"
                    i = i + 1
        MessageBox.showinfo("Cargar Archivo", "El archivo se termino de cargar")
        html = True
    except:
        MessageBox.showerror("Error", "Carge el archivo de nuevo")
def dos(lista,lista2):
    global datosRepo, nombre, image1, image2, label, label2, ListaC
    nombre = lista.get()
    nombre2 = lista2.get()
    ListaC.buscarMat4(nombre)
    ListaC.buscarMat4(nombre2)
    image2 = tk.PhotoImage(file=nombre)
    image1 = tk.PhotoImage(file=nombre2)
    image1 = image1.subsample(2,2)
    image2 = image2.subsample(2,2)
    label = tk.Label(Ventana, image = image1)
    label2 = tk.Label(Ventana, image = image2)
    label.place(x=20, y=20)
    label2.place(x=20, y=300)
def elegir(lista,a):
    global datosRepo, nombre, image1, image2, label, label2, ListaC
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

def linea(lista,f1,c1,ca,accion):
    global datosRepo, nombre, image1, image2, label, label2, ListaC
    nombre = lista.get()
    f = f1.get()
    c = c1.get()
    cant = ca.get()
    if str(f) != "" and str(c) != "" and str(cant) != "":
        
        if accion == 5:
            ListaC.buscarMat2(nombre, int(f), int(c), int(cant), accion)
            image2 = tk.PhotoImage(file=nombre+"agreH.png")
            now = datetime.now()
            datosRepo = datosRepo + str(now.day)+"/" + str(now.month)+"/" + str(now.year) +" - "+ str(now.time())  + " - Agregar línea horizontal a una imagen - Matriz (o matrices) usadas: " +nombre + ","
        elif accion == 6:
            ListaC.buscarMat2(nombre, int(f), int(c), int(cant), accion)
            image2 = tk.PhotoImage(file=nombre+"agreV.png")
            now = datetime.now()
            datosRepo = datosRepo + str(now.day)+"/" + str(now.month)+"/" + str(now.year) +" - "+ str(now.time())  + " - Agregar línea vertical a una imagen - Matriz (o matrices) usadas: " +nombre + ","
        elif accion == 8:
            ListaC.buscarMat2(nombre, int(f), int(c), int(cant), accion)
            image2 = tk.PhotoImage(file=nombre+"agreT.png")
            now = datetime.now()
            datosRepo = datosRepo + str(now.day)+"/" + str(now.month)+"/" + str(now.year) +" - "+ str(now.time())  + " - Agregar triangulo a una imagen - Matriz (o matrices) usadas: " +nombre + ","
        image1 = tk.PhotoImage(file=nombre+".png")
        image1 = image1.subsample(1,1)
        image2 = image2.subsample(1,1)
        label = tk.Label(Ventana, image = image1)
        label2 = tk.Label(Ventana, image = image2)
        label.place(x=20, y=20)
        label2.place(x=490, y=20)
    else:
        MessageBox.showerror("Error", "Debe llenarse todos los campos")

def limYr(lista,f1,c1,f2,c2,accion):
    global datosRepo, nombre, image1, image2, label, label2, ListaC
    nombre = lista.get()
    f = f1.get()
    c = c1.get()
    ff = f2.get()
    cc = c2.get()
    if str(f) != "" and str(c) != "" and str(ff) != "" and str(cc) != "":
        if accion == 4:
            ListaC.buscarMat3(nombre, int(f),int(c) ,int(ff),int(cc), accion)
            image2 = tk.PhotoImage(file=nombre+"limp.png")
            now = datetime.now()
            datosRepo = datosRepo + str(now.day)+"/" + str(now.month)+"/" + str(now.year) +" - "+ str(now.time())  + " - Limpiar zona de una imagen - Matriz (o matrices) usadas: " +nombre + ","
        elif accion == 7:
            ListaC.buscarMat3(nombre, int(f),int(c) ,int(ff),int(cc), accion)
            image2 = tk.PhotoImage(file=nombre+"agreR.png")
            now = datetime.now()
            datosRepo = datosRepo + str(now.day)+"/" + str(now.month)+"/" + str(now.year) +" - "+ str(now.time())  + " - Agregar rectángulo - Matriz (o matrices) usadas: " +nombre + ","
        image1 = tk.PhotoImage(file=nombre+".png")
        image1 = image1.subsample(1,1)
        image2 = image2.subsample(1,1)
        label = tk.Label(Ventana, image = image1)
        label2 = tk.Label(Ventana, image = image2)
        label.place(x=20, y=20)
        label2.place(x=490, y=20)
    else:
        MessageBox.showerror("Error", "Debe llenarse todos los campos")

def destruir(ventana):
    ventana.destroy()

def rotar(op):
    global datosRepo, html
    a = int(op)
    if html: 
        ventana = Toplevel()
        ventana.title("Operaciones") 
        ventana.geometry("300x90")
        ventana.configure(background = "#17202A")
        op = Label(ventana,text="Seleccione una matriz para realizar la operación", fg = "white") 
        op.pack()
        op.configure(background = "#17202A")
        lista = ttk.Combobox(ventana,width=17, state="readonly")
        nom = ListaC.Nombres().split(",")
        lista["values"] = nom
        lista.set(nom[0])
        lista.place(x=30, y=40)
        button = Button(ventana,text="Aceptar", fg = "white",bg="#E74C3C",command=lambda:[elegir(lista,a),destruir(ventana)])
        button.place(x=170,y=40)
        ventana.mainloop()
    else:
        MessageBox.showinfo("Operaciones", "Debe cargar un archivo de entrada")
def validate_entry(text):
    return text.isdecimal()
def limpiar():    
    global datosRepo, html
    if html: 
        ventana = Toplevel()
        ventana.title("Operaciones") 
        ventana.geometry("300x170")
        ventana.configure(background = "#17202A")
        a = Label(ventana,text="Seleccione una matriz para realizar la operación", fg = "white")
        a.pack()
        a.config(bg = "#17202A")
        lista = ttk.Combobox(ventana,width=17, state="readonly")
        nom = ListaC.Nombres().split(",")
        lista["values"] = nom
        lista.set(nom[0])
        lista.pack()
        b = Label(ventana,text="Coordenada inicial", fg = "white")
        b.pack()
        b.config(bg = "#17202A")
        c = Label(ventana,text="Fila", fg = "#E74C3C")
        c.place(x=60,y=60)
        c.config(bg = "#17202A")
        f1 = tk.Entry(ventana,validate = "key", validatecommand=(ventana.register(validate_entry),"%S"),width=5,justify=tk.LEFT)
        f1.place(x=90,y=60)
        d = Label(ventana,text="Columna", fg = "#E74C3C")
        d.place(x=145,y=60)
        d.config(bg = "#17202A")
        c1 = tk.Entry(ventana,validate = "key", validatecommand=(ventana.register(validate_entry),"%S"),width=5,justify=tk.LEFT)
        c1.place(x=205,y=60)
        e = Label(ventana,text="Coordenada final", fg = "white")
        e.place(x=103,y=80)
        e.config(bg = "#17202A")
        f = Label(ventana,text="Fila", fg = "#E74C3C")
        f.place(x=60,y=100)
        f.config(bg = "#17202A")
        f2 = tk.Entry(ventana, validate = "key", validatecommand=(ventana.register(validate_entry),"%S"),width=5,justify=tk.LEFT)
        f2.place(x=90,y=100)
        g = Label(ventana,text="Columna", fg = "#E74C3C")
        g.place(x=145,y=100)
        g.config(bg = "#17202A")
        c2 = tk.Entry(ventana,validate = "key", validatecommand=(ventana.register(validate_entry),"%S"),width=5,justify=tk.LEFT)
        c2.place(x=205,y=100)
        button = Button(ventana,text="Aceptar",fg = "white",bg="#E74C3C",command=lambda:[limYr(lista,f1,c1,f2,c2,4),destruir(ventana)])
        button.place(x=125,y=130)
        ventana.mainloop()
    else:
        MessageBox.showinfo("Operaciones", "Debe cargar un archivo de entrada")


def agregarF(accion):
    global datosRepo, html
    if html:
        ventana = Toplevel()
        ventana.title("Operaciones") 
        ventana.geometry("300x170")
        ventana.configure(background = "#17202A")
        a = Label(ventana,text="Seleccione una matriz para realizar la operación", fg = "white")
        a.pack()
        a.config(bg = "#17202A")
        lista = ttk.Combobox(ventana,width=17, state="readonly")
        nom = ListaC.Nombres().split(",")
        lista["values"] = nom
        lista.set(nom[0])
        lista.pack()
        b = Label(ventana,text="Coordenada inicial", fg = "white")
        b.pack()
        b.config(bg = "#17202A")
        c = Label(ventana,text="Fila", fg = "#E74C3C")
        c.place(x=60,y=60)
        c.config(bg = "#17202A")
        f1 = tk.Entry(ventana,validate = "key", validatecommand=(ventana.register(validate_entry),"%S"),width=5,justify=tk.LEFT)
        f1.place(x=90,y=60)
        d = Label(ventana,text="Columna", fg = "#E74C3C")
        d.place(x=145,y=60)
        d.config(bg = "#17202A")
        c1 = tk.Entry(ventana,validate = "key", validatecommand=(ventana.register(validate_entry),"%S"),width=5,justify=tk.LEFT)
        c1.place(x=205,y=60)
        e = Label(ventana,text="Cantidad de Elementos", fg = "white")
        e.place(x=85,y=80)
        e.config(bg = "#17202A")
        cant= tk.Entry(ventana,validate = "key", validatecommand=(ventana.register(validate_entry),"%S"),width=10,justify=tk.LEFT)
        cant.place(x=117,y=100)
        button = Button(ventana,text="Aceptar",fg = "white",bg="#E74C3C",command=lambda:[linea(lista,f1,c1,cant,accion),destruir(ventana)])
        button.place(x=125,y=130)
        ventana.mainloop()
    else:
        MessageBox.showinfo("Operaciones", "Debe cargar un archivo de entrada")


def agregarR():    
    global datosRepo, html
    if html: 
        ventana = Toplevel()
        ventana.title("Operaciones") 
        ventana.geometry("300x170")
        ventana.configure(background = "#17202A")
        a = Label(ventana,text="Seleccione una matriz para realizar la operación", fg = "white")
        a.pack()
        a.config(bg = "#17202A")
        lista = ttk.Combobox(ventana,width=17, state="readonly")
        nom = ListaC.Nombres().split(",")
        lista["values"] = nom
        lista.set(nom[0])
        lista.pack()
        b = Label(ventana,text="Coordenada inicial", fg = "white")
        b.pack()
        b.config(bg = "#17202A")
        c = Label(ventana,text="Fila", fg = "#E74C3C")
        c.place(x=60,y=60)
        c.config(bg = "#17202A")
        f1 = tk.Entry(ventana,validate = "key", validatecommand=(ventana.register(validate_entry),"%S"),width=5,justify=tk.LEFT)
        f1.place(x=90,y=60)
        d = Label(ventana,text="Columna", fg = "#E74C3C")
        d.place(x=145,y=60)
        d.config(bg = "#17202A")
        c1 = tk.Entry(ventana,validate = "key", validatecommand=(ventana.register(validate_entry),"%S"),width=5,justify=tk.LEFT)
        c1.place(x=205,y=60)
        e = Label(ventana,text="Cantidad", fg = "white")
        e.place(x=120,y=80)
        e.config(bg = "#17202A")
        f = Label(ventana,text="Filas", fg = "#E74C3C")
        f.place(x=60,y=100)
        f.config(bg = "#17202A")
        f2 = tk.Entry(ventana,validate = "key", validatecommand=(ventana.register(validate_entry),"%S"),width=5,justify=tk.LEFT)
        f2.place(x=95,y=100)
        g = Label(ventana,text="Columnas", fg = "#E74C3C")
        g.place(x=140,y=100)
        g.config(bg = "#17202A")
        c2 = tk.Entry(ventana,validate = "key", validatecommand=(ventana.register(validate_entry),"%S"),width=5,justify=tk.LEFT)
        c2.place(x=205,y=100)
        button = Button(ventana,text="Aceptar",fg = "white",bg="#E74C3C",command=lambda:[limYr(lista,f1,c1,f2,c2,7),destruir(ventana)])
        button.place(x=125,y=130)
        ventana.mainloop()
    else:
        MessageBox.showinfo("Operaciones", "Debe cargar un archivo de entrada")
 

def agregarT():    
    global datosRepo, html
    if html:
        ventana = Toplevel()
        ventana.title("Operaciones") 
        ventana.geometry("300x170")
        ventana.configure(background = "#17202A")
        a = Label(ventana,text="Seleccione una matriz para realizar la operación", fg = "white")
        a.pack()
        a.config(bg = "#17202A")
        lista = ttk.Combobox(ventana,width=17, state="readonly")
        nom = ListaC.Nombres().split(",")
        lista["values"] = nom
        lista.set(nom[0])
        lista.pack()
        b = Label(ventana,text="Coordenada inicial", fg = "white")
        b.pack()
        b.config(bg = "#17202A")
        c = Label(ventana,text="Fila", fg = "#E74C3C")
        c.place(x=60,y=60)
        c.config(bg = "#17202A")
        f1 = tk.Entry(ventana,width=5,justify=tk.LEFT)
        f1.place(x=90,y=60)
        d = Label(ventana,text="Columna", fg = "#E74C3C")
        d.place(x=145,y=60)
        d.config(bg = "#17202A")
        c1 = tk.Entry(ventana,width=5,justify=tk.LEFT)
        c1.place(x=205,y=60)
        e = Label(ventana,text="Numero de filas y columnas", fg = "white")
        e.place(x=75,y=80)
        e.config(bg = "#17202A")
        cant= tk.Entry(ventana,width=10,justify=tk.LEFT)
        cant.place(x=117,y=100)
        button = Button(ventana,text="Aceptar",fg = "white",bg="#E74C3C",command=lambda:[linea(lista,f1,c1,cant,8),destruir(ventana)])
        button.place(x=125,y=130)
        ventana.mainloop()
    else:
        MessageBox.showinfo("Operaciones", "Debe cargar un archivo de entrada")

def dosMat(accion):
    global datosRepo, html
    if html:
        ventana = Toplevel()
        ventana.title("Operaciones") 
        ventana.geometry("300x150")
        ventana.configure(background = "#17202A")
        a = Label(ventana,text="Matriz A", fg = "white")
        a.pack()
        a.config(bg = "#17202A")
        lista = ttk.Combobox(ventana,width=17, state="readonly")
        nom = ListaC.Nombres().split(",")
        lista["values"] = nom
        lista.set(nom[0])
        lista.pack()
        b = Label(ventana,text="Matriz B", fg = "white")
        b.pack()
        b.config(bg = "#17202A")
        lista2 = ttk.Combobox(ventana,width=17, state="readonly")
        lista2["values"] = nom
        lista2.set(nom[0])
        lista2.pack()
        button = Button(ventana,text="Aceptar",fg = "white",bg="#E74C3C",command=lambda:[dos(lista,lista2),destruir(ventana)])
        button.pack()
        ventana.mainloop()
    else:
        MessageBox.showinfo("Operaciones", "Debe cargar un archivo de entrada")

def reporte():
    global datosRepo, html
    if html:
        datos = datosRepo.split(",")
        fichero = open("Reporte.html","w")
        fichero.write("""<!doctype html>
                    <html lang="en">
                    <head>
                    <meta charset="utf-8">
                    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
                    <meta charset="UTF-8"/>
                    <meta name="viewport" content="width=device-width, initial-scale=1">
                    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-eOJMYsd53ii+scO/bJGFsiCZc+5NDVN2yr8+0RDqr0Ql0h+rP48ckxlpbzKgwra6" crossorigin="anonymous">
                    <title>Reporte</title>
                    </head>
                    <body  style="background-color:#17202A;">
                    
                     <h1 style="color:white">Reporte</h1>
                    <table class="table">
                    <tbody>""")
        for s in datos:
            fichero.write("<tr><td> <font color=\"#E74C3C\">"+s+"</font></td></tr>\n")
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
Barra = Menu(Ventana, bg = "#E74C3C",fg = "white")
Barra.config(bg = "#E74C3C",fg = "white")
#Cargar Archivo
CargarArchivo = Menu(Barra)
CargarArchivo.config(bg = "#E74C3C",fg = "white")
CargarArchivo.add_command(label = "Cargar archivo de entrada",command=cargarArchivo)

#Operaciones
Operaciones = Menu(Barra)
Operaciones.config(bg = "#E74C3C",fg = "white")
Operaciones.add_command(label = "Rotacion horizontal de una imagen",command=lambda:[rotar(1)])
Operaciones.add_command(label = "Rotacion vertical de una imagen",command=lambda:[rotar(2)])
Operaciones.add_command(label = "Transpuesta de una imagen",command =lambda:[rotar(3)])
Operaciones.add_command(label = "Limpiar zona de una imagen",command=limpiar)
Operaciones.add_command(label = "Agregar línea horizontal a una imagen",command=lambda:[agregarF(5)])
Operaciones.add_command(label = "Agregar línea vertical a una imagen",command=lambda:[agregarF(6)])
Operaciones.add_command(label = "Agregar rectángulo",command=agregarR)
Operaciones.add_command(label = "Agregar triángulo rectángulo",command=agregarT)
Operaciones.add_command(label = "Unión A, B",command=lambda:[dosMat(9)])
Operaciones.add_command(label = "Intersección A, B",command=lambda:[dosMat(10)])
Operaciones.add_command(label = "Diferencia A, B",command=lambda:[dosMat(11)])
Operaciones.add_command(label = "Diferencia simétrica A, B",command=lambda:[dosMat(12)])

#Reportes
Reportes = Menu(Barra)
Reportes.config(bg = "#E74C3C",fg = "white")
Reportes.add_command(label = "Reporte HTML",command=reporte)

#Ayuda
Ayuda = Menu(Barra)
Ayuda.config(bg = "#E74C3C",fg = "white")
Ayuda.add_command(label = "Información del estudiante",command=datosEstudiante)
Ayuda.add_command(label = "Documentación del programa",command=Docu)

Barra.add_cascade(label = "Cargar archivo", menu = CargarArchivo)
Barra.add_cascade(label = "Operaciones", menu = Operaciones)
Barra.add_cascade(label = "Reportes", menu = Reportes)
Barra.add_cascade(label = "Ayuda", menu = Ayuda)

Ventana.config(menu = Barra)
Ventana.mainloop()