#include <iostream>
#include <string.h>
#include <string>
#include <Windows.h>
#include <cstdio>
#include <fstream>
#include <stdlib.h>
#include "Listas.h"

using namespace std;

int main() {
	
	SetConsoleOutputCP(CP_UTF8);
	
	
	int opcion=0;
	char ruta[60];
	string linea;		
	
	
	while(opcion!=5){
		cout << prueba.saludo<<endl;
		cout << "******** Menu ********"<<endl;
		cout << " 1. Carga de usuarios"<<endl;
		cout << " 2. Carga de tareas"<<endl;
		cout << " 3. Ingreso manual"<<endl;
		cout << " 4. Reportes"<<endl;
		cout << " 5. Salir"<<endl;
		cout << "Ingrese el numero de opcion"<<endl;
		cin>>opcion;
		
		switch(opcion){
			case 1:{
				
				cout << "Ingrese el nombre del archivo"<<endl;
				cin>>ruta;
				
				ifstream archivo;			
				archivo.open(ruta,ios::in);
				
				if(archivo.fail()){
					cout<<"Error en abrir el archivo\n";					
				}else{
					
					while(!archivo.eof()){
						getline(archivo,linea);
						cout<<linea<<endl;
					}
					
					
					archivo.close();
				}
					
				
				break;
			}
						
				
			case 2:{
				
				break;
			}				
			case 3:{
				
				break;
			}				
			case 4:{
				
				break;
			}							
			default:{
				cout <<"Error en la entrada"<<endl;
				break;					
			}				
		}
	}
	
	
	
	
	
	return 0;		

