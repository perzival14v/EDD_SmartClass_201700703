from logging import info
from re import T
import re
from Fase2.Estructuras.NodoLD import nodoLD
from Fase2.Estructuras.NodoArbolAVL import nodoArbol
from Fase2.Estructuras.ArbolB import arbolB
from Fase2.Estructuras.matriz_dispersa import matrizDispersa
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
def graficar_arbol_b_recursivo(arbolB:arbolB, g, numeracion):
    #contador esta adelantado en una posicion para poder elegir el siguiente nodo de la lista
    contador = 1
    textoNodo = ""
    pos=0
    secc=0

    tag = "node" + str(numeracion)

    for a in arbolB.lista:
        infoNodo = str(a.indice) + "--" + a.info.nombre 

        if secc != len(arbolB.lista)-1:
            textoNodo = textoNodo + "<f"+str(secc)+"> " + "|" + infoNodo + "|"
            secc+=1
        else: 
            textoNodo = textoNodo + "<f"+str(secc)+"> " + "|" + infoNodo + "|" + "<f" + str(secc+1)+ ">"

    g.node(tag,nohtml(textoNodo))    

    for i in arbolB.lista:
                
        

        if i.hijoIzq != None:
            #CAMINO SI EL NODO ACTUAL TIENE UN HIJO IZQUIERDO     
            union = ":f" + str(pos)  
            numeracion+=1                 
            g.edge(tag+union,graficar_arbol_b_recursivo(i.hijoIzq,g,numeracion))
            
        
        #CAMINO SI ES EL ULTIMO NODO EN LA LISTA (SE TERMINA CON EL NODO DERECHO)
        if i.hijoDer != None and pos+1 == len(arbolB.lista):
            union = ":f" + str(pos+1)
            numeracion+=1                 
            g.edge(tag+union,graficar_arbol_b_recursivo(i.hijoDer,g,numeracion))                                                     

        
                                    
        pos+=1
    return tag

def graficar_arbol_b(arbolB:arbolB, contador):
    g = graphviz.Digraph('G', filename='Graficas/arbolB' + str(contador) + '.gv', format='svg'
                        , node_attr={'shape':'record', 'height': '.1'})    
    
    g.attr(nodesep="0.5")
    g.attr(compound="true")
    g.edge_attr['dir'] = 'both'                                                    

    graficar_arbol_b_recursivo(arbolB.raiz,g, 0)
    
    g.view()

def graficar_matriz_dispersa(matriz:matrizDispersa, contador):
    g = graphviz.Digraph('G', filename='Graficas/matriz' + str(contador) + '.gv', format='svg')    
    
    g.attr(nodesep="0.5")
    g.attr("node", shape="box")
    g.edge_attr['dir'] = 'both'      
    #g.graph_attr['rankdir'] = 'LR'                                        
    

    aux = matriz.raiz        

    while aux.abajo != None:
        aux = aux.abajo

    #CREACION DE LOS NODOS    
    while aux != None:
        aux2 = aux
        
        while aux2 != None:
            g.node("nodo-"+str(aux2.posicion[0])+"-"+str(aux2.posicion[1])
                    ,label=str(aux2.tag),group=str(aux2.posicion[1]))            
            aux2 = aux2.der

        aux = aux.arriba
        
    #CREACION DE LAS FLECHAS HORIZONTALES    

    aux = matriz.raiz    

    while aux != None:
        aux2 = aux
        
        while aux2.der != None:
            with g.subgraph() as s:
                s.attr(rank='same')
                s.edge("nodo-"+str(aux2.posicion[0])+"-"+str(aux2.posicion[1])
                ,"nodo-"+str(aux2.der.posicion[0])+"-"+str(aux2.der.posicion[1])
                ,tailport="e", headport="w")            
                aux2 = aux2.der
        
        aux = aux.abajo

    #CREACION DE LAS FLECHAS VERTICALES
    aux = matriz.raiz    

    while aux != None:
        aux2 = aux
        
        while aux2.abajo != None:
            g.edge("nodo-"+str(aux2.posicion[0])+"-"+str(aux2.posicion[1])
            ,"nodo-"+str(aux2.abajo.posicion[0])+"-"+str(aux2.abajo.posicion[1])
            ,tailport="s", headport="n")            
            aux2 = aux2.abajo        
        aux = aux.der

    g.view()