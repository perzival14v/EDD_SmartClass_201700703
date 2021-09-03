#include "graphviz.h"
#include <iostream>
#include <fstream>
#include <string.h>
#include <string>
#include <sstream>
#include <windows.h>
#include <shellapi.h>
#include "errores.h"
#include "estudiantes.h"
#include "tareas.h"

#define SSTR( x ) static_cast< std::ostringstream & >( \
        ( std::ostringstream() << std::dec << x ) ).str()

using namespace std;

graphviz::graphviz()
{
}

string agregarNodoCola(int numeroNodo,errores error){
	
	string texto = "N"+SSTR(numeroNodo) + "[label=\"id:";
	
	
	texto=texto+SSTR(error.id)+"\n";
	texto=texto+"Tipo: " + error.tipo + "\n";
	texto=texto+"Descripcion: " + error.descripcion + "\", shape=box];"	;
	
	return texto;
}


string conectarNodosCola(int numeroNodo){
	string texto ="\n";
	texto = texto + "N"+SSTR(numeroNodo) + "->" +"N"+SSTR(numeroNodo+1)+";";
	return texto;
}


void imprimirCola(nodoCola *&cabeza,int indice){

	ofstream archivo;
	
			
	string nombreSalidaArchivo="Graficas/ArchivosDot/cola" + SSTR(indice) + ".dot";
	
	char nombreSalidaArchivoCHAR[nombreSalidaArchivo.length()];	
	for(int i=0;i < nombreSalidaArchivo.length();i++){
		nombreSalidaArchivoCHAR[i] = nombreSalidaArchivo[i];
	}
	
	string nombreSalidaComando = "Graficas\\ArchivosDot\\cola" + SSTR(indice) +".dot";
	string nombreArchivo ="cola"+SSTR(indice) +".svg";
	
	string comandoFinal="START dot.exe -Tsvg " + nombreSalidaComando + " -o Graficas\\" + nombreArchivo;
	
	cout << comandoFinal.length();
	
	char comandoFinalCHAR[comandoFinal.length()];
	for(int i=0;i < comandoFinal.length();i++){
		comandoFinalCHAR[i] = comandoFinal[i];
	}
					
	
	archivo.open(nombreSalidaArchivoCHAR, ios_base::out);
	
	if(archivo.fail()){
		cout << "Error al momento de crear el archivo" << endl;
	}else{
	
		archivo<<"digraph cola{ \n rankdir=LR;" ;
		
		//Creamos los nodos en graphviz		
		nodoCola *aux= cabeza;
		int contadorNodo=0;
		
		while(aux!=NULL){
			archivo << "\n";
			archivo << agregarNodoCola(contadorNodo,aux->info);
			aux = aux->siguiente;
			contadorNodo++;
		};
		
		//Creamos las conexiones de los nodos
		contadorNodo=0;
		aux=cabeza;
		while(aux->siguiente!=NULL){			
			archivo << conectarNodosCola(contadorNodo);
			aux = aux->siguiente;
			contadorNodo++;
		};
		
		
		archivo<<"}";
	};
	
	archivo.close();	
	system(comandoFinalCHAR);
	
}



/*--------------------------------------------GRAFICAR LISTA ESTUDIANTES-----------------------------------------*/

string agregarNodoListaDobleCircular(int numeroNodo,estudiantes estudiante){
	
	string texto = "N"+SSTR(numeroNodo) + "[label=\"Carnet:";
	
	
	texto=texto+estudiante.carnet+"\n";
	texto=texto+"DPI: " + estudiante.dpi + "\n";
	texto=texto+"Nombre: " + estudiante.nombre + "\n";
	texto=texto+"Carrera: " + estudiante.carrera + "\n";
	texto=texto+"Password: " + estudiante.contrasenia + "\n";
	texto=texto+"Creditos: " + estudiante.creditos + "\n";
	texto=texto+"Edad: " + estudiante.edad + "\", shape=box];"	;
	
	return texto;
}

string conectarNodoListaDobleCircular(int numeroNodo,int numeroNodoFinal){
	string texto ="\n";
	
	if(numeroNodo==0){
		texto = texto + "N"+SSTR(numeroNodo) + "->" +"N"+SSTR(numeroNodo+1)+";\n";
		texto = texto + "N"+SSTR(numeroNodo) + "->" +"N"+SSTR(numeroNodoFinal)+";\n";
	}else if(numeroNodo==numeroNodoFinal){
		texto = texto + "N"+SSTR(numeroNodo) + "->" +"N0;\n";
	}else{
		texto = texto + "N"+SSTR(numeroNodo) + "->" +"N"+SSTR(numeroNodo-1)+";\n";
		texto = texto + "N"+SSTR(numeroNodo) + "->" +"N"+SSTR(numeroNodo+1)+";\n";
	}
	
	
	return texto;
}

void imprimirEstudiantes(nodoLDC *&cabeza,int indice){
	ofstream archivo;
	
			
	string nombreSalidaArchivo="Graficas/ArchivosDot/estudiantes" + SSTR(indice) + ".dot";
	
	char nombreSalidaArchivoCHAR[nombreSalidaArchivo.length()] = "";	
	for(int i=0;i < nombreSalidaArchivo.length();i++){
		nombreSalidaArchivoCHAR[i] = nombreSalidaArchivo[i];
	}
	
	string nombreSalidaComando = "Graficas\\ArchivosDot\\estudiantes" + SSTR(indice) +".dot";
	string nombreArchivo ="estudiantes"+SSTR(indice) +".svg";
	
	string comandoFinal="START dot.exe -Tsvg " + nombreSalidaComando + " -o Graficas\\" + nombreArchivo;
	char comandoFinalCHAR[comandoFinal.length()]="";
	for(int i=0;i < comandoFinal.length();i++){
		comandoFinalCHAR[i] = comandoFinal[i];
	}
					
	
	archivo.open(nombreSalidaArchivoCHAR, ios_base::out);
	
	if(archivo.fail()){
		cout << "Error al momento de crear el archivo" << endl;
	}else{
	
		archivo<<"digraph estudiantes{ \n rankdir=LR;" ;
		
		//Creamos los nodos en graphviz		
		nodoLDC *aux= cabeza;
		int contadorNodo=0;
		int contadorNodoFinal;
		
		while(aux->siguiente!=cabeza){
			archivo << "\n";
			archivo << agregarNodoListaDobleCircular(contadorNodo,aux->info);
			aux = aux->siguiente;									
			contadorNodo++;
			
			if(aux->siguiente==cabeza){
				archivo << "\n";
				archivo << agregarNodoListaDobleCircular(contadorNodo,aux->info);
			};
		};
		
		//Creamos las conexiones de los nodos
		contadorNodoFinal=contadorNodo;
		contadorNodo=0;
		aux=cabeza;
		while(aux->siguiente!=cabeza){			
			archivo << conectarNodoListaDobleCircular(contadorNodo,contadorNodoFinal);
			aux = aux->siguiente;						
			contadorNodo++;
			
			if(aux->siguiente==cabeza){
				archivo << "\n";
				archivo << conectarNodoListaDobleCircular(contadorNodo,contadorNodoFinal);
			};
			
			
		};
		
		
		archivo<<"concentrate=true }";
	};
	
	archivo.close();	
	system(comandoFinalCHAR);
}



/*-----------------------------------------GRAFICAR LISTA TAREAS ------------------------------------------------*/

string agregarNodoListaDoble(int numeroNodo,tareas tarea){
	
	string texto = "N"+SSTR(numeroNodo) + "[label=\"Carnet:";	
	
	texto=texto+tarea.carnet+"\n";
	texto=texto+"ID: " + SSTR(tarea.idT) + "\n";
	texto=texto+"Nombre: " + tarea.nombreTarea + "\n";
	texto=texto+"Descripcion: " + tarea.descripcion + "\n";
	texto=texto+"Materia: " + tarea.materia + "\n";
	texto=texto+"Fecha: " + tarea.fecha + "\n";
	texto=texto+"Hora: " + SSTR(tarea.hora) + "\n";
	texto=texto+"Estado: " + tarea.estado + "\", shape=box];"	;
	
	return texto;
}

string conectarNodoListaDoble(int numeroNodo){
	string texto ="\n";
	
	if(numeroNodo==0){
		texto = texto + "N"+SSTR(numeroNodo) + "->" +"N"+SSTR(numeroNodo+1)+";\n";		
	}else{
		texto = texto + "N"+SSTR(numeroNodo) + "->" +"N"+SSTR(numeroNodo-1)+";\n";
		texto = texto + "N"+SSTR(numeroNodo) + "->" +"N"+SSTR(numeroNodo+1)+";\n";
	}
	
	
	return texto;
}


void imprimirTareas(nodoLD *&cabeza,int indice){
	ofstream archivo;
	
			
	string nombreSalidaArchivo="Graficas/ArchivosDot/tareas" + SSTR(indice) + ".dot";
	
	char nombreSalidaArchivoCHAR[nombreSalidaArchivo.length()] = "";	
	for(int i=0;i < nombreSalidaArchivo.length();i++){
		nombreSalidaArchivoCHAR[i] = nombreSalidaArchivo[i];
	}
	
	string nombreSalidaComando = "Graficas\\ArchivosDot\\tareas" + SSTR(indice) +".dot";
	string nombreArchivo ="tareas"+SSTR(indice) +".svg";
	
	
	
	
	string comandoFinal="START dot.exe -Tsvg " + nombreSalidaComando + " -o Graficas\\" + nombreArchivo;
	char comandoFinalCHAR[comandoFinal.length()]="";
	for(int i=0;i < comandoFinal.length();i++){
		comandoFinalCHAR[i] = comandoFinal[i];
		
	}
					
	
	archivo.open(nombreSalidaArchivoCHAR, ios_base::out);
	
	if(archivo.fail()){
		cout << "Error al momento de crear el archivo" << endl;
	}else{
	
		archivo<<"digraph tareas{ \n rankdir=LR;" ;
		
		//Creamos los nodos en graphviz		
		nodoLD *aux= cabeza;
		int contadorNodo=0;
		int contadorNodoFinal;
		
		while(aux!=NULL){
			archivo << "\n";
			archivo << agregarNodoListaDoble(contadorNodo,aux->info);
			aux = aux->siguiente;									
			contadorNodo++;
						
		};
		
		//Creamos las conexiones de los nodos
		contadorNodoFinal=contadorNodo;
		contadorNodo=0;
		aux=cabeza;
		while(aux!=NULL){			
			archivo << conectarNodoListaDoble(contadorNodo);
			aux = aux->siguiente;						
			contadorNodo++;
											
		};
		
		
		archivo<<"concentrate=true; }";
	};
	
	archivo.close();	
	system(comandoFinalCHAR);
}


void imprimirTareasFiltradas(nodoLD *&cabeza,int indice){
	ofstream archivo;
	
			
	string nombreSalidaArchivo="Graficas/ArchivosDot/tf" + SSTR(indice) + ".dot";
	
	char nombreSalidaArchivoCHAR[nombreSalidaArchivo.length()] = "";	
	for(int i=0;i < nombreSalidaArchivo.length();i++){
		nombreSalidaArchivoCHAR[i] = nombreSalidaArchivo[i];
	}
	
	string nombreSalidaComando = "Graficas\\ArchivosDot\\tf" + SSTR(indice) +".dot";
	string nombreArchivo ="tf"+SSTR(indice) +".svg";
	
	
	
	
	string comandoFinal="START dot.exe -Tsvg " + nombreSalidaComando + " -o Graficas\\" + nombreArchivo;
	char comandoFinalCHAR[comandoFinal.length()+1];
	for(int i=0;i < comandoFinal.length();i++){
		comandoFinalCHAR[i] = comandoFinal[i];
		
	}
					
	
	archivo.open(nombreSalidaArchivoCHAR, ios_base::out);
	
	if(archivo.fail()){
		cout << "Error al momento de crear el archivo" << endl;
	}else{
	
		archivo<<"digraph tf{ \n rankdir=LR;" ;
		
		//Creamos los nodos en graphviz		
		nodoLD *aux= cabeza;
		int contadorNodo=0;		
		
		while(aux->siguiente!=NULL){
			archivo << "\n";
			if(aux->info.carnet!="vacio"){
				archivo << agregarNodoListaDoble(contadorNodo,aux->info);
				aux = aux->siguiente;									
				contadorNodo++;
			}else{
				aux = aux->siguiente;
			};									
		};
		
		//Creamos las conexiones de los nodos
		
		contadorNodo=0;
		aux=cabeza;				
		while(aux->siguiente!=NULL){			
		
			if(aux->info.carnet!="vacio"){
				archivo << conectarNodoListaDoble(contadorNodo);
				aux = aux->siguiente;						
				contadorNodo++;
			}else{
				aux = aux->siguiente;
			};																
		};
		
		
		archivo<<"concentrate=true; }";
	};
	
	archivo.close();	
	system(comandoFinalCHAR);
}











