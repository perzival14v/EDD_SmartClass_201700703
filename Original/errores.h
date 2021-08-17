#include <iostream>
#include <conio.h>
#include <string.h>
#include <string>
#include <Windows.h>
#include <cstdio>
#include <fstream>
#include <stdlib.h>

class error{
	public:
		string tipo;
		string descripcion;
		error(string tipo, string descripcion);
};

error::error(string _tipo,string _descripcion){
	
	tipo=_tipo;
	descripcion=_descripcion;
	
};
