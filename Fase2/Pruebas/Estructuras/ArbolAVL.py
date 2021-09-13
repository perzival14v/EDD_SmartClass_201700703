from Estructuras.NodoArbol import nodoArbol as nA
import copy
    

def agregar2(nodoActual:nA, dato):
    if dato >= nodoActual.info :                 
        if nodoActual.der == None:
            nodoActual.der = nA()
            nodoActual.der.info=dato
        else:
            agregar2(nodoActual.der,dato)
    
    if dato < nodoActual.info and nodoActual.izq == None :
        if nodoActual.izq == None:
            nodoActual.izq = nA()
            nodoActual.izq.info=dato
        else:
            agregar2(nodoActual.izq,dato)

    
            
class arbolAVL:    

    def __init__(self):
        self.raiz= None  

    def agregar(self, dato):
        if self.raiz == None:
            self.raiz = nA()
            self.raiz.info = dato
        else:                       
            agregar2(self.raiz, dato)