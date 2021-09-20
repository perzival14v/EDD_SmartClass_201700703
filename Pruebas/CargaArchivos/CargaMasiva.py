from Fase2.Analizador_JSON.analisadorLexico import analizador
from Fase2.Objetos.Estudiantes import *
from Fase2.Analizador_JSON import *

import json

def cargaMasivaEstudiantes(path,arbol):

    analizador(open(path,"r").read(),arbol)
    
    