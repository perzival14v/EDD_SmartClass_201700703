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



/*------------------------------------BUSQUEDAS DENTRO DE LA LISTA---------------------------------------*/

void busquedaTarea(nodoLD *&cabeza,int mes, int dia, int hora){
	
	int posicion = (30*9*mes)+(30*hora)+dia;
	cout << posicion <<endl;
	nodoLD *aux = cabeza;
	
	if(aux!=NULL)	{
		
		while(posicion>0){
			aux=aux->siguiente;
			posicion--;
		}
		tareas tarea = aux->info;
		
		if(tarea.carnet!="vacio"){
			cout<<"\nCarnet:"<<tarea.carnet<<endl;
			cout<<"ID: " << tarea.idT <<endl;
			cout<<"Nombre: " << tarea.nombreTarea <<endl;
			cout<<"Descripcion: " << tarea.descripcion<<endl;
			cout<<"Materia: " << tarea.materia <<endl;
			cout<<"Fecha: " << tarea.fecha <<endl;
			cout<<"Hora: " << tarea.hora <<endl;
			cout<<"Estado: " << tarea.estado <<endl	;
		}else{
			cout << "\n Tarea no existe" <<endl;
		}
		
		
		
	}else{
		cout << "La lista esta vacia" <<endl;
	}
	
	
	
}

/*------------------------------------Agregacion/Modificacion/Eliminacion de datos USUARIO-------------------------------*/
void modificarEstudiante(nodoLDC *&cabeza,string dpi,int opcion){				
	
	nodoLDC *aux = cabeza;		
	
	while(aux->siguiente!=cabeza)	{			
		if(aux->info.dpi==dpi){
			break;
		}								
		aux = aux->siguiente;	
		
	};
	
	
	if(aux->info.dpi==dpi){
		string datoNuevo;
		switch(opcion){			
			case 1:{
				cout << "ingrese el nuevo carnet" << endl;
				cin >> datoNuevo;
				
				aux->info.carnet=datoNuevo;
				
				break;
			}
			
			case 2:{
				cout << "ingrese el nuevo DPI" << endl;
				cin >> datoNuevo;
				
				aux->info.dpi=datoNuevo;
				break;
			}
			
			case 3:{
				cout << "ingrese el nuevo nombre" << endl;
				cin >> datoNuevo;
				
				aux->info.nombre=datoNuevo;
				break;
			}
			
			case 4:{
				cout << "ingrese la nueva carrera" << endl;
				cin >> datoNuevo;
				
				aux->info.carrera=datoNuevo;
				
				
				break;
			}
			
			case 5:{
				cout << "ingrese la nueva contreseña" << endl;
				cin >> datoNuevo;
				
				aux->info.contrasenia=datoNuevo;
				
				
				break;
			}
			
			case 6:{
				
				cout << "ingrese la nueva cantidad de creditos" << endl;
				cin >> datoNuevo;
				
				aux->info.creditos=datoNuevo;
				
				break;
			}
			
			case 7:{
				
				cout << "ingrese la nueva edad" << endl;
				cin >> datoNuevo;
				
				aux->info.edad=datoNuevo;
				
				
				break;
			}
		};
		
		
		
	}else{
		cout << "Dato no encontrado" << endl;
	};
}

void eliminarEstudiante(nodoLDC *&cabeza,string dpi){
	nodoLDC *aux = cabeza;		
	
	while(aux->siguiente!=cabeza)	{			
		if(aux->info.dpi==dpi){
			int opcion;
			
			cout << "Estudiante Encontrado, ¿Desea eliminarlo?" <<endl;			
			cout << "1. Si" << endl;
			cout << "2. No" << endl;
			cin >> opcion;
			
			if(opcion==1){
				nodoLDC *eliminar;
				eliminar =aux;
				aux->anterior->siguiente = aux->siguiente;
				aux->siguiente->anterior = aux->anterior;
				
				delete eliminar;
			}
			
			
			return;
		}								
		aux = aux->siguiente;			
	};
	
	
	cout << "Dato no encontrado" << endl;	
}


/*------------------------------------Agregacion/Modificacion/Eliminacion de datos TAREAS-------------------------------*/

int agregarTareaNueva(nodoLD *&cabeza,tareas nueva,int mes, int dia,int id){
	nodoLD *aux = cabeza;		
	int contador=0;
	int indice = (30*9*(mes-7))+(30*(nueva.hora-8))+(dia-1);
	
	
	
	while(aux!=NULL){	
		if(contador==indice && aux->info.carnet=="vacio"){									
			aux->info.idT=id;
			aux->info.carnet=nueva.carnet;
			aux->info.nombreTarea=nueva.nombreTarea;
			aux->info.descripcion=nueva.descripcion;
			aux->info.materia=nueva.materia;
			aux->info.fecha=nueva.fecha;
			aux->info.hora=nueva.hora;
			aux->info.estado=nueva.estado;		
			
			return	0;
		};
		aux=aux->siguiente;
		contador++;
	};
	
	
	cout << "No se encontro el indice o la tarea ya existe";
	return 1;
}


void modificarTarea(nodoLD *&cabeza,int indice,int opcion){
	nodoLD *aux = cabeza;		
	int contador=0;
	
	
	while(aux!=NULL){	
		if(contador==indice && aux->info.carnet!="vacio"){									
			switch(opcion){			
			case 1:{
				cout << "ingrese el nuevo carnet" << endl;
				cin >> aux->info.carnet;
							
				
				break;
			}
			
			case 2:{
				cout << "ingrese el nuevo nombre de tarea" << endl;
				cin >> aux->info.nombreTarea;
							
				break;
			}
			
			case 3:{
				cout << "ingrese la nueva descripcion" << endl;
				cin >> aux->info.descripcion;
							
				break;
			}
			
			case 4:{
				cout << "ingrese la nueva materia" << endl;
				cin >> aux->info.materia;
								
				
				
				break;
			}
			
			case 5:{
				cout << "ingrese la nueva fecha" << endl;
				cin >> aux->info.fecha;
							
				
				
				break;
			}
					
			
			case 6:{
				
				cout << "ingrese el nuevo estado" << endl;
				cin >> aux->info.estado;
								
				
				
				break;
			}
		};		
			
			return	;
		};
		contador++;
		aux=aux->siguiente;
	};
	
	
	cout << "No se encontro el indice o la tarea no existe";
}


void eliminarTarea(nodoLD *&cabeza,int indice){
	nodoLD *aux = cabeza;		
	int contador=0;
	
	
	while(aux!=NULL){	
		if(contador==indice){									
			aux->info.idT=-1;
			aux->info.carnet="vacio";
			aux->info.nombreTarea="vacio";
			aux->info.descripcion="vacio";
			aux->info.materia="vacio";
			aux->info.fecha="vacio";
			aux->info.hora=-1;
			aux->info.estado="vacio";		
			
			return;
		};
		contador++;
		aux=aux->siguiente;		
	};
			
	cout << "No se encontro el indice";
	return;
}


listas::listas()
{
}
