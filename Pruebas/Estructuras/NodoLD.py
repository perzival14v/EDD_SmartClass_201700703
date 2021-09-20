from Fase2.Estructuras import NodoArbol


class nodoLD:
    def __init__(self):
        self.info=None
        self.siguiente=None
        self.anterior=None
        self.conexion1=None
        self.conexion2=None
        

    @staticmethod
    def getNewNodo(info):
        
        n = nodoLD()
        n.info = info

        return n