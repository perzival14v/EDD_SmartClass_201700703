#include "tareas.h"
#include <iostream>
#include <string.h>
#include <string>
#include <stdlib.h>

using namespace std;



tareas::tareas()
{
	idT=-1;
	carnet="vacio";
	nombreTarea="Calificacion";
	descripcion="vacio";
	materia="vacio";
	fecha="vacio";
	hora=-1;
	estado="vacio";
	
	
}

tareas::tareas(int _idT,string _carnet, string _nombreTarea, string _descripcion, string _materia, string _fecha, int _hora, string _estado){
	idT=_idT;
	carnet=_carnet;
	nombreTarea=_nombreTarea;
	descripcion=_descripcion;
	materia=_materia;
	fecha=_fecha;
	hora=_hora;
	estado=_estado;
}


void mostrarDatos(tareas matriz[][30][9]){
	for(int i=0;i<5;i++){
		for(int j=0;j<30;j++){
			for(int k=0;k<9;k++){
				if(matriz[i][j][k].carnet!="vacio"){								
					cout <<"\n"<< matriz[i][j][k].carnet <<endl;
					cout << matriz[i][j][k].nombreTarea <<endl;
					cout << matriz[i][j][k].descripcion <<endl;
					cout << matriz[i][j][k].materia <<endl;
					cout << matriz[i][j][k].fecha <<endl;
					cout << matriz[i][j][k].estado <<endl;						
				};
			};
		};
	};
}
