from Estructuras.ListaDoble import listaDoble
from Estructuras.NodoLD import nodoLD
from Estructuras.ArbolAVL import arbolAVL
from Objetos.Estudiantes import estudiante

from graficar import *


e1 = estudiante()

estudiantes = arbolAVL()
estudiantes.agregar(10, e1)
estudiantes.agregar(5 , e1)
estudiantes.agregar(15, e1)
estudiantes.agregar(12, e1)
estudiantes.agregar(20, e1)
graficarArbolAVL(estudiantes.raiz,0)
estudiantes.agregar(11, e1)
graficarArbolAVL(estudiantes.raiz,1)


lista = listaDoble()
lista.agregar(nodoLD.getNewNodo(5))
lista.agregar(nodoLD.getNewNodo(6))
lista.agregar(nodoLD.getNewNodo(8))
lista.agregar(nodoLD.getNewNodo(9))
lista.agregar(nodoLD.getNewNodo(0))

graficarLD(lista.cabeza,0)