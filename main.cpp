#include <iostream>
#include <string.h>
#include <string>
#include <Windows.h>
#include <cstdio>
#include <fstream>
#include <stdlib.h>
#include "estudiantes.h"
#include "tareas.h"
#include "Listas.h"
#include "errores.h"


using namespace std;


int main() {
	
	SetConsoleOutputCP(CP_UTF8);
	
	
	int opcion=0;
	char ruta[60];
	string linea;
	
	//orden de la matriz de tareas, [meses][dias][horas]			
	tareas matrizTareas[5][30][9];	
	
	nodoLDC *listaEstudiantes=NULL;
	
	
	
	
	
	while(opcion!=5){		
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
				/*Carga de estudiantes*/
				cout << "Ingrese el nombre del archivo"<<endl;
				cin>>ruta;
				
				ifstream archivo;			
				archivo.open(ruta,ios::in);
				
				if(archivo.fail()){
					cout<<"Error en abrir el archivo\n";					
				}else{
					
					int contador=-1;
					
					while(!archivo.eof()){						
						/*Lectura linea por linea*/
						getline(archivo,linea);
						
						//Saltar la primera linea																		
						if(contador==-1){
							contador++;
							continue;	
						};
						
						//Analizamos el texto, luego convertimos a un objeto tipo estudiante, luego lo agregamos a la lista doblemente enlazada
						
						estudiantes nuevoE = analizarTextoEstudiantes(linea,contador);
						agregarLDC(listaEstudiantes,nuevoE);																	
					}
					
					
					archivo.close();
				}
				
				
				cout << endl;			
				recorrerLDC(listaEstudiantes);
				cout << endl;
				
				cout << endl;			
				recorrerLDC(listaEstudiantes);
				cout << endl;
				
							
				break;
			}
						
				
			case 2:{
				/*Carga de tareas*/
				
				string palabra;
				int mes;
				int dia;
				int hora;
				
				
				cout << "Ingrese el nombre del archivo"<<endl;
				cin>>ruta;
				
				ifstream archivo;			
				archivo.open(ruta,ios::in);
				
				if(archivo.fail()){
					cout<<"Error en abrir el archivo\n";					
				}else{
					
					int contador=-1;
					
					while(!archivo.eof()){						
						/*Lectura linea por linea*/
						getline(archivo,linea);
						
						//Saltar la primera linea																		
						if(contador==-1){
							contador++;
							continue;	
						};
						//Analizamos las tareas	(una linea)					
						for(int j=0;j<linea.length();j++){
							if(contador<3){
								if(linea[j]=","){
									
									switch(contador){
										case 0:{
											mes = stoi(palabra);
											break;
										};
										case 1:{
											dia = stoi(palabra);
											break;
										};
										case 2:{
											hora = stoi(palabra);
											break;
										};
									};									
									
									contador++;
									palabra="";
								}else{
									palabra=palabra+linea[j];
								}
								
							}else if(linea[j]=='\n'){
								contador=0;
								palabra="";
							};	
						};																					
					}
					
					
					archivo.close();
				}
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
};		


/*FUNCIONES UTILIZADAS DENTRO DEL CODIGO DEMASIADO GRANDES PARA DEJARLAS DENTRO DEL MAIN*/







