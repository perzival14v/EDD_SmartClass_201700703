#include <iostream>
#include <conio.h>
#include <string.h>
#include <string>
#include <Windows.h>
#include <cstdio>
#include <fstream>
#include <stdlib.h>
#include "estudiante.h"

/*DIFERENTES TIPOS DE NODO*/
struct nodoPila{	
	nodo *siguiente;
};


struct nodoLDC{	
	nodo *siguiente;
	nodo *anterior;
	estudiante info = estudiante(0,0,"","","","",0,0);
};
	
/*OPERACIONES PARA ESTRUCTURAS DE PILA*/
void encolar(nodoPila *&cabeza /*Agregar el tipo de dato*/){
	nodo *nuevoNodo = new nodoPila();
	nuevoNodo->info=p1; /*Agregar el tipo de dato*/
	nuevoNodo->siguiente = cabeza;
	cabeza = nuevoNodo;
};


void desEncolar(nodoPila *&pila){
			
	nodoPila *aux= pila;
	pa = aux->info;
	pila = aux->siguiente;
	delete aux;
};


void recorrerPila(nodoPila *&pila){
	nodoPila *aux= pila;
	while(aux!=NULL){
		
		
		
		cout << aux->info.Nombre <<" "<<aux->info.Edad << endl;
		aux = aux->siguiente;
	}		 
}


/*OPERACIONES PARA ESTRUCTURA DE LISTA DOBLEMENTE ENLAZADA CIRCULAR*/


void agregarLDC(nodoLDC *&cabeza, estudiante e1){
	
	
	nodoLDC *aux = cabeza;
	nodoLDC *nuevoNodo = new nodoLDC();
	/*Primer nodo agregado a la lista*/
	
	if(cabeza==NULL){
		cabeza->siguiente = cabeza;
		cabeza->anterior=cabeza;
		cabeza->info=e1;		
	}else{
		
		nuevoNodo->info=e1;
		
		while(aux->siguiente!=cabeza)	{
			aux = aux->siguiente;	
		};
		
		aux->siguiente = nuevoNodo;
		nuevoNodo->anterior =aux;
		nuevoNodo->siguiente = cabeza;
		
	};						
	
	
	
}




