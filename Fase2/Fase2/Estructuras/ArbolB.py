from Fase2.Estructuras.NodoArbolB import nodoArbolB
import copy

class arbolB:
    def __init__(self,orden):
        self.raiz=None
        self.orden=orden

    def agregar(self,dato):

        if self.raiz == None:
            self.raiz = nodoArbolB()
            self.raiz.agregar(dato)
        else:
            
            retorno = self.raiz.agregar(dato)

            if retorno == self.orden:
                self.raiz = dividir(self.orden,self.raiz)

def dividir(orden,nodo:nodoArbolB):
    if orden%2==1:
        posicion = (orden+1)/2
        contador=1
        aux = nodo

        separacion_izq = nodoArbolB()
        centro=nodoArbolB()

        while contador != posicion:
            separacion_izq.agregar(aux.info)            
            aux = aux.siguiente
            contador = contador + 1        

        centro = aux

        centro.hijoIzq = separacion_izq
        separacion_izq.padre = centro
        centro.hijoDer = centro.siguiente
        centro.hijoDer.padre = centro

        centro.anterior.siguiente = None
        centro.anterior = None
        centro.siguiente.anterior = None
        centro.siguiente = None


    return centro


            
        

