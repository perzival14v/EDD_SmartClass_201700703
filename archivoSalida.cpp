#include "archivoSalida.h"
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
#include "listas.h"

#define SSTR( x ) static_cast< std::ostringstream & >( \
        ( std::ostringstream() << std::dec << x ) ).str()

using namespace std;

archivoSalida::archivoSalida()
{
}


string parserFecha(string fecha){
	
	string year;
	string mes;
	string dia;
	int contadorBarra=0;
	string palabra;
	
	for(int i=0;i<fecha.length();i++){				
		if(fecha[i]=='/'){
			contadorBarra++;
			
			switch(contadorBarra){
				case 1:{
					year=palabra;
					break;
				};
				case 2:{
					mes=palabra;
					break;
				};	
			};
			palabra="";
			
		}else{
			palabra = palabra + fecha[i];	
		}
	};
	
	
	dia=palabra;
	
	return dia + "/" + mes +"/" + year;
	
	
}

void generarArchivoSalida(nodoLDC *&cabezaEstudiantes, nodoLD *&cabezaTareas){
	
	nodoLD *auxTareas = cabezaTareas;
	nodoLDC *auxEstudiantes = cabezaEstudiantes;		
	ofstream archivo;	
	
	
	
	archivo.open("Salida\\Salida.txt", ios_base::out);
	
	if(archivo.fail()){
		cout << "Error al momento de crear el archivo" << endl;
	}else{
		archivo << "¿Elements?";
		
		//Agregamos tareas
		while(auxTareas->siguiente!=NULL){	
		
			if(auxTareas->info.carnet!="vacio"){
				archivo << "\n\t¿element type=\"task\"?";			
				archivo << "\n\t\t¿item Carnet = \"" << auxTareas->info.carnet << "\" $?";
				archivo << "\n\t\t¿item Nombre = \"" << auxTareas->info.nombreTarea << "\" $?";
				archivo << "\n\t\t¿item Descripcion = \"" << auxTareas->info.descripcion << "\" $?";
				archivo << "\n\t\t¿item Materia = \"" << auxTareas->info.materia << "\" $?";
				archivo << "\n\t\t¿item Fecha = \"" << parserFecha(auxTareas->info.fecha) << "\" $?";
				archivo << "\n\t\t¿item Hora = \"" << auxTareas->info.hora << "\" $?";
				archivo << "\n\t\t¿item Estado = \"" << auxTareas->info.estado << "\" $?";
				
				archivo << "\n\t¿$element?";	
			}
												
			auxTareas = auxTareas->siguiente;										
						
		};
		
		//Agregamos usuarios
		while(auxEstudiantes->siguiente!=cabezaEstudiantes){			
			archivo << "\n\t¿element type=\"user\"?";			
			archivo << "\n\t\t¿item Carnet = \"" << auxEstudiantes->info.carnet << "\" $?";
			archivo << "\n\t\t¿item DPI = \"" << auxEstudiantes->info.dpi << "\" $?";
			archivo << "\n\t\t¿item Nombre = \"" << auxEstudiantes->info.nombre << "\" $?";
			archivo << "\n\t\t¿item Carrera = \"" << auxEstudiantes->info.carrera << "\" $?";
			archivo << "\n\t\t¿item Password = \"" << auxEstudiantes->info.contrasenia << "\" $?";
			archivo << "\n\t\t¿item Creditos = \"" << auxEstudiantes->info.creditos << "\" $?";
			archivo << "\n\t\t¿item Edad = \"" << auxEstudiantes->info.edad << "\" $?";
			
			archivo << "\n\t¿$element?";
			
			auxEstudiantes = auxEstudiantes->siguiente;	
			
			if(auxEstudiantes->siguiente==cabezaEstudiantes){
				archivo << "\n\t¿element type=\"user\"?";			
				archivo << "\n\t\t¿item Carnet = \"" << auxEstudiantes->info.carnet << "\" $?";
				archivo << "\n\t\t¿item DPI = \"" << auxEstudiantes->info.dpi << "\" $?";
				archivo << "\n\t\t¿item Nombre = \"" << auxEstudiantes->info.nombre << "\" $?";
				archivo << "\n\t\t¿item Carrera = \"" << auxEstudiantes->info.carrera << "\" $?";
				archivo << "\n\t\t¿item Password = \"" << auxEstudiantes->info.contrasenia << "\" $?";
				archivo << "\n\t\t¿item Creditos = \"" << auxEstudiantes->info.creditos << "\" $?";
				archivo << "\n\t\t¿item Edad = \"" << auxEstudiantes->info.edad << "\" $?";
				archivo << "\n\t¿$element?";
			}
			
			
														
						
		};
		
		
		archivo << "¿\n$Elements?";
	};
	
	
	
}
