from nodo import Nodo
from lista_orto import ListaOrtogonal
import xml.etree.cElementTree as ET
import time

class ListaCircular():
    def __init__ (self):
        self.primero = None
        self.ultimo = None
    
    def vacia(self):
        return self.primero == None

    def Agregar(self,dato,nombre):
        if self.vacia():
            self.primero = self.ultimo = Nodo(dato,nombre)
            self.ultimo.siguiente = self.primero
        else:
            aux = self.ultimo
            self.ultimo = aux.siguiente = Nodo(dato,nombre)
            self.ultimo.siguiente = self.primero
        
    def Recorrer(self):
        aux = self.primero
        if aux != None :
            while aux.siguiente != self.primero:
                print(aux.nombre)
                aux.dato.MostrarMat()
                aux = aux.siguiente
            (aux.nombre) 
            aux.dato.MostrarMat()
        else:
            print("No hay datos")  

    def Nombres(self):
        aux = self.primero
        nombres = ""
        if aux != None :
            while aux.siguiente != self.primero:
                nombres = nombres + aux.nombre + ","
                aux = aux.siguiente
            nombres = nombres + aux.nombre 
        else:
            print("No hay datos")
        return nombres

    def buscarMat(self,nombre,accion):
        aux = self.primero
        if aux != None :
            while aux.siguiente != self.primero:
                if str(aux.nombre) == str(nombre):
                    if accion == 1:
                        aux.dato.imagen(nombre)
                        aux.dato.rotH()
                        aux.dato.imagen(nombre+"rotH")
                    elif accion == 2:
                        aux.dato.imagen(nombre)
                        aux.dato.rotV()
                        aux.dato.imagen(nombre+"rotV")
                    elif accion == 3:
                        aux.dato.imagen(nombre)
                        aux.dato.tran()
                        aux.dato.imagen(nombre+"tran")
                aux = aux.siguiente
            if str(aux.nombre )== str(nombre):
                if accion == 1:
                    aux.dato.imagen(nombre)
                    aux.dato.rotH()
                    aux.dato.imagen(nombre+"rotH")
                elif accion == 2:
                    aux.dato.imagen(nombre)
                    aux.dato.rotV()
                    aux.dato.imagen(nombre+"rotV")
                elif accion == 3:
                    aux.dato.imagen(nombre)
                    aux.dato.tran()
                    aux.dato.imagen(nombre+"tran")
        else:
            print("No hay datos")

    def buscarMat2(self,nombre,f,c,cant,accion):
        aux = self.primero
        if aux != None :
            while aux.siguiente != self.primero:
                if str(aux.nombre) == str(nombre):
                    if accion == 5:
                        aux.dato.imagen(nombre)
                        aux.dato.agreH(f, c, cant)
                        aux.dato.imagen(nombre+"agreH")
                    elif accion == 6:
                        aux.dato.imagen(nombre)
                        aux.dato.agreV(f, c, cant)
                        aux.dato.imagen(nombre+"agreV")
                    elif accion == 8:
                        aux.dato.imagen(nombre)
                        aux.dato.agreT(f, c, cant)
                        aux.dato.imagen(nombre+"agreT")                
                aux = aux.siguiente
            if str(aux.nombre )== str(nombre):
                if accion == 5:
                    aux.dato.imagen(nombre)
                    aux.dato.agreH(f, c, cant)
                    aux.dato.imagen(nombre+"agreH")
                elif accion == 6:
                    aux.dato.imagen(nombre)
                    aux.dato.agreV(f, c, cant)
                    aux.dato.imagen(nombre+"agreV")
                elif accion == 8:
                    aux.dato.imagen(nombre)
                    aux.dato.agreT(f, c, cant)
                    aux.dato.imagen(nombre+"agreT")
        else:
            print("No hay datos")

    def buscarMat3(self,nombre,f1,c1,f2,c2,accion):
        aux = self.primero
        if aux != None :
            while aux.siguiente != self.primero:
                if str(aux.nombre) == str(nombre):
                    if accion == 4:
                        aux.dato.imagen(nombre)
                        aux.dato.limpiar(f1,c1,f2,c2)
                        aux.dato.imagen(nombre+"limp")
                    elif accion == 7:
                        aux.dato.imagen(nombre)
                        aux.dato.agreR(f1,c1,f2,c2)
                        aux.dato.imagen(nombre+"agreR")             
                aux = aux.siguiente
            if str(aux.nombre )== str(nombre):
                if accion == 4:
                    aux.dato.imagen(nombre)
                    aux.dato.limpiar(f1,c1,f2,c2)
                    aux.dato.imagen(nombre+"limp")
                elif accion == 7:
                    aux.dato.imagen(nombre)
                    aux.dato.agreR(f1,c1,f2,c2)
                    aux.dato.imagen(nombre+"agreR") 
        else:
            print("No hay datos")

    def ElegirNombre(self):
        nombres = ""
        aux = self.primero
        auxi = self.primero
        busq = None
        if aux != None:
            while aux.siguiente != self.primero:
                nombres = nombres + aux.nombre + ","
                aux = aux.siguiente
            nombres = nombres + aux.nombre + ","
            a = nombres.split(",")
            for i in range(1,len(a)+1):
                print(str(i)+"-"+a[i-1])
            elegido = int(input("Elija una opción: "))
            var = True
            for i in range(1,len(a)+1):
                if elegido == i:
                    busq = a[i-1]
                    var = False
            if(auxi != None):           
                while auxi.siguiente != self.primero:
                    if busq == auxi.nombre:
                        nn = auxi.dato.NoFilas()
                        mm = auxi.dato.NoColumnas()
                        auxi.dato.Grafo(busq,mm,nn)
                    auxi = auxi.siguiente
                    if busq == auxi.nombre and auxi.siguiente ==self.primero:
                        nn = auxi.dato.NoFilas()
                        mm = auxi.dato.NoColumnas()
                        auxi.dato.Grafo(busq,mm,nn)
            if var:
                print("Opcion no valida")     
        else:
            print("***No se a cargado ningun archivo de entrada")

 
     


                 

