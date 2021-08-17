#include "estudiantes.h"
#include <iostream>
using namespace std;

estudiantes::estudiantes(){
	carnet=1;
	dpi=1;
	nombre="vacio";
	carrera="vacio";
	correo="vacio";
	contrasenia="vacio";
	creditos=1;
	edad=1;
};


estudiantes::estudiantes(string _carnet, string _dpi, string _nombre, string _carrera, string _correo, string _contrasenia, string _creditos, string _edad){
	carnet=_carnet;
	dpi=_dpi;
	nombre=_nombre;
	carrera=_carrera;
	correo=_correo;
	contrasenia=_contrasenia;
	creditos=_creditos;
	edad=_edad;
};





