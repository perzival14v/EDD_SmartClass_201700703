#ifndef TAREAS_H
#define TAREAS_H
#include <iostream>
#include <string.h>
#include <string>
#include <stdlib.h>

using namespace std;

class tareas
{
	public:				
		int idT;
		string carnet;
		string nombreTarea;
		string descripcion;
		string materia;
		string fecha;
		string hora;
		string estado;		
		
		tareas();
		tareas(int _idT,string _carnet, string _nombreTarea, string _descripcion, string _materia, string _fecha, string _hora, string _estado);
		
	protected:
};


int[] coordenadas(int contador,string linea){
	
};

#endif
