from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, response
from Fase2.Estructuras.NodoArbolB import nodoArbolB
from Fase2.Estructuras.ArbolB import arbolB
from Fase2.Graficar.graficar import *
from Fase2.CargaArchivos.CargaMasiva import *
from Fase2.Estructuras.ArbolAVL import *
from Fase2.Estructuras.matriz_dispersa import *
import json,gc

arbolEstudiantes = arbolAVL()
arbol_cursos_pensum = arbolB(5)
matriz_prueba = matrizDispersa()


@csrf_exempt
def cargaMasiva(request):    
    if request.method=="POST":        
        instrucciones_json = json.loads(request.body)
        if "tipo" in instrucciones_json[0].keys():
            #Carga de estudiantes dentro del arbol AVL
            if str.lower(instrucciones_json[0].get("tipo")) == "estudiante":
                arbolEstudiantes=arbolAVL()
                cargaMasivaEstudiantes(instrucciones_json[0].get("path"), arbolEstudiantes)
            #Carga de cursos de pensum dentro de arbol B                
            elif str.lower(instrucciones_json[0].get("tipo")) == "cursos_pensum":
                cargaMasicaCursosPensum(instrucciones_json[0].get("path"), arbol_cursos_pensum)
                graficar_arbol_b(arbol_cursos_pensum,0)
            elif str.lower(instrucciones_json[0].get("tipo")) == "curso":
                print()
                
        else:
            print("BUENAAAAS")


    return HttpResponse("Buenas")
    
@csrf_exempt
def pruebas(request):    
    if request.method=="POST":        
        #instrucciones_json = json.loads(request.body)
        matriz_prueba.agregar(1,1,1)
        matriz_prueba.agregar(1,1,122)
        matriz_prueba.agregar(1,1,133)
        matriz_prueba.agregar(1,3,2)
        matriz_prueba.agregar(1,2,3)
        matriz_prueba.agregar(2,8,4)
        matriz_prueba.agregar(3,4,5)
        matriz_prueba.agregar(7,3,6)
        graficar_matriz_dispersa(matriz_prueba,0)

    return HttpResponse("Buenas")