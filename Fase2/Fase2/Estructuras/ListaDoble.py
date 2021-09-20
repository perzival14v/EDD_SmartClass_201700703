from Estructuras.NodoLD import nodoLD

class listaDoble:
    def __init__(self):
        self.cabeza=None        
    
    def agregar(self, nuevo:nodoLD):
        if self.cabeza==None:
            self.cabeza = nuevo
        else:

            aux = self.cabeza

            while aux.siguiente != None:
                aux = aux.siguiente
            aux.siguiente = nuevo
    