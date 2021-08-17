#include <iostream>
#include <conio.h>
#include <string.h>
#include <string>
#include <Windows.h>
#include <cstdio>
#include <fstream>
#include <stdlib.h>


using namespace std;


/*DIFERENTES TIPOS DE NODO*/
struct nodoPila{	
	nodoPila *siguiente;
};


struct nodoLDC{	
	nodoLDC *siguiente;
	nodoLDC *anterior;
	estudiantes info;
};
	
/*OPERACIONES PARA ESTRUCTURAS DE PILA*/

/*
 encolar(nodoPila *&cabeza //Agregar el tipo de dato){
	nodoPila *nuevoNodo = new nodoPila();
	nuevoNodo->info=p1; //Agregar el tipo de dato
	nuevoNodo->siguiente = cabeza;
	cabeza = nuevoNodo;
};


 desEncolar(nodoPila *&pila){
			
	nodoPila *aux= pila;
	pa = aux->info;
	pila = aux->siguiente;
	delete aux;
};
*/

void recorrerPila(nodoPila *&pila){
	nodoPila *aux= pila;
	while(aux!=NULL){
								
		aux = aux->siguiente;
	}		 
}


/*OPERACIONES PARA ESTRUCTURA DE LISTA DOBLEMENTE ENLAZADA CIRCULAR*/


void agregarLDC(nodoLDC *&punteroCabeza, estudiantes e1){
	
	
	nodoLDC *aux = punteroCabeza;
	nodoLDC *nuevoNodo = new nodoLDC();
	/*Primer nodo agregado a la lista*/
	
	if(punteroCabeza==NULL){
		punteroCabeza = nuevoNodo;
		nuevoNodo->siguiente = punteroCabeza;
		nuevoNodo->anterior=nuevoNodo;
		nuevoNodo->info=e1;		
	}else{
		
		nuevoNodo->info=e1;
		
		while(aux->siguiente!=punteroCabeza)	{
			aux = aux->siguiente;	
		};
		
		aux->siguiente = nuevoNodo;
		nuevoNodo->anterior =aux;
		nuevoNodo->siguiente = punteroCabeza;
		
	};						
			
}

void recorrerLDC(nodoLDC *&cabeza){
	
	nodoLDC *aux = cabeza;
	
	if(cabeza!=NULL){
		cout << cabeza->info.nombre	<<endl;
	}
	
	while(aux->siguiente!=cabeza)	{						
		aux = aux->siguiente;	
		cout << aux->info.nombre	<<endl;
	};
};



