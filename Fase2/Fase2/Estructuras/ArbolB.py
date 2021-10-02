from Fase2.Estructuras.NodoArbolB import nodoArbolB
from Fase2.Estructuras.contenedor_nodos_arbolB import *
import copy,gc

gc.disable()


class arbolB:
    def __init__(self,orden):
        self.raiz=None
        self.orden=orden

    def agregar(self,dato:nodoArbolB):

        if self.raiz == None:
            self.raiz = Contenedor()
            Contenedor.agregar(self.raiz,dato.indice,dato,self.orden)
        else:
            #AQUI ESTA EL ERROR                        
            self.raiz = Contenedor.agregar(self.raiz,dato.indice,dato,self.orden)
            detectar_division([self.raiz,len(self.raiz.lista),self.raiz.padre],self.orden)         
            





            
        

