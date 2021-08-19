#include "estudiantes.h"

#include <iostream>
using namespace std;

estudiantes::estudiantes(){
	carnet=1;
	dpi=1;
	nombre="vacio";
	carrera="vacio";
	correo="vacio";
	contrasenia="vacio";
	creditos=1;
	edad=1;
}


estudiantes::estudiantes(string _carnet, string _dpi, string _nombre, string _carrera, string _correo, string _contrasenia, string _creditos, string _edad){
	carnet=_carnet;
	dpi=_dpi;
	nombre=_nombre;
	carrera=_carrera;
	correo=_correo;
	contrasenia=_contrasenia;
	creditos=_creditos;
	edad=_edad;
}

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
							
		if(j==linea.length()-1){
			correo = palabra+linea[linea.length()-1];
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
					pasw = palabra;
					break;
				}
				case 5:{
					credi = palabra;
					break;
				}
				case 6:{
					edad = palabra;
					break;
				}
				case 7:{					
					correo = palabra;
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
	
}
