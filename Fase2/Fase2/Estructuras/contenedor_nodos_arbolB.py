from Fase2.Estructuras.NodoArbolB import nodoArbolB

class Contenedor:
    def __init__(self):
        self.lista=[]
        self.padre=None
        self.contador=0

    @staticmethod
    def agregar(contenedor,indice:int,dato:nodoArbolB):

        index = 0
        contenedorUsado = contenedor

        if contenedor.lista == []:
            contenedor.lista.append(dato)
            return [contenedorUsado,len(contenedor.lista)]

        for x in contenedor.lista:

            if indice > x.indice:
                if x.hijoDer != None:
                    if index == len(contenedor.lista)-1:
                        return Contenedor.agregar(x.hijoDer,indice,dato)
                        
                    elif indice <= contenedor.lista[index+1].indice:
                        return Contenedor.agregar(x.hijoDer,indice,dato)
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
                    return Contenedor.agregar(x.hijoIzq,indice,dato)                    
                else:
                    contenedor.lista.insert(index,dato)
                    break


        return [contenedorUsado,len(contenedor.lista)]

    @staticmethod
    def agregar_y_quitar(contenedor_origen,contenedor_destino,indice:int,dato:nodoArbolB):
        Contenedor.agregar(contenedor_destino,indice,dato)
        contenedor_origen.lista.remove(dato)

    def subir_contenedor(contenedor_ascendente,contenedor_destino):
        contenedor_ascendente.padre = contenedor_destino.padre        

        Contenedor.agregar(contenedor_destino,
                            contenedor_ascendente.lista[0].indice,
                            contenedor_ascendente.lista[0])

        

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

        return [contenedor_destino,len(contenedor_destino.lista)]