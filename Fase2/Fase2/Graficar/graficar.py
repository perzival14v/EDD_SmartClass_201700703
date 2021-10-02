from re import T
from Fase2.Estructuras.NodoLD import nodoLD
from Fase2.Estructuras.NodoArbolAVL import nodoArbol
from Fase2.Estructuras.ArbolB import arbolB
from typing import Type
import graphviz
from graphviz import nohtml


def graficarArbolAVLrecursivo(nodo:nodoArbol, g):
    if nodo != None:
        if nodo.izq != None:

            g.node(str(nodo.indice), label=str(str(nodo.indice)+"\n"+str(nodo.info.nombre)+"\n"+str(nodo.info.carrera)))
            g.node(str(nodo.izq.indice), label=str(str(nodo.izq.indice)+"\n"+str(nodo.izq.info.nombre)+"\n"+str(nodo.izq.info.carrera)))

            g.edge(str(nodo.indice),str(nodo.izq.indice))
            graficarArbolAVLrecursivo(nodo.izq, g)
        
        if nodo.der != None:  

            g.node(str(nodo.indice), label=str(str(nodo.indice)+"\n"+str(nodo.info.nombre)+"\n"+str(nodo.info.carrera)))
            g.node(str(nodo.der.indice), label=str(str(nodo.der.indice)+"\n"+str(nodo.der.info.nombre)+"\n"+str(nodo.der.info.carrera)))

            g.edge(str(nodo.indice),str(nodo.der.indice))
            graficarArbolAVLrecursivo(nodo.der, g)
    else:
        return

def graficarArbolAVL(nodo:nodoArbol, contador):
    g = graphviz.Digraph('G', filename='Graficas/arbolAVL' + str(contador) + '.gv', format='svg')
    g.attr("node", shape="box")
    g.attr(splines="ortho")
    g.attr(nodesep="0.5")

    graficarArbolAVLrecursivo(nodo, g)        
    
    g.view()

def graficarLD(nodo:nodoLD, contador):

    g = graphviz.Digraph('G', filename='Graficas/listaDoble' + str(contador) + '.gv', format='svg')

    while nodo.siguiente != None:
        g.edge(str(nodo.info),str(nodo.siguiente.info))
        nodo = nodo.siguiente      
            
    g.graph_attr['rankdir'] = 'LR'
    g.edge_attr['dir'] = 'both'

    g.view()
#cr = contador recursivo
def graficar_arbol_b_recursivo(arbolB:arbolB, g, cr):
    contador=1 
    pos=0  
    nombre="nodo" + str(cr[0]) + "|" + str(cr[2]) + cr[1] + "|" + str(pos)
    regreso=[nombre,"cluster_"+nombre+"_contenedor"]
    infoDentroNodo=""
    
    #nodo # <- indica el nivel del arbol | # <- indica del nodo que proviene |# <- indica la posicion dentro del nivel

    for i in arbolB.lista:

        infoDentroNodo= str(i.indice) 
        tag = "nodo" + str(cr[0]) + "|" + str(cr[2]) + cr[1] + "|" + str(pos)
        creado = False


        if i.hijoIzq != None:
            #CAMINO SI EL NODO ACTUAL TIENE UN HIJO IZQUIERDO 
                        
            with g.subgraph(name='cluster_'+nombre+"_contenedor") as c:   
                c.graph_attr['rankdir'] = 'LR' 
                c.node(tag, nohtml("<f0> |<f1>" + str(i.indice) + "|<f2>"))

            retorno =  graficar_arbol_b_recursivo(i.hijoIzq,g,[cr[0]+1,"I", tag])         
            g.edge(tag+":f0",retorno[0] , lhead=retorno[1])
            creado = True

        if i != arbolB.lista[len(arbolB.lista)-1] and pos != 0:

            #CAMINO SI YA TERMINO CON LOS HIJOS IZQUIERDO Y ES DIFERENTE AL ULTIMO NODO
            if not creado:
                #PRIMER NODO
                with g.subgraph(name='cluster_'+nombre+"_contenedor") as c:   
                    c.graph_attr['rankdir'] = 'LR'
                    c.node(tag, nohtml("<f0> |<f1>" + infoDentroNodo + "|<f2>"))

            #SEGUNDO NODO
            
            tagAnterior = "nodo" + str(cr[0]) + "|" + str(cr[2]) + cr[1] + "|" + str(pos-1)          


            #CONEXION ENTRE LOS NODOS        
            g.edge(tag+":f0",tagAnterior+":f2")

            
        else:
            #CAMINO SI ES EL ULTIMO NODO EN LA LISTA (SE TERMINA CON EL NODO DERECHO)
            if i.hijoDer != None and pos+1 == len(arbolB.lista):

                with g.subgraph(name='cluster_'+nombre+"_contenedor") as c:   
                    c.graph_attr['rankdir'] = 'LR'             
                    c.node(tag, nohtml("<f0> |<f1>" + infoDentroNodo + "|<f2>"))

                retorno = graficar_arbol_b_recursivo(i.hijoDer,g,[cr[0]+1,"D", tag])                           
                g.edge(tag+":f2",retorno[0], lhead=retorno[1]) 
                
                                
                if pos != 0:
                    tagAnterior = "nodo" + str(cr[0]) + "|" + str(cr[2]) + cr[1] + "|" + str(pos-1)                       
                    #g.edge(tag+":f0",tagAnterior+":f2")                    
            else:      
                #CAMINO SI ES EL ULTIMO NODO EN LA LISTA Y NO TIENE HIJO DERECHO
                if not creado:
                    with g.subgraph(name='cluster_'+nombre+"_contenedor") as c:   
                        c.graph_attr['rankdir'] = 'LR'             
                        c.node(tag, nohtml("<f0> |<f1>" + infoDentroNodo + "|<f2>"))                    
                
                if pos != 0:
                    tagAnterior = "nodo" + str(cr[0]) + "|" + str(cr[2]) + cr[1] + "|" + str(pos-1)                       
                    #g.edge(tag+":f0",tagAnterior+":f2")

        pos+=1

    return regreso

def graficar_arbol_b(arbolB:arbolB, contador):
    g = graphviz.Digraph('G', filename='Graficas/arbolB' + str(contador) + '.gv', format='svg'
                        , node_attr={'shape':'record', 'height': '.1'})    
    
    g.attr(nodesep="0.5")
    g.attr(compound="true")
    
        
    #contador esta adelantado en una posicion para poder elegir el siguiente nodo de la lista
    contador = 1

    nivel=0
    pos=0
    infoDentroNodo=""

    #nodo # <- indica el nivel del arbol _ # <- indica la posicion dentro del nivel

    for i in arbolB.raiz.lista:

        creado=False
        infoDentroNodo= str(i.indice) 
        tag = "nodo" + str(nivel) + "_" + str(pos)


        if i.hijoIzq != None:
            #CAMINO SI EL NODO ACTUAL TIENE UN HIJO IZQUIERDO                        
            
            with g.subgraph(name='cluster_raiz') as c:   
                c.graph_attr['rankdir'] = 'LR'             
                c.node(tag, nohtml("<f0> |<f1>" + infoDentroNodo + "|<f2>"))

            retorno = graficar_arbol_b_recursivo(i.hijoIzq,g,[1,"I", tag])
            g.edge(tag+":f0", retorno[0], lhead=retorno[1])            
            creado = True
            

        if i != arbolB.raiz.lista[len(arbolB.raiz.lista)-1] and pos != 0:
            #CAMINO SI YA TERMINO CON LOS HIJOS IZQUIERDO Y ES DIFERENTE AL ULTIMO NODO
            
            if not creado:
                #PRIMER NODO
                with g.subgraph(name='cluster_raiz') as c:   
                    c.graph_attr['rankdir'] = 'LR'             
                    c.node(tag, nohtml("<f0> |<f1>" + infoDentroNodo + "|<f2>"))                
                creado = True

            #SEGUNDO NODO (anterior)             
            tagAnterior = "nodo" + str(nivel) + "_" + str(pos-1)
           

            #CONEXION ENTRE LOS NODOS        
            g.edge(tag+":f0",tagAnterior+":f2")
            
            contador+=1
        else:
            #CAMINO SI ES EL ULTIMO NODO EN LA LISTA (SE TERMINA CON EL NODO DERECHO)
            if i.hijoDer != None and pos+1 == len(arbolB.raiz.lista):
                #g.node(tag, nohtml("<f0> |<f1>" + infoDentroNodo + "|<f2>"))

                with g.subgraph(name='cluster_raiz') as c:   
                    c.graph_attr['rankdir'] = 'LR'             
                    c.node(tag, nohtml("<f0> |<f1>" + infoDentroNodo + "|<f2>"))

                retorno = graficar_arbol_b_recursivo(i.hijoDer,g,[1,"D", tag])                             
                g.edge(tag+":f2",retorno[0], lhead=retorno[1])               

                if pos != 0:
                    tagAnterior = "nodo" + str(nivel) + "_" + str(pos-1)                         
                    #g.edge(tag+":f0",tagAnterior+":f2")
                    

                
            else:
                #CAMINO SI ES EL ULTIMO NODO EN LA LISTA Y NO TIENE HIJO DERECHO
                if not creado:                                    
                    g.node(tag, nohtml("<f0> |<f1>" + infoDentroNodo + "|<f2>"))
                    creado = True

                if pos != 0:
                    tagAnterior = "nodo" + str(nivel) + "_" + str(pos-1)                         
                    #g.edge(tag+":f0",tagAnterior+":f2")
                    
                

        pos+=1
                                
    g.edge_attr['dir'] = 'both'
    

    
    g.view()
