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

def reposicionar(arreglo,nodo:nodoHash,indice,tamaño):
    n=1
        
    #BUSCAR SI EXISTE YA EL INDICE Y LA INFORMACION
    if nodo.llave == arreglo[indice][1].llave:
        arreglo[indice][1]=nodo
        return arreglo
    


    anterior = 0    
    #SI HAY COLISION HACER REPOSICIONAMIENTO CUADRATICO
    while arreglo[indice][1].llave!=None:
        aumento = n*n                                   

        if indice+aumento >= tamaño:
            indice -=anterior
            indice = (indice+aumento)%tamaño            
        else:
            indice -=anterior
            indice += aumento 
            anterior = aumento
        n+=1
    
    arreglo[indice][1]=nodo
    return arreglo

def agregar(arreglo,nodo:nodoHash,indice,tamaño,apunte):
    #AGREGAR Y BUSCAR INDICE        
        n=1
        
        #BUSCAR SI EXISTE YA EL INDICE Y LA INFORMACION
        if nodo.llave == arreglo[indice][1].llave:
            arreglo[indice][1].lista.agregar(apunte)
            return [arreglo,0]
        #SI HUBO COLISION Y YA ESTA DENTRO DE LA TABLA HASH
        elif arreglo[indice][1].llave!=None:
            anterior = 0
            #SI HUBO COLISION Y HAY QUE ENCONTRAR DONDE ESTA
            for i in arreglo:
                if i[1].llave == nodo.llave:
                    i[1].lista.agregar(apunte)
                    return [arreglo,0]

        anterior = 0
        #SI HAY COLISION HACER REPOSICIONAMIENTO CUADRATICO
        while arreglo[indice][1].llave!=None:
            aumento = n*n                                   

            if indice+aumento >= tamaño:
                indice -=anterior
                indice = (indice+aumento)%tamaño
            else:
                indice -=anterior
                indice += aumento 
                anterior = aumento
            n+=1

        nodo.lista.agregar(apunte)
        arreglo[indice][1]=nodo
        return [arreglo,1]

class tablaHash(object):
    def __init__(self,tamaño):
        self.tabla_hash = []
        self.tamaño=tamaño
        self.datos_ingresados=0
        for i in range(0,self.tamaño):
            self.tabla_hash.append([i,nodoHash()])

    def funcion(self,k,m):
        return k%m

    def agregar(self,nodo:nodoHash,apunte):
        indice = self.funcion(nodo.llave,self.tamaño)

        resultado = agregar(self.tabla_hash,nodo,indice,self.tamaño,apunte)
        self.tabla_hash= resultado[0]
        self.datos_ingresados+= resultado[1]

        #REDIMENSIONAR TABLA HASH

        if self.datos_ingresados/self.tamaño >=0.5:
            self.tamaño=siguiente_primo(self.tamaño)

            aux=[]

            for i in range(0,self.tamaño):
                aux.append([i,nodoHash()])


            for j in self.tabla_hash:
                if j[1].llave !=None:
                    indice = self.funcion(j[1].llave,self.tamaño)
                    aux=reposicionar(aux,j[1],indice,self.tamaño)

            self.tabla_hash=aux





        
