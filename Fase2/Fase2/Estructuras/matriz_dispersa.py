from re import T
from Fase2.Estructuras.nodo_matriz_dispersa import *

class matrizDispersa:
    def __init__(self):
        self.raiz=nodoMatrizDispersa()
        self.der=None
        self.izq=None        


    def agregar(self,fila:int,columna:int,dato):

        #columna
        box = self.raiz
        #fila
        box2 = self.raiz

        #SE USAN ESTAS VARIABLES EN (AGREGANDO NODOS DENTRO DE LA MATRIZ)
        row = None
        column = None
        entrar1 = True
        entrar2 = True
        

    #COLUMNAS-------------------------------------------------------------------------------
        #Verificando que exista la columna
        while box.der != None:
            if columna > box.der.posicion[1]:
                box = box.der
            else:
                break


        #SI EL NODO ES MAS GRANDE QUE LOS EXISTENTES
        if box.der == None:
            box.der = nodoMatrizDispersa()            
            box.der.izq = box            
            box.der.posicion[1] = columna
            box.der.tag = "Dia: " + str(columna)
            
            
        #SI EL NODO YA EXISTE
        elif columna == box.der.posicion[1]:
            entrar1 = False
        
        #SI EL NODO NO EXISTE Y ES MENOR A UNO EXISTENTE
        else:
            nuevo = nodoMatrizDispersa()
            nuevo.posicion[1] = columna

            nuevo.der = box.der
            nuevo.izq = box
            nuevo.der.izq = nuevo
            box.der = nuevo
            box.der.tag = "Dia: " + str(columna)
            
    #FILAS --------------------------------------------------------------------
        while box2.abajo != None:
            if  fila > box2.abajo.posicion[0]:
                box2 = box2.abajo
            else:
                break
        #der = abajo, izq = arriba
        #SI EL NODO ES MAS GRANDE QUE LOS EXISTENTES
        if box2.abajo == None:
            box2.abajo = nodoMatrizDispersa()            
            box2.abajo.arriba = box2            
            box2.abajo.posicion[0] = fila
            box2.abajo.tag="Hora: " + str(fila)
            
            
        #SI EL NODO YA EXISTE
        elif fila == box2.abajo.posicion[0]:
            entrar2 = False
                        
        
        #SI EL NODO NO EXISTE Y ES MENOR A UNO EXISTENTE
        else:
            nuevo2 = nodoMatrizDispersa()
            nuevo2.posicion[0] = fila

            nuevo2.abajo = box2.abajo
            nuevo2.arriba = box2
            nuevo2.abajo.arriba = nuevo2
            box2.abajo = nuevo2
            box2.abajo.tag="Hora: " + str(fila)
        
        
        #AGREGANDO NODOS DENTRO DE LA MATRIZ----------------------------------------------------------------
        row = box2.abajo
        column = box.der
        nuevo_dentro=nodoMatrizDispersa()

        while row.der != None :
            if columna > row.der.posicion[1]:
                row = row.der
            else:
                break

        #SI EL NODO ES MAS GRANDE QUE LOS EXISTENTES
        if row.der == None:
            row.der = nuevo_dentro   
            row.der.izq = row            
            row.der.posicion[1] = columna
            row.der.info.agregar(dato)
            row.der.tag+=1
            
        #SI EL NODO YA EXISTE
        elif columna == row.der.posicion[1]:
            row.der.info.agregar(dato)
            row.der.tag+=1
        
        
        #SI EL NODO NO EXISTE Y ES MENOR A UNO EXISTENTE
        else:            
            nuevo_dentro.posicion[1] = columna

            nuevo_dentro.der = row.der
            nuevo_dentro.izq = row
            nuevo_dentro.der.izq = nuevo_dentro
            row.der = nuevo_dentro
            row.der.info.agregar(dato)
            row.der.tag+=1
        #COLUMNAS ---------------------------------------------------------------------

        while column.abajo != None :
            if fila > column.abajo.posicion[0]: 
                column = column.abajo
            else:
                break

        
        #SI EL NODO ES MAS GRANDE QUE LOS EXISTENTES
        if column.abajo == None:
            column.abajo = nuevo_dentro           
            column.abajo.arriba = column            
            column.abajo.posicion[0] = fila

        elif fila == column.abajo.posicion[0]:
            x=1                        
        
        #SI EL NODO NO EXISTE Y ES MENOR A UNO EXISTENTE
        else:            
            nuevo_dentro.posicion[0] = fila

            nuevo_dentro.abajo = column.abajo
            nuevo_dentro.arriba = column
            nuevo_dentro.abajo.arriba = nuevo_dentro
            column.abajo = nuevo_dentro
        
            