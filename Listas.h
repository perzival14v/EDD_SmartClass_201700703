#ifndef LISTAS_H
#define LISTAS_H
#include "estudiantes.h"
#include "tareas.h"
#include "errores.h"

class listas
{
	public:
		listas();
	protected:
};

struct nodoCola{	
	nodoCola *siguiente;
	errores info;
};

struct nodoLDC{	
	nodoLDC *siguiente;
	nodoLDC *anterior;
	estudiantes info;
};

struct nodoLD{
	nodoLD *siguiente;
	nodoLD *anterior;
	tareas info;
};


#endif
