from typing import IO
from Fase2.Objetos.Estudiantes import *
from Fase2.Estructuras.ArbolAVL import *
import re, copy


def analizador(archivo,arbol:arbolAVL):

    separador=0

    for line in archivo:
        if re.search("user",str.lower(line))!= None:
            separador=0
            est = estudiante()

        if re.search("task",str.lower(line))!= None:
            separador=1

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
                est.creditos=re.sub("\"","",re.search("\".*\"",line).group(0))
            if re.search("edad",str.lower(line)):
                est.edad=re.sub("\"","",re.search("\".*\"",line).group(0))
        elif separador==1 and re.search("\$element",line)==None:
            print()
        
        if re.search("\$element",line)!=None:
            arbol.agregar(copy.deepcopy(est.carnet),copy.deepcopy(est))
            est=None
            
        