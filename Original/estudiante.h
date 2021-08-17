#include <iostream>
#include <conio.h>
#include <string.h>
#include <string>
#include <Windows.h>
#include <cstdio>
#include <fstream>
#include <stdlib.h>

class estudiante{
	public:
		int carnet;
		int dpi;
		string nombre;
		string carrera;
		string correo;
		string contraseña;
		int creditos;
		int edad;
		
		estudiante(int carnet, int dpi, string nombre, string carrera, string correo, string contraseña, int creditos, int edad);	
};

estudiante::estudiante(int _carnet, int _dpi, string _nombre, string _carrera, string _correo, string _contraseña, int _creditos, int _edad){
	carnet=_carnet;
	dpi=_dpi;
	nombre=_nombre;
	carrera=_carrera;
	correo=_correo;
	contraseña=_contraseña;
	creditos=_creditos;
	edad=_edad;
};
