#include <iostream>
#include <conio.h>
#include <string.h>
#include <string>
#include <Windows.h>
#include <cstdio>
#include <fstream>
#include <stdlib.h>

using namespace std;

class error{
	public:
		string tipo;
		string descripcion;
		error(string tipo, string descripcion);
};


/*1 significa error, 0 significa un DPI valido*/
int verificarDPI(string dpi){
	
	if(dpi.length()==16){
		return 0;
	}else{
		return 1;
	};
			
};


int verificarCarnet(string carnet){
	
	if(carnet.length()==9){
		return 0;
	}else{
		return 1;
	};
			
};



