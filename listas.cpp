#include "listas.h"
#include <iostream>
#include <conio.h>
#include <string.h>
#include <string>
#include <cstdio>
#include <stdlib.h>
#include "estudiantes.h"
#include "tareas.h"
#include "errores.h"

using namespace std;

/*DIFERENTES TIPOS DE NODO*/


/*OPERACIONES PARA ESTRUCTURAS DE COLA*/


void encolar(nodoCola *&cabeza, errores e1){
	nodoCola *nuevoNodo = new nodoCola();
	nuevoNodo->info=e1; 
	nuevoNodo->siguiente = cabeza;
	cabeza = nuevoNodo;
	
	return;
}


void desEncolar(nodoCola *&cola){
	nodoCola *aux= cola;
	nodoCola *eliminar;
	
	while(aux->siguiente->siguiente!=NULL){
		aux = aux->siguiente;
		
	};					
	eliminar = aux->siguiente->siguiente;
	aux->siguiente = NULL;
	delete eliminar;
}


void recorrerCola(nodoCola *&cola){
	nodoCola *aux= cola;
	if(aux==NULL){
		cout << "No hay errores en la cola" << endl;	
	};
	
	while(aux!=NULL){
		cout << aux->info.id << endl;
		cout << aux->info.tipo << endl;
		cout << aux->info.descripcion << endl;
		cout << "---------------------------------" << endl;
		aux = aux->siguiente;
	};	
	
	return;
		 
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
}

void agregarLD(nodoLD *&punteroCabeza, tareas t1){
	nodoLD *aux = punteroCabeza;
	nodoLD *nuevoNodo = new nodoLD();
	/*Primer nodo agregado a la lista*/
	
	if(punteroCabeza==NULL){
		punteroCabeza = nuevoNodo;
		nuevoNodo->siguiente = NULL;		
		nuevoNodo->info=t1;		
	}else{
		
		nuevoNodo->info=t1;
		
		while(aux->siguiente!=NULL)	{
			aux = aux->siguiente;	
		};
		
		aux->siguiente = nuevoNodo;
		nuevoNodo->anterior =aux;
		nuevoNodo->siguiente = NULL;
		
	};
}

void recorrerLD(nodoLD *&cabeza){
	
	nodoLD *aux = cabeza;		
	
	while(aux!=NULL){	
		if(aux->info.carnet!="vacio"){									
			cout <<"\n"<<	aux->info.carnet <<endl;
			cout << aux->info.nombreTarea <<endl;
			cout << aux->info.descripcion <<endl;
			cout << aux->info.materia <<endl;
			cout << aux->info.fecha <<endl;
			cout << aux->info.estado <<endl;							
			aux = aux->siguiente;			
		};
	};
	
	
}

void columnMajor(nodoLD *&cabeza ,tareas matriz[5][30][9]){
	for(int i=0;i<5;i++){
		for(int j=0;j<9;j++){
			for(int k=0;k<30;k++){												
					agregarLD(cabeza,matriz[i][k][j]);																																		
			};
		};
	};	
}



/*-----------------------------------ANALISIS DE ERRORES--------------------------------------*/
/*1 significa error, 0 significa un DPI valido*/
int verificarDPI(string dpi){
	
	if(dpi.length()==13){
		return 0;
	}else{
		return 1;
	};
			
}


int verificarCarnet(string carnet){
	
	if(carnet.length()==9){
		return 0;
	}else{
		return 1;
	};
			
}


int verificarCorreo(string correo){
	
	int arroba=0;
	int punto=0;
	int otro=0;
	
	string dominioS="";
	
	for(int i=0;i<correo.length();i++){
		if(correo[i]=='@'){
			arroba=1;
		};
		
		if((correo[i]=='.') && (  (correo.length()-i-1==3) || (correo.length()-i-1==2) )){
						
			for(int j=i;j<correo.length();j++){
				dominioS=dominioS+correo[j];
			};
																			
			if(dominioS==".com"){
				punto=1;
				otro=1;	
			};
					
			if(dominioS==".es"){
				punto=1;
				otro=1;	
			};
					
			if(dominioS==".org"){
				punto=1;
				otro=1;	
			};												
		};
	};
	
	if(arroba==0){
		return 1;
	};
	
	if(punto==0){
		return 1;
	};
	
	if(otro==0){
		return 1;
	};
	
	return 0;
}


int verificarAsignacionCarnet(string carnet, nodoLDC *&cabeza){
	nodoLDC *aux = cabeza;		
	
	while(aux->siguiente!=cabeza){						
	
		if(aux->info.carnet==carnet){									
			
			
			return 0;			
		};
		
		aux = aux->siguiente;
	};
	
	return 1;
	
}


int verificarFecha(string fecha){
	int contadorBarra=0;	
	
	string palabra;
	
	for(int i=0;i<fecha.length();i++){
		
		if(fecha[i]=='/'){
			contadorBarra++;
			
			switch(contadorBarra){
				case 1:{
					if(palabra.length()!=4){
						return 1;
					};
					break;
				};
				case 2:{
					if(palabra.length()!=2){
						return 1;
					};
					break;
				};	
			};
			palabra="";
			
		}else{
			palabra = palabra + fecha[i];	
		}
		
	}
	
	if(palabra.length()!=2){
		return 1;
	}
	
	return 0;
	
}


listas::listas()
{
}
