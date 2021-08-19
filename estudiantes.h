#ifndef ESTUDIANTES_H
#define ESTUDIANTES_H

#include <iostream>
#include <string.h>
#include <string>
#include <stdlib.h>

using namespace std;


class estudiantes
{
	public:
		string carnet;
		string dpi;
		string nombre;
		string carrera;
		string correo;
		string contrasenia;
		string creditos;
		string edad;
		estudiantes();
		estudiantes(string carnet, string dpi, string nombre, string carrera, string correo, string contrasenia, string creditos, string edad);
	protected:
};

#endif
