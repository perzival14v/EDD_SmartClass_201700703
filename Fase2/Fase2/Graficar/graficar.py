import re
from typing import List
from Fase2.CargaArchivos.CargaMasiva import cargaMasicaCursosPensum
from Fase2.Estructuras import nodo_hash
from Fase2.Estructuras.NodoLD import nodoLD
from Fase2.Estructuras.NodoArbolAVL import nodoArbol
from Fase2.Estructuras.ArbolB import arbolB
from Fase2.Estructuras.matriz_dispersa import matrizDispersa
import graphviz
from graphviz import nohtml

from Fase2.Objetos import estudiante, tareas


def graficarArbolAVLrecursivo(nodo:nodoArbol, g):
    if nodo != None:
        if nodo.izq != None:

            g.node(str(nodo.indice), label=str(str(nodo.indice)+"\n"+str(nodo.info.nombre)+"\n"+str(nodo.info.carrera)))
            g.node(str(nodo.izq.indice), label=str(str(nodo.izq.indice)+"\n"+str(nodo.izq.info.nombre)+"\n"+str(nodo.izq.info.carrera)))

            g.edge(str(nodo.indice),str(nodo.izq.indice),tailport="w", headport="n")
            graficarArbolAVLrecursivo(nodo.izq, g)
        
        if nodo.der != None:  

            g.node(str(nodo.indice), label=str(str(nodo.indice)+"\n"+str(nodo.info.nombre)+"\n"+str(nodo.info.carrera)))
            g.node(str(nodo.der.indice), label=str(str(nodo.der.indice)+"\n"+str(nodo.der.info.nombre)+"\n"+str(nodo.der.info.carrera)))

            g.edge(str(nodo.indice),str(nodo.der.indice),tailport="e", headport="n")
            graficarArbolAVLrecursivo(nodo.der, g)
    else:
        return

def graficarArbolAVL(nodo:nodoArbol, contador):
    g = graphviz.Digraph('G', filename='Graficas/arbolAVL' + str(contador) + '.gv', format='svg')
    g.attr("node", shape="box")
    #g.attr(splines="ortho")
    g.attr(nodesep="0.5")

    graficarArbolAVLrecursivo(nodo, g)        
    
    g.view()

def graficarLD(nodo:nodoLD, contador):

    g = graphviz.Digraph('G', filename='Graficas/listaDoble' + str(contador) + '.gv', format='svg')
    g.attr("node", shape="box")
    
    contador=0

    aux = nodo

    while aux != None:
        etiqueta = str(aux.info.carnet) + "\n" + "Nombre: " + str(aux.info.nombre)         + "\n" + "Descripcion: " + str(aux.info.descripcion) + "\n" + "Materia: " + str(aux.info.materia)    + "\n" + "Fecha: " + str(aux.info.dia) + "/" + str(aux.info.mes) + "/" + str(aux.info.anio)     + "\n" + "Hora: " + str(aux.info.hora) + "\n" + "Estado: " + str(aux.info.estado)
        g.node("nodo"+str(contador),etiqueta)
        contador+=1
        aux = aux.siguiente

    contador=1

    while nodo.siguiente != None:
        g.edge("nodo"+str(contador),"nodo"+str(contador+1))
        nodo = nodo.siguiente      
            
    g.graph_attr['rankdir'] = 'LR'
    g.edge_attr['dir'] = 'both'

    g.view()
#cr = contador recursivo
def graficar_arbol_b_recursivo(arbolB:arbolB, g, numeracion):
    #contador esta adelantado en una posicion para poder elegir el siguiente nodo de la lista    
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
            respuesta=graficar_arbol_b_recursivo(i.hijoIzq,g,numeracion)
            g.edge(tag+union,respuesta[0])
            numeracion = respuesta[1]
        
        #CAMINO SI ES EL ULTIMO NODO EN LA LISTA (SE TERMINA CON EL NODO DERECHO)
        if i.hijoDer != None and pos+1 == len(arbolB.lista):
            union = ":f" + str(pos+1)
            numeracion+=1 
            respuesta=graficar_arbol_b_recursivo(i.hijoDer,g,numeracion)      
            g.edge(tag+union,respuesta[0])
            numeracion = respuesta[1]                                                     

        
                                    
        pos+=1
    return [tag,numeracion]

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

def graficar_prerequisito_recursivo(curso,lista_cursos:List,g,lista_usados:List,cola:List):
    if curso not in lista_usados:        
        label = curso + " - " + lista_cursos[curso][1]
        g.node(curso,label=label)

        lista_usados.append(curso)
        cola.extend(lista_cursos[curso][3])

        for i in cola:
            graficar_prerequisito_recursivo(i,lista_cursos,g,lista_usados,[])
            g.edge(curso,i,label=lista_cursos[i][2],tailport="w", headport="e")    
        
    

    return lista_usados

def graficar_prerequisitos(curso,lista_cursos,contador):
    g = graphviz.Digraph('G', filename='Graficas/PreRequisito_'+str(curso) +"_"+ str(contador) + '.gv', format='svg')    
    
    g.attr(nodesep="0.5")
    g.attr("node", shape="box")    
    g.edge_attr['dir'] = 'back'          
    g.graph_attr['rankdir'] = 'RL'      
    if curso=="todos":        
        usados=[]
        suma = 0
        for i in lista_cursos:
            usados=graficar_prerequisito_recursivo(i,lista_cursos,g,usados,[])
            suma += int(lista_cursos[i][2])
        print(suma)
        
    else:
        graficar_prerequisito_recursivo(curso,lista_cursos,g,[],[])


    g.view()

def graficar_tabla_hash(tabla_hash, contador):
    g = graphviz.Digraph('G', filename='Graficas/TablaHash_'+ str(contador) + '.gv', 
                        format='svg',node_attr={'shape': 'plaintext'})            
    g.attr(nodesep="0.5")
    g.graph_attr['rankdir'] = 'LR' 

    tablaHTML = '''<
        <TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0" CELLPADDING="30">'''
    puerto = 0
    for i in tabla_hash:
        #Creacion de los nodos
        puerto+=1       

        if i[1].llave == None:
            carne = "<BR/>"
        else:
            carne = str(i[1].llave)

        tablaHTML += '''
        <TR>
            <TD PORT="f'''+str(puerto)+'''">''' + carne + '''</TD>
        </TR>'''

    tablaHTML+="""
    </TABLE>>"""    
    g.node('struct1',tablaHTML)
    g.attr("node", shape="ellipse")
    puerto = 0
    for i in tabla_hash:
        #Creacion de los nodos
        puerto+=1       

        if i[1].llave == None:
            continue
        else:
            aux = i[1].lista.cabeza
            cuenta = 0
            anterior = "struct1:f"+str(puerto)
            while aux != None:
                cuenta+=1
                nombre = "nodo_f" + str(puerto) + str(cuenta)
                g.node(nombre,label="apunte "+str(cuenta))
                g.edge(anterior,nombre)
                anterior = nombre
                aux = aux.siguiente
            

    

    g.view()

def graficar_apuntes_estudiante(tabla_hash,carne):

    g = graphviz.Digraph('G', filename='Graficas/apuntes_'+ str(carne) + '.gv', 
                        format='svg')            
    g.attr(nodesep="0.5")
    g.graph_attr['rankdir'] = 'LR'
    g.attr("node", shape="box") 

    for i in tabla_hash:
        if i[1].llave == int(carne):
            aux = i[1].lista.cabeza
            cuenta = 0
            anterior = "carne"
            g.node(anterior,label=carne)
            while aux != None:
                g.edge_attr['dir'] = 'both'
                cuenta+=1
                nombre = "nodo_" + str(cuenta)
                label = aux.info.titulo
                label+= "\n" + aux.info.apunte
                g.node(nombre,label=label)                
                g.edge(anterior,nombre)
                anterior = nombre
                aux = aux.siguiente


    g.view()





