#ifndef ESTUDIANTES_H
#define ESTUDIANTES_H
#include <iostream>
#include <string.h>
#include <string>
#include <stdlib.h>

using namespace std;


class estudiantes
{
	public:
		string carnet;
		string dpi;
		string nombre;
		string carrera;
		string correo;
		string contrasenia;
		string creditos;
		string edad;
		estudiantes();
		estudiantes(string carnet, string dpi, string nombre, string carrera, string correo, string contrasenia, string creditos, string edad);
	protected:
};

estudiantes analizarTextoEstudiantes(string linea,int contador){
	
	string carnet;
	string dpi;
	string nombre;
	string carrera;
	string correo;
	string pasw;
	string credi;
	string edad;											
	string palabra;						
	
	
	for(int j=0; j<linea.length();j++){
							
		if(linea[j]=='\n'){
			break;
		};
							
		if(linea[j]==','){
								
			switch(contador){
				case 0:{
					carnet = palabra;
					break;
				}
				case 1:{
					dpi = palabra;
					break;
				}
				case 2:{
					nombre = palabra;
					break;
				}
				case 3:{
					carrera = palabra;
					break;
				}
				case 4:{
					correo = palabra;
					break;
				}
				case 5:{
					pasw = palabra;
					break;
				}
				case 6:{
					credi = palabra;
					break;
				}
				case 7:{
					edad = palabra;
					break;
						}										
				};
																								
				contador++;
				palabra="";
								
		}else{
			palabra=palabra+linea[j];																									
			};
	};
	
	estudiantes nuevo = estudiantes(carnet,dpi,nombre,carrera,correo,pasw,credi,edad);
	
	return nuevo;
	
};



#endif
