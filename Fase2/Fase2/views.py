from Fase2.Estructuras.NodoArbolB import nodoArbolB
from Fase2.Estructuras.ArbolB import arbolB
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, response
from Fase2.Graficar.graficar import *
from Fase2.CargaArchivos.CargaMasiva import *
from Fase2.Estructuras.ArbolAVL import *
import json,gc

arbolEstudiantes = arbolAVL()
arbol_cursos_pensum = arbolB(3)



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
        arbol_cursos_pensum.agregar(nodoArbolB(100,"nodo1"))
        arbol_cursos_pensum.agregar(nodoArbolB(90,"nodo2"))
        arbol_cursos_pensum.agregar(nodoArbolB(40,"nodo3"))
        arbol_cursos_pensum.agregar(nodoArbolB(30,"nodo4"))
        arbol_cursos_pensum.agregar(nodoArbolB(20,"nodo5"))        
        arbol_cursos_pensum.agregar(nodoArbolB(200,"nodo6"))        
        arbol_cursos_pensum.agregar(nodoArbolB(300,"nodo7"))
        #HASTA EL 300 VA BIEN
        arbol_cursos_pensum.agregar(nodoArbolB(400,"nodo8"))
        

        arbol_cursos_pensum.agregar(nodoArbolB(500,"nodo9"))
        arbol_cursos_pensum.agregar(nodoArbolB(600,"nodo10"))
        arbol_cursos_pensum.agregar(nodoArbolB(700,"nodo11"))
        arbol_cursos_pensum.agregar(nodoArbolB(800,"nodo12"))
        arbol_cursos_pensum.agregar(nodoArbolB(900,"nodo13"))
        graficar_arbol_b(arbol_cursos_pensum,0)
        arbol_cursos_pensum.agregar(nodoArbolB(1000,"nodo14"))
        graficar_arbol_b(arbol_cursos_pensum,1)

        print("Prueba de arbol")


    return HttpResponse("Buenas")