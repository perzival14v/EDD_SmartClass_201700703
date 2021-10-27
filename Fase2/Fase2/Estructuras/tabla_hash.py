import re
from Fase2.Estructuras.nodo_hash import nodoHash

def siguiente_primo(numero):    
    prueba = numero+1    
    esprimo=False
    while numero < prueba:
        for n in range(2, prueba):
            if prueba % n == 0:
                esprimo=False
                break
            else:
                esprimo=True
        if esprimo:
            return prueba    
        else:
            prueba+=1        

def agregar(diccionario,nodo:nodoHash,indice,tamaño,apunte):
    #AGREGAR Y BUSCAR INDICE        
        n=1
        
        if nodo.llave == diccionario[indice].llave:
            diccionario[indice].lista.agregar(apunte)
            return diccionario


        while indice in diccionario:
            aumento = n*n                           

            if indice+aumento > tamaño:
                indice = (indice+aumento)%tamaño
            else:
                indice += aumento
            n+=1

        nodo.lista.agregar(apunte)
        diccionario[indice]=nodo
        return diccionario

class tablaHash(object):
    def __init__(self,tamaño):
        self.tabla_hash = {}
        self.tamaño=tamaño
        self.datos_ingresados=0

    def funcion(k,m):
        return k%m

    def agregar(self,nodo:nodoHash,apunte):
        indice = self.funcion(nodo.llave,self.tamaño)

        self.tabla_hash=agregar(self.tabla_hash,nodo,indice,self.tamaño,apunte)
        self.datos_ingresados+=1

        #REDIMENSIONAR TABLA HASH

        if self.datos_ingresados/self.tamaño >=0.5:
            self.tamaño=siguiente_primo(self.tamaño)

            aux={}

            for y in self.tabla_hash.values():
                indice = self.funcion(y.llave,self.tamaño)
                aux=agregar(aux,y,indice,self.tamaño)

            self.tabla_hash=aux





        
