from Fase2.Analizador_JSON.analisadorLexico import analizador
from Fase2.Objetos.Estudiantes import *
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

