from Fase2.Estructuras.NodoArbol import nodoArbol as nA
from Fase2.Objetos.Estudiantes import estudiante
import copy

def correccionNivel(nodo:nA):
    if nodo!=None:
        if nodo.izq != None:
            if nodo.der !=  None:
                if nodo.izq.nivel < nodo.der.nivel:
                    nodo.nivel = nodo.der.nivel + 1 
                else:
                    nodo.nivel = nodo.izq.nivel + 1 
            else:
                nodo.nivel = nodo.izq.nivel + 1 
        else:
            if nodo.der !=  None:
                nodo.nivel = nodo.der.nivel + 1        
            else:
                nodo.nivel=1
    return nodo

def ri(abuelo:nA):
    A = copy.deepcopy(abuelo)
    B = copy.deepcopy(abuelo.der)
    
    abuelo = copy.deepcopy(B)
    abuelo.izq = copy.deepcopy(A)

    abuelo.izq.der = B.izq

    abuelo.izq.der = correccionNivel(abuelo.izq.der)

    abuelo.izq = correccionNivel(abuelo.izq)
    abuelo.der = correccionNivel(abuelo.der)
    abuelo = correccionNivel(abuelo)


    return abuelo

def rd(abuelo:nA):
    A = copy.deepcopy(abuelo)
    B = copy.deepcopy(abuelo.izq)
        
    abuelo = copy.deepcopy(B)
    abuelo.der = copy.deepcopy(A)

    abuelo.der.izq = B.der

    abuelo.der.izq = correccionNivel(abuelo.der.izq)
    abuelo.izq = correccionNivel(abuelo.izq)
    abuelo.der = correccionNivel(abuelo.der)
    abuelo = correccionNivel(abuelo)

    return abuelo

def rdi(abuelo:nA):
    abuelo.der = rd(abuelo.der)
    return ri(abuelo)

def rid(abuelo:nA):
    abuelo.izq = ri(abuelo.izq)
    return rd(abuelo)

def agregar2(nodoActual:nA, indice, estudiante:estudiante):

    #RAMA DERECHA
    if indice >= nodoActual.indice :                 
        if nodoActual.der == None:
            nodoActual.der = nA()
            nodoActual.der.indice=indice
            nodoActual.der.info = estudiante

            #Calculo de niveles e hijos
            if nodoActual.der.nivel+1 > nodoActual.nivel:
                nodoActual.nivel = nodoActual.der.nivel+1
            

        else:
            nodoActual.der=agregar2(nodoActual.der,indice,estudiante)

            #Calculo de niveles e hijos

            if nodoActual.der.nivel+1 > nodoActual.nivel:
                nodoActual.nivel = nodoActual.der.nivel+1
                
                        


    #RAMA IZQUIERDA
    else:
        if nodoActual.izq == None:
            nodoActual.izq = nA()
            nodoActual.izq.indice=indice
            nodoActual.izq.info = estudiante
            #Calculo de niveles e hijos
            if nodoActual.izq.nivel+1 > nodoActual.nivel:
                nodoActual.nivel = nodoActual.izq.nivel+1
            

        else:
            nodoActual.izq=agregar2(nodoActual.izq,indice,estudiante)

            #Calculo de niveles e hijos
            if nodoActual.izq.nivel+1 > nodoActual.nivel:
                nodoActual.nivel = nodoActual.izq.nivel+1
                


    #Iniciamos el analisis de las rotaciones
    if nodoActual.izq == None:
        if nodoActual.der == None:
            balance = 0
        else:
            balance = 0 - nodoActual.der.nivel
    else:
        if nodoActual.der == None:
            balance = nodoActual.izq.nivel
        else:
            balance = nodoActual.izq.nivel - nodoActual.der.nivel    

    
    if balance <= -2:
            #Rotacion simple a la izquierda
        if nodoActual.der.indice< indice:
            nodoActual = ri(nodoActual)
        else:
            nodoActual = rdi(nodoActual)


    if balance >= 2:
            #Rotacion simple a la derecha
        if nodoActual.izq.indice> indice:
            nodoActual = rd(nodoActual)
        else:
            nodoActual = rid(nodoActual)
        
    
    

    return nodoActual
    
            
class arbolAVL:    

    def __init__(self):
        self.raiz= None  

    def agregar(self, indice, e:estudiante):
        if self.raiz == None:
            self.raiz = nA()
            self.raiz.indice = indice
            self.raiz.info = e
        else:                       
            self.raiz=agregar2(self.raiz, indice, e)
            
            
            
