#include "graphviz.h"
#include <iostream>
#include <fstream>
#include <string.h>
#include <string>
#include <sstream>
#include <windows.h>
#include <shellapi.h>


using namespace std;

graphviz::graphviz()
{
}


void imprimirCola(nodoCola *&cabeza,int indice){

	ofstream archivo;
	
	stringstream conversor;
	conversor << indice;
			
	string nombreSalidaArchivo="Graficas/ArchivosDot/cola" + conversor.str() + ".dot";
	
	char nombreSalidaArchivoCHAR[nombreSalidaArchivo.length()] = "";	
	for(int i=0;i < nombreSalidaArchivo.length();i++){
		nombreSalidaArchivoCHAR[i] = nombreSalidaArchivo[i];
	}
	
	string nombreSalidaComando = "Graficas\\ArchivosDot\\cola" + conversor.str() +".dot";
	string nombreArchivo ="cola"+conversor.str() +".png";
	
	string comandoFinal="START dot.exe -Tpng C:\\Users\\USUARIO\\Desktop\\Javier\\Universidad\\EDD\\Fase_1\\" + nombreSalidaComando + " -o C:\\Users\\USUARIO\\Desktop\\Javier\\Universidad\\EDD\\Fase_1\\Graficas\\" + nombreArchivo;
	char comandoFinalCHAR[comandoFinal.length()]="";
	for(int i=0;i < comandoFinal.length();i++){
		comandoFinalCHAR[i] = comandoFinal[i];
	}
					
	
	archivo.open(nombreSalidaArchivoCHAR, ios_base::out);
	
	if(archivo.fail()){
		cout << "Error al momento de crear el archivo" << endl;
	}else{
	
		archivo<<"""digraph ejemplo1{ \n \
					nodo0; \n \
					nodo1; \n \
				}""" ;
		
		
	};
		
	system(comandoFinalCHAR);
	
}


