#ifndef GRAPHVIZ_H
#define GRAPHVIZ_H

#include "listas.h"

class graphviz
{
	public:
		graphviz();
	protected:
};

void imprimirEstudiantes(nodoLDC *&cabeza,int indice);
void imprimirTareas(nodoLD *&cabeza,int indice);
void imprimirTareasFiltradas(nodoLD *&cabeza,int indice);
void imprimirCola(nodoCola *&cabeza,int indice);
#endif
