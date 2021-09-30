from Fase2.Estructuras.NodoArbolB import nodoArbolB
from Fase2.Estructuras.contenedor_nodos_arbolB import *
import copy

class arbolB:
    def __init__(self,orden):
        self.raiz=None
        self.orden=orden

    def agregar(self,dato:nodoArbolB):

        if self.raiz == None:
            self.raiz = Contenedor()
            Contenedor.agregar(self.raiz,dato.indice,dato)
        else:
            
            retorno = Contenedor.agregar(self.raiz,dato.indice,dato)

            padre = retorno[0]
            padre = detectar_division(retorno,self.orden)

def eliminar_hijo(padre,hijo):

    for i in padre.lista:
        if i.hijoIzq == hijo:
            i.hijoIzq = None
        if i == padre.lista[len(padre.lista)-1]:
            if i.hijoDer == hijo:
                i.hijoDer = None


def detectar_division(retorno,orden):
    if retorno[1] == orden:

        if retorno[0].padre != None:
            nodoMedio = dividir(orden,retorno[0])
            
            eliminar_hijo(retorno[0].padre,retorno[0])
            
            retorno2 = Contenedor.subir_contenedor(nodoMedio,retorno[0].padre)
            return detectar_division(retorno2,orden)
        else:
            return dividir(orden,retorno[0])                      

def dividir(orden,contenedor:Contenedor):
    if orden%2==1:
        posicion = (orden+1)/2                
    else:
        posicion = orden/2 


    separacion_izq = Contenedor()
    separacion_der = Contenedor() 


    for i in range(int(posicion-1)):
        Contenedor.agregar_y_quitar(contenedor,
        separacion_izq,contenedor.lista[i].indice,
        contenedor.lista[i]) 

    separacion_izq.lista[len(separacion_izq.lista)-1].hijoDer = contenedor.lista[0].hijoIzq

    for j in range(1,len(contenedor.lista)):
        Contenedor.agregar_y_quitar(contenedor,
        separacion_der,
        contenedor.lista[j].indice,contenedor.lista[j])
                            
    separacion_der.lista[0].hijoIzq = contenedor.lista[0].hijoDer
    


    contenedor.lista[0].hijoIzq = separacion_izq
    contenedor.lista[0].hijoIzq.padre = contenedor
    contenedor.lista[0].hijoDer = separacion_der
    contenedor.lista[0].hijoDer.padre = contenedor               

    return contenedor


            
        

