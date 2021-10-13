from Fase2.Estructuras.NodoArbolB import nodoArbolB
import gc

gc.disable()


class Contenedor:
    def __init__(self):
        self.lista=[]
        self.padre=None
        self.contador=0

    @staticmethod
    def agregar(contenedor,indice:int,dato:nodoArbolB,orden):
        
        
        
        index = 0
        contenedorUsado = contenedor
        
        if contenedor.lista == []:
            contenedor.lista.append(dato)
            return [contenedorUsado,len(contenedor.lista)]

        for x in contenedor.lista:

            if indice > x.indice:
                if x.hijoDer != None:
                    if index == len(contenedor.lista)-1:
                                                                      
                        hoja = Contenedor.agregar(x.hijoDer,indice,dato,orden)                        
                        detectar_division([hoja,len(hoja.lista),contenedor],orden)
                        break
                    elif indice <= contenedor.lista[index+1].indice:
                        
                        hoja = Contenedor.agregar(x.hijoDer,indice,dato,orden)
                        detectar_division([hoja,len(hoja.lista),contenedor],orden)
                        break
                    else:
                        index += 1
                        continue
                else:
                    if index+1 == len(contenedor.lista):
                        
                        contenedor.lista.insert(index+1,dato)
                        break
                    else:
                        index+=1

            if indice <= x.indice:
                if x.hijoIzq != None:
                    
                    hoja = Contenedor.agregar(x.hijoIzq,indice,dato,orden)
                    detectar_division([hoja,len(hoja.lista),contenedor],orden) 
                    break                
                else:                    
                    contenedor.lista.insert(index,dato)
                    #detectar_division([contenedor,len(contenedor.lista),contenedor.padre],orden)  
                    break


        return contenedorUsado

    @staticmethod
    def agregar_mismo_nivel(contenedor,indice:int,dato:nodoArbolB,orden):
                        
        index = 0
        contenedorUsado = contenedor
        
        if contenedor.lista == []:
            contenedor.lista.append(dato)
            return [contenedorUsado,len(contenedor.lista)]

        for x in contenedor.lista:

            if indice > x.indice:                
                if index+1 == len(contenedor.lista):
                    
                    contenedor.lista.insert(index+1,dato)
                    break
                else:
                    index+=1

            if indice <= x.indice:                                   
                contenedor.lista.insert(index,dato)
                #detectar_division([contenedor,len(contenedor.lista),contenedor.padre],orden)  
                break


        return contenedorUsado

    @staticmethod
    def agregar_y_quitar(contenedor_origen,contenedor_destino,indice:int,dato:nodoArbolB,orden):
        Contenedor.agregar_mismo_nivel(contenedor_destino,indice,dato,orden)
        contenedor_origen.lista.remove(dato)

    def subir_contenedor(contenedor_ascendente,contenedor_destino,orden):
        contenedor_ascendente.padre = contenedor_destino.padre        

        Contenedor.agregar(contenedor_destino,
                            contenedor_ascendente.lista[0].indice,
                            contenedor_ascendente.lista[0],orden)

        

        #RALACIONAR LOS HIJOS DEL CONTENEDOR ASCENDENTE CON LOS DEL NODO DESTINO

        indice=0

        for i in contenedor_destino.lista:
            if i.indice == contenedor_ascendente.lista[0].indice:
                break
            else:
                indice+=1
        
        if indice == 0:
            contenedor_destino.lista[indice+1].hijoIzq = contenedor_destino.lista[indice].hijoDer
        elif indice > 0 and indice < len(contenedor_destino.lista)-1:
            contenedor_destino.lista[indice-1].hijoDer = contenedor_destino.lista[indice].hijoIzq
            contenedor_destino.lista[indice+1].hijoIzq = contenedor_destino.lista[indice].hijoDer
        else:
            contenedor_destino.lista[indice-1].hijoDer = contenedor_destino.lista[indice].hijoIzq

        #contenedor_ascendente.lista.remove(contenedor_ascendente.lista[0])

        #return [contenedor_destino,len(contenedor_destino.lista),contenedor_destino.padre ]

def eliminar_hijo(padre,hijo):

    for i in padre.lista:
        if i.hijoIzq == hijo:
            i.hijoIzq = None
        if i.hijoDer == hijo:
            i.hijoDer = None
        """if i == padre.lista[len(padre.lista)-1]:
            if i.hijoDer == hijo:
                i.hijoDer = None"""

def detectar_division(retorno,orden):
    if retorno[1] == orden:

        if retorno[2] != None:
            nodoMedio = dividir(orden,retorno[0])
            
            eliminar_hijo(retorno[2],retorno[0])
            
            Contenedor.subir_contenedor(nodoMedio,retorno[2],orden)
            
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
        separacion_izq,contenedor.lista[0].indice,
        contenedor.lista[0],orden) 

    separacion_izq.lista[len(separacion_izq.lista)-1].hijoDer = contenedor.lista[0].hijoIzq

    for j in range(1,len(contenedor.lista)):
        Contenedor.agregar_y_quitar(contenedor,
        separacion_der,
        contenedor.lista[1].indice,contenedor.lista[1],orden)
                            
    separacion_der.lista[0].hijoIzq = contenedor.lista[0].hijoDer
    


    contenedor.lista[0].hijoIzq = separacion_izq
    contenedor.lista[0].hijoIzq.padre = contenedor
    contenedor.lista[0].hijoDer = separacion_der
    contenedor.lista[0].hijoDer.padre = contenedor               

    return contenedor