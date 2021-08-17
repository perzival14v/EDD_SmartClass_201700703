#include "tareas.h"
#include <iostream>
#include <string.h>
#include <string>
#include <stdlib.h>

using namespace std;



tareas::tareas()
{
}

tareas::tareas(int _idT,string _carnet, string _nombreTarea, string _descripcion, string _materia, string _fecha, string _hora, string _estado){
	idT=_idT;
	carnet=_carnet;
	nombreTarea=_nombreTarea;
	descripcion=_descripcion;
	materia=_materia;
	fecha=_fecha;
	hora=_hora;
	estado=_estado;
}
