from Fase2.Estructuras.NodoLD import nodoLD
from Fase2.Estructuras.NodoArbol import nodoArbol
from typing import Type
import graphviz


def graficarArbolAVLrecursivo(nodo:nodoArbol, g):
    if nodo != None:
        if nodo.izq != None:
            g.edge(str(nodo.indice),str(nodo.izq.indice))
            graficarArbolAVLrecursivo(nodo.izq, g)
        
        if nodo.der != None:  
            g.edge(str(nodo.indice),str(nodo.der.indice))
            graficarArbolAVLrecursivo(nodo.der, g)
    else:
        return

def graficarArbolAVL(nodo:nodoArbol, contador):
    g = graphviz.Graph('G', filename='Graficas/arbolAVL' + str(contador) + '.gv', format='svg')

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