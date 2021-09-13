from Estructuras.NodoArbol import nodoArbol as nA

    

def agregar2(nodoActual:nA, nuevoNodo:nA):
    if nuevoNodo.info >= nodoActual.info and nodoActual.der == None :
        nodoActual.der = nuevoNodo
         
    else:
         agregar2(nodoActual.der,nuevoNodo)
    
    if nuevoNodo.info < nodoActual.info and nodoActual.izq == None :
       nodoActual.izq = nuevoNodo
        
    else:
        agregar2(nodoActual.izq,nuevoNodo)

    
            
class arbolAVL:    

    def __init__(self):
        self.raiz= nA(-1)   

    def agregar(self, nuevoNodo:nA):
        if self.raiz == None:
            self.raiz = nuevoNodo
        else:                       
            agregar2(self.raiz, nuevoNodo)