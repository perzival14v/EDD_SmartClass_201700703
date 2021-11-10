import re
from Fase2.Analizador_JSON.analisadorLexico import analizador
from Fase2.Estructuras import ArbolAVL, ListaDoble, nodo_hash
from Fase2.Estructuras.ArbolAVL import *
from Fase2.Estructuras.ArbolB import arbolB
from Fase2.Estructuras.tabla_hash import tablaHash
from Fase2.Estructuras.nodo_hash import nodoHash
from Fase2.Objetos import apunte
from Fase2.Objetos.apunte import Apunte
from Fase2.Objetos import curso
from Fase2.Objetos.estudiante import *
from Fase2.Objetos.curso import *
from Fase2.Analizador_JSON import *
from Fase2.Estructuras.NodoArbolB import *
import json

def cargaMasivaEstudiantes(path,arbol):
    analizador(open(path,"r"),arbol)
    
    
def cargaMasicaCursosPensum(path,arbol):    
    archivo = json.loads(open(path,"r",encoding="utf-8").read())

    for i in archivo.get("Cursos"):
        curso_nuevo = Curso()
        curso_nuevo.codigo = i.get("Codigo")
        curso_nuevo.nombre = i.get("Nombre") 
        curso_nuevo.creditos = i.get("Creditos")
        curso_nuevo.pre_requisitos = i.get("Prerequisitos")
        curso_nuevo.obligatorio = i.get("Obligatorio")    

        nodo = nodoArbolB(int(curso_nuevo.codigo),curso_nuevo)
        arbol.agregar(nodo)


def cargaMasivaCursos(path,arbol:arbolAVL()):
    archivo = json.loads(open(path,"r",encoding="utf-8").read())

    datos = archivo.get("Estudiantes")

    for i in datos:
        carnet = i.get("Carnet")
        lista_anios = i.get("Años")

        est = buscar_dentro_AVL(arbol.raiz,int(carnet))

        if est != None:            
            for j in lista_anios:
                anio = j.get("Año")

                if est.yearList == None:
                    aux = listaDoble()
                    aux.agregar(int(anio))
                    est.yearList = aux

                nodo_anio = est.yearList.buscar(int(anio))

                if nodo_anio == None:
                    est.yearList.agregar(int(anio))
                    nodo_anio = est.yearList.buscar(int(anio))

                lista_semestres = j.get("Semestres")
                for k in lista_semestres:
                    semestre = k.get("Semestre")
                    lista_cursos = k.get("Cursos")

                    if nodo_anio.conexion1 == None:
                        aux = listaDoble()
                        aux.agregar(int(semestre))
                        nodo_anio.conexion1 = aux

                    nodo_semestre = nodo_anio.conexion1.buscar(int(semestre))

                    if nodo_semestre == None:
                        nodo_anio.conexion1.agregar(int(semestre))                
                        nodo_semestre = nodo_anio.conexion1.buscar(int(semestre))

                    for l in lista_cursos:
                        
                        cur = Curso()

                        cur.codigo = l.get("Codigo")
                        cur.nombre = l.get("Nombre")
                        cur.creditos = l.get("Creditos")
                        cur.pre_requisitos = l.get("Prerequisitos")
                        cur.obligatorio = l.get("Obligatorio")

                        nodo_arb_b = nodoArbolB(cur.codigo,cur)
                        
                        

                        if nodo_semestre.conexion1 == None:
                            nodo_semestre.conexion1 = arbolB(5)


                        nodo_semestre.conexion1.agregar(nodo_arb_b)
        else:
            print("Estudiante " + carnet +" no existe, se salta la informacion")


def cargaMasivaApuntes(path,tabla_hash):
    archivo = json.loads(open(path,"r",encoding="utf-8").read())

    datos = archivo.get("usuarios")

    for i in datos:
        carnet = i.get("carnet")
        apuntes = i.get("apuntes")
        for j in apuntes:
            titulo = j.get("titulo")
            contenido=j.get("contenido")

            #Creacion del nodo
            nodo = nodoHash()
            nodo.llave = int(carnet)        

            #Creacion del apunte
            anotacion = Apunte(titulo,contenido)

            #Agregar a la tabla hash
            tabla_hash.agregar(nodo,anotacion)
