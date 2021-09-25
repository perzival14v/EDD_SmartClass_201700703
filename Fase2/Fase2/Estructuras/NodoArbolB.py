import copy

class nodoArbolB:
    def __init__(self):
        self.info=None
        self.siguiente=None
        self.anterior=None
        self.padre=None
        self.hijoIzq=None
        self.hijoDer=None
        self.contador=0


    def agregar(self,dato):

        aux = self

        if aux.info == None:
            self.info = dato
        elif aux.info >= dato:
                
            ayuda = copy.deepcopy(self)
            self = nodoArbolB()
            self.info = dato
            self.siguiente = ayuda
            self.siguiente.anterior = self
                

        else:

            while aux.siguiente != None and aux.siguiente.info < dato:
                aux=aux.siguiente
                
            if aux.hijoDer != None:
                return self.agregar(aux.hijoDer,dato)
            else:                                          
                aux.siguiente = nodoArbolB()
                aux.siguiente.info = dato
                aux.siguiente.anterior = aux                
                
                
        return contar(self)

def contar(inicio):
        
    contador=0
    while inicio != None:
        contador=contador+1
        inicio = inicio.siguiente
    return contador
            
    

        
