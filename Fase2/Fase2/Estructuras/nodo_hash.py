from Fase2.Estructuras.ListaDoble import listaDoble


class nodoHash(object):

    def __init__(self,llave):
        self.llave=llave
        self.lista=listaDoble()