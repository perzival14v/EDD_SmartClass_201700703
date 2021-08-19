#include <iostream>
#include <string.h>
#include <string>
#include <Windows.h>
#include <cstdio>
#include <fstream>
#include <stdlib.h>
#include <sstream>

#include "listas.h"

#include "estudiantes.h"

#include "tareas.h"

#include "errores.h"


using namespace std;

estudiantes analizarTextoEstudiantes(string linea,int contador);
int verificarDPI(string dpi);
int verificarCarnet(string carnet);
void mostrarDatos(tareas matriz[][30][9]);


void agregarLDC(nodoLDC *&punteroCabeza, estudiantes e1);
void recorrerLDC(nodoLDC *&cabeza);

void agregarLD(nodoLD *&punteroCabeza, tareas t1);
void recorrerLD(nodoLD *&cabeza);

void columnMajor(nodoLD *&cabeza ,tareas matriz[][30][9]);

void encolar(nodoCola *&cabeza,errores e1);
void recorrerCola(nodoCola *&cola);

int verificarAsignacionCarnet(string carnet, nodoLDC *&cabeza);
int verificarFecha(string fecha);
int verificarCorreo(string correo);



int main(){
	
	SetConsoleOutputCP(CP_UTF8);
	
	
	int opcion=0;
	int idErrores=0;
	char ruta[60];
	string linea="";
	
	//orden de la matriz de tareas, [meses][dias][horas]			
	tareas matrizTareas[5][30][9];	
	
	nodoLDC *listaEstudiantes=NULL;	
	nodoLD  *listaTareas=NULL;
	nodoCola *colaErrores=NULL;
	
	
	
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
					int contadorLinea=1;
					
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
						
						//Iniciamos a verificar errores:
						
						
						// regresar 1 significa error, regresar 0 significa no error
						if(verificarDPI(nuevoE.dpi)==1){
							errores error = errores(idErrores,"Estudiante","DPI no tiene la cantidad de digitos correctos");
							cout << "ERROR EN DPI LINEA:" << contadorLinea << endl;
							encolar(colaErrores,error);
							
							
							idErrores++;
							
						};
						
						if(verificarCarnet(nuevoE.carnet)==1){
							errores error = errores(idErrores,"Estudiante","Carnet no tiene la cantidad de digitos correctos");
							cout << "ERROR EN CARNET LINEA:" << contadorLinea << endl;
							encolar(colaErrores,error);
							idErrores++;
							
						};
						
						if(verificarCorreo(nuevoE.correo)==1){
							errores error = errores(idErrores,"Estudiante","Correo no tiene un formato correcto");
							cout << "ERROR EN CORREO LINEA:" << contadorLinea << endl;
							encolar(colaErrores,error);
							idErrores++;
							
						};
						
						contadorLinea++;					
					}
					
					
					archivo.close();
				}																
							
				break;
			}										
			case 2:{
				/*Carga de tareas*/
				
				string palabra="";				
				int mes=0;
				int dia=0;
				int hora=0;																			
				int error=0;
				
				string carnet;
				string nombreTarea;
				string descripcion;
				string materia;
				string fecha;
				
				string estado;
																				
				
				cout << "Ingrese el nombre del archivo"<<endl;
				cin>>ruta;
				
				ifstream archivo;			
				archivo.open(ruta,ios::in);
				
				if(archivo.fail()){
					cout<<"Error en abrir el archivo\n";					
				}else{
					
					int contador=-1;
					int contadorLinea=1;
					int ID=0;
					
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
														
							
							if(j==linea.length()-1){
								estado=palabra+linea[linea.length()-1];
								contador=0;
								palabra="";
							}									
							else if(linea[j]==','){
														
								switch(contador){
									case 0:{
										stringstream conversorMes(palabra);										
										conversorMes >> mes;										
										
										
										if(mes>=7 && mes<=11){
												
										}else{
											cout<< "\nmes fuera de rango, se salta la tarea LINEA:" << contadorLinea << endl;
											contador=0;
											palabra="";
											error=1;
										};
																	
										break;
									};
									case 1:{
										stringstream conversorDia(palabra);
										conversorDia >> dia;
										
										
										
										if(dia>=0 && dia<=30){									
										}else{
											cout<< "\ndia fuera de rango, se salta la tarea LINEA:"<< contadorLinea << endl;
											contador=0;
											palabra="";	
											error=1;
										};												
											break;
									};
									case 2:{
										stringstream conversorHora(palabra);
										conversorHora >> hora;
											
										if(hora>=8 && hora<=16){
										}else{
											cout<< "\nhora fuera de rango, se salta la tarea LINEA:"<< contadorLinea << endl;
											contador=0;
											palabra="";
											error=1;
										};
																																						
										break;
									};
									
									case 3:{
										carnet = palabra;
										break;
									};
									
									case 4:{
										nombreTarea=palabra;
										break;
									};
									
									case 5:{
										descripcion=palabra;
										break;
									};
									
									case 6:{
										materia=palabra;
										break;
									};
									
									case 7:{
										fecha=palabra;
										break;
									};
								
																																													
								};			
								
									if(error==0){
										contador++;
										palabra="";
									}else{										
										break;
									}																		
										
							}else{
									palabra=palabra+linea[j];
							};
													
								
						};																
							//SI DAN UN DIA FUERA DE LA MATRIZ NO ENTRA AL IF											
						if(error==0){	
							tareas tarea = 	tareas(ID,carnet,nombreTarea,descripcion,materia,fecha,hora,estado);														
							matrizTareas[mes-7][dia-1][hora-8] = tarea;
							
												
							//Analizamos los errores
																					
							if(verificarAsignacionCarnet(tarea.carnet,listaEstudiantes)){
								errores error = errores(idErrores,"Tarea","Carnet no existe dentro de los estudiantes");
								cout << "ERROR EN CARNET NO EXISTENTE LINEA:" << contadorLinea << endl;
								encolar(colaErrores,error);
								idErrores++;
								
							};
							
							if(verificarFecha(tarea.fecha)){
								errores error = errores(idErrores,"Tarea","Fecha no tiene el formato correcto");
								cout << "ERROR EN FECHA LINEA:" << contadorLinea << endl;
								encolar(colaErrores,error);
								idErrores++;
								
							};
							
							contadorLinea++;						
							
							error=0;						
						}else{
							error=0;
						};
						
						
																										
					};
					
					
					archivo.close();
				}
				
				//Linealizamos la informacion
				cout << "\niniciamos la linealizacion de la informacion" << endl;
				columnMajor(listaTareas,matrizTareas);																				
				
				
				break;
			}				
			case 3:{
				
				int opcionMenuManual
				while(opcionMenuManual!=3){		
					cout << "******** Menu ********"<<endl;
					cout << " 1. Usuarios"<<endl;
					cout << " 2. Tareas"<<endl;					
					cout << " 3. Salir"<<endl;
					cout << "Ingrese el numero de opcion"<<endl;
					cin>>opcionMenuManual;
					
					switch(opcionMenuManual){
						case 1:{
							int opcionMMUsuarios
							while(opcionMMUsuarios!=4){		
								cout << "******** Menu USUARIOS********"<<endl;
								cout << " 1. Ingresar"<<endl;
								cout << " 2. Modificar"<<endl;					
								cout << " 3. Eliminar"<<endl;
								cout << " 4. Salir"<<endl;
								cout << "Ingrese el numero de opcion"<<endl;
								cin>>opcionMMUsuarios;
							}
							
							break;
						}		
						case 2:{
							
							int opcionMMTareas
							while(opcionMMTareas!=4){		
								cout << "******** Menu TAREAS********"<<endl;
								cout << " 1. Ingresar"<<endl;
								cout << " 2. Modificar"<<endl;					
								cout << " 3. Eliminar"<<endl;
								cout << " 4. Salir"<<endl;
								cout << "Ingrese el numero de opcion"<<endl;
								cin>>opcionMMTareas;
							}
							
							
							break;
						}
					};
					
				};
				
				break;
			}				
			case 4:{
				recorrerCola(colaErrores);
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


