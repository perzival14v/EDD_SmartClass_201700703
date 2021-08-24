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


void busquedaTarea(nodoLD *&cabeza,int direccion1, int direccion2, int direccion3);
void agregarLDC(nodoLDC *&punteroCabeza, estudiantes e1);
void recorrerLDC(nodoLDC *&cabeza);

void agregarLD(nodoLD *&punteroCabeza, tareas t1);
void recorrerLD(nodoLD *&cabeza);

void columnMajor(nodoLD *&cabeza ,tareas matriz[][30][9]);

void encolar(nodoCola *&cabeza,errores e1);
void recorrerCola(nodoCola *&cola);

int verificarAsignacionCarnet(string carnet, nodoLDC *&cabeza);
int verificarFecha(string fecha);
int verificarCorreo(string correo);


void modificarEstudiante(nodoLDC *&cabeza,string dato,int opcion);
void eliminarEstudiante(nodoLDC *&cabeza,string dpi);

int agregarTareaNueva(nodoLD *&cabeza,tareas nueva,int mes, int dia,int id);
void modificarTarea(nodoLD *&cabeza,int indice,int opcion);
void eliminarTarea(nodoLD *&cabeza,int indice);


#endif
