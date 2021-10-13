import re

from Fase2.Estructuras.NodoLD import nodoLD


class listaDoble:
    def __init__(self):
        self.cabeza=None        
    
    def agregar(self, dato:nodoLD):

        nuevo = dato

        if type(dato) != nodoLD:
            nuevo = nodoLD()
            nuevo.info = dato

        if self.cabeza==None:
            self.cabeza = nuevo
        else:

            aux = self.cabeza

            while aux.siguiente != None:
                aux = aux.siguiente
            aux.siguiente = nuevo
            aux.siguiente.anterior = aux
    def buscar(self,id_buscado):
        
        aux = self.cabeza

        while aux!= None:
            if aux.info == id_buscado:
                return aux        
            aux = aux.siguiente

        return None

    def buscar_posicion(self,posicion):
        aux = self.cabeza
        contador=1

        while contador<posicion:                   
            aux = aux.siguiente
            contador+=1

        return aux.info
    
