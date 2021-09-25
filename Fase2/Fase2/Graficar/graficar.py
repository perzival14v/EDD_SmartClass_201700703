from Fase2.Estructuras.NodoLD import nodoLD
from Fase2.Estructuras.NodoArbolAVL import nodoArbol
from typing import Type
import graphviz


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