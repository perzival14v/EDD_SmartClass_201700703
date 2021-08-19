#ifndef ERRORES_H
#define ERRORES_H

#include<iostream>
#include<cstring>
#include<conio.h>
#include<string.h>
#include<string>
#include<cstdio>

using namespace std;

class errores{
	public:
		int id;
		string tipo;
		string descripcion;
		errores();
		errores(int id,string tipo, string descripcion);
};

#endif
