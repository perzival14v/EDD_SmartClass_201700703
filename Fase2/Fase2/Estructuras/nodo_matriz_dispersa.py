from Fase2.Estructuras.ListaDoble import *

class nodoMatrizDispersa:
    def __init__(self):
        self.arriba=None
        self.abajo=None
        self.izq=None
        self.der=None
        self.info=listaDoble()
        self.posicion = [-1,-1]
        self.tag=0