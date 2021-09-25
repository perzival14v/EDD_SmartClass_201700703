from Fase2.Estructuras.ArbolB import arbolB
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, response
from Fase2.Graficar.graficar import *
from Fase2.CargaArchivos.CargaMasiva import *
from Fase2.Estructuras.ArbolAVL import *
import json

arbolEstudiantes = arbolAVL()
arbol_cursos_pensum = arbolB(5)


@csrf_exempt
def estudiantes(request):    
    if request.method=="POST":        
        instrucciones_json = json.loads(request.body)
        if "tipo" in instrucciones_json[0].keys():
            if str.lower(instrucciones_json[0].get("tipo")) == "estudiante":
                arbolEstudiantes=arbolAVL()
                cargaMasivaEstudiantes(instrucciones_json[0].get("path"), arbolEstudiantes)                
            elif str.lower(instrucciones_json[0].get("tipo")) == "curso":
                print("curso")
        else:
            print("BUENAAAAS")


    return HttpResponse("Buenas")
    
@csrf_exempt
def cursosEstudiantes(request):    
    if request.method=="POST":        
        instrucciones_json = json.loads(request.body)
        arbol_cursos_pensum.agregar(8)
        arbol_cursos_pensum.agregar(10)
        arbol_cursos_pensum.agregar(12)
        arbol_cursos_pensum.agregar(14)
        arbol_cursos_pensum.agregar(16)
        print("Prueba de arbol")


    return HttpResponse("Buenas")