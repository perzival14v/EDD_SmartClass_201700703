from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, response
from Graficar.graficar import *
from Fase2.CargaArchivos.CargaMasiva import *
from Fase2.Estructuras.ArbolAVL import *
import json


@csrf_exempt
def prueba(request):    
    if request.method=="POST":        
        instrucciones_json = json.loads(request.body)
        if "tipo" in instrucciones_json[0].keys():
            if str.lower(instrucciones_json[0].get("tipo")) == "estudiante":
                cargaMasivaEstudiantes(instrucciones_json[0].get("path"))
            elif str.lower(instrucciones_json[0].get("tipo")) == "curso":
                print("curso")
        else:
            print("BUENAAAAS")


    return HttpResponse("Buenas")

