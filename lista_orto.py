from nodo1 import Nodo1
import os
class ListaOrtogonal():
    def __init__ (self):
        self.inicio = None
        
    def CrearMatriz(self,n,m,Datos):
        q = None
        s = None
        k = 0
        for i in range(1,n+1):
            for j in range(1,m+1):
                nuevoNodo = Nodo1(Datos[k])
                k = k + 1
                nuevoNodo.siguiente = None
                nuevoNodo.abajo = None
                if j == 1:
                    nuevoNodo.anterior = None
                    if self.inicio == None:
                        self.inicio = nuevoNodo
                    q = nuevoNodo
                else:
                    nuevoNodo.anterior = q
                    q.siguiente = nuevoNodo
                    q = nuevoNodo
                if i == 1:
                    nuevoNodo.arriba = None
                    q = nuevoNodo
                else:
                    nuevoNodo.arriba = s
                    s.abajo = nuevoNodo
                    s = s.siguiente
            s = self.inicio
            while s.abajo != None:
                s = s.abajo


    def MostrarMat(self):
        if self.inicio != None:
            aux = self.inicio
            while aux != None:
                auxi = aux
                while auxi != None:
                    auxi.Mostrar()
                    auxi = auxi.siguiente
                aux = aux.abajo
                print("")
                
    def NoFilas(self):
        pp = self.inicio
        fila = 0
        while pp.abajo != None:
            fila = fila + 1
            pp = pp.abajo
        fila = fila + 1
        return fila

    def NoColumnas(self):
        pp = self.inicio
        colum = 0
        while pp.siguiente != None:
            colum = colum + 1
            pp = pp.siguiente
        colum = colum + 1
        return colum

    def imagen(self,nombre):
        file = open("Reporte.dot","w")
        file.write("digraph G {node [fontname=\"Arial\"];node_A [shape=record    label=\"")

        p = self.inicio
        i = 1
        file.write("{"+str(nombre)+"|")
        while p != None:
            file.write(str(i))
            i = i + 1
            p = p.abajo
            if p != None:
                file.write("|")
        file.write("}|")

        aux = self.inicio
        s = 1
        while aux != None:
            file.write("{"+str(s)+"|")
            auxi = aux
            while auxi != None:
                file.write(auxi.getDato())
                auxi = auxi.abajo
                if auxi != None:
                    file.write("|")
            aux = aux.siguiente
            file.write("}")
            s = s + 1
            if aux != None:
                file.write("|")
   
        file.write("\"];} ")
        file.close()
        os.system("dot -Tpng Reporte.dot -o "+str(nombre)+".png")

    

    def rotH(self):
        aux = self.inicio
        while aux != None:
            auxi = aux
            while auxi != None:
                p = auxi.abajo
                auxi.abajo = auxi.arriba
                auxi.arriba = p
                auxi = auxi.siguiente
            if aux.arriba == None:
                self.inicio = aux
            aux = aux.arriba

    def rotV(self):
        aux = self.inicio
        while aux != None:
            auxi = aux
            while auxi != None:
                p = auxi.siguiente
                auxi.siguiente = auxi.anterior
                auxi.anterior = p
                auxi = auxi.abajo
            if aux.anterior == None:
                self.inicio = aux
            aux = aux.anterior

    def tran(self):
        aux = self.inicio
        while aux != None:
            auxi = aux
            while auxi != None:
                p = auxi.abajo
                auxi.abajo = auxi.siguiente
                auxi.siguiente = p
                p = auxi.anterior
                auxi.anterior = auxi.arriba
                auxi.arriba = p
                auxi = auxi.abajo
            aux = aux.siguiente

    def limpiar(self,f1,c1,f2,c2):
        aux = self.inicio      
        f = f2 - f1
        c = c2 - c1
        p = None
        encontrado = False
        for i in range(1,self.NoColumnas()+1):
            auxi = aux
            for j in range(1,self.NoFilas()+1):
                if i == f1 and j == c1:
                    p = auxi
                    encontrado = True
                    break
                auxi = auxi.siguiente
            if encontrado:
                break
            aux = aux.abajo

        for i in range(0, f+1):
            q = p
            for j in range(0,c+1):
                q.setDato(" ")
                q = q.siguiente
            p = p.abajo
            
    def agreH(self,f,c,a):
        aux = self.inicio
        p = None
        encontrado = False
        for i in range(1,self.NoColumnas()+1):
            auxi = aux
            for j in range(1,self.NoFilas()+1):
                if i == f and j == c:
                    p = auxi
                    encontrado = True
                    break
                auxi = auxi.siguiente
            if encontrado:
                break
            aux = aux.abajo
        for i in range(0, a):
            p.setDato("*")
            p = p.siguiente

    def agreV(self,f,c,a):
        aux = self.inicio
        p = None
        encontrado = False
        for i in range(1,self.NoColumnas()+1):
            auxi = aux
            for j in range(1,self.NoFilas()+1):
                if i == f and j == c:
                    p = auxi
                    encontrado = True
                    break
                auxi = auxi.siguiente
            if encontrado:
                break
            aux = aux.abajo
        for i in range(0, a):
            p.setDato("*")
            p = p.abajo
        
    def agreR(self,f,c,a,b):
        aux = self.inicio
        p = None
        q = None
        encontrado = False
        for i in range(1,self.NoColumnas()+1):
            auxi = aux
            for j in range(1,self.NoFilas()+1):
                if i == f and j == c:
                    p = auxi
                    r = auxi
                    encontrado = True
                    break
                auxi = auxi.siguiente
            if encontrado:
                break
            aux = aux.abajo
        
        for i in range(0, a-1):
            p.setDato("*")
            p = p.abajo
        q = p
        for i in range(0, b):
            q.setDato("*")
            r.setDato("*")
            s = r
            q = q.siguiente
            r = r.siguiente
        for i in range(0, a-1):
            s.setDato("*")
            s = s.abajo

    def agreT(self,f,c,a):
        aux = self.inicio
        p = None
        q = None
        encontrado = False
        for i in range(1,self.NoColumnas()+1):
            auxi = aux
            for j in range(1,self.NoFilas()+1):
                if i == f and j == c:
                    p = auxi
                    s = auxi
                    encontrado = True
                    break
                auxi = auxi.siguiente
            if encontrado:
                break
            aux = aux.abajo
        
        for i in range(0, a-1):
            p.setDato("*")
            p = p.abajo
        q = p
        for i in range(0, a):
            q.setDato("*")
            q = q.siguiente

        for i in range(0, a-1):
            s = s.abajo
            s = s.siguiente
            s.setDato("*")
        
