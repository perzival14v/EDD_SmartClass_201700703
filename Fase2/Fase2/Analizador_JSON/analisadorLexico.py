from typing import IO
from Fase2.Estructuras.ListaDoble import listaDoble
from Fase2.Objetos.estudiante import *
from Fase2.Estructuras.ArbolAVL import *
import re, copy

from Fase2.Objetos.tareas import Tarea


def analizador(archivo,arbol:arbolAVL):

    separador=0
    est=None
    tar=None

    for line in archivo:
        if re.search("user",str.lower(line))!= None:
            separador=0
            est = Estudiantes()
            

        if re.search("task",str.lower(line))!= None:
            separador=1
            tar = Tarea()
                       

        if separador==0 and re.search("\$element",line)==None:
            if re.search("carnet",str.lower(line)):
                est.carnet=re.sub("\"","",re.search("\".*\"",line).group(0))                
            if re.search("dpi",str.lower(line)):
                est.dpi=re.sub("\"","",re.search("\".*\"",line).group(0))
            if re.search("nombre",str.lower(line)):
                est.nombre=re.sub("\"","",re.search("\".*\"",line).group(0))
            if re.search("carrera",str.lower(line)):
                est.carrera=re.sub("\"","",re.search("\".*\"",line).group(0))
            if re.search("password",str.lower(line)):
                est.password=re.sub("\"","",re.search("\".*\"",line).group(0))
            if re.search("creditos",str.lower(line)):
                est.creditos="".join(re.findall("\d",line))
            if re.search("edad",str.lower(line)):
                est.edad="".join(re.findall("\d",line))
        elif separador==1 and re.search("\$element",line)==None:
            if re.search("carnet",str.lower(line)):
                tar.carnet=re.sub("\"","",re.search("\".*\"",line).group(0))                
            if re.search("nombre",str.lower(line)):
                tar.nombre=re.sub("\"","",re.search("\".*\"",line).group(0))
            if re.search("descripcion",str.lower(line)):
                tar.descripcion=re.sub("\"","",re.search("\".*\"",line).group(0))
            if re.search("materia",str.lower(line)):
                tar.materia=re.sub("\"","",re.search("\".*\"",line).group(0))
            if re.search("fecha",str.lower(line)):

                fecha=re.sub("\"","",re.search("\".*\"",line).group(0))
                separacion = re.split("/",fecha)
                tar.dia=separacion[0]
                tar.mes=separacion[1]
                tar.anio=separacion[2]


            if re.search("hora",str.lower(line)):
                hora=re.sub("\"","",re.search("\".*\"",line).group(0))
                separacion = re.split(":",hora)
                tar.hora=separacion[0]

            if re.search("estado",str.lower(line)):
                tar.estado=re.sub("\"","",re.search("\".*\"",line).group(0))
        
        if re.search("\$element",line)!=None and separador==0 and re.search("user",str.lower(line))== None:
            arbol.agregar(copy.deepcopy(int(est.carnet)),copy.deepcopy(est))
            est=None
        elif re.search("\$element",line)!=None and separador==1 and re.search("task",str.lower(line))== None:
            estudiante = buscar_dentro_AVL(arbol.raiz,int(tar.carnet))

            if estudiante == None:
                print("Estudiante no existe no se agrega tarea")
            else:
                if estudiante.yearList == None:
                    estudiante.yearList = listaDoble()
                
                buscar_y_agregar_tarea(estudiante.yearList , copy.copy(int(tar.anio))
                                        ,copy.copy(int(tar.mes)),copy.copy(int(tar.dia))
                                        ,copy.copy(int(tar.hora)),copy.deepcopy(tar))                
            tar=None
        