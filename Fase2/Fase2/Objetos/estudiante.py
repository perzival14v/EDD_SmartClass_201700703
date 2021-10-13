
from Fase2.Estructuras.ListaDoble import listaDoble
from Fase2.Estructuras.matriz_dispersa import matrizDispersa

class Estudiantes:
    def __init__(self):
        self.carnet=None
        self.dpi=None
        self.nombre=None
        self.carrera=None
        self.correo=None
        self.password=None
        self.creditos=None
        self.edad=None
        self.yearList=listaDoble()

    def iniciar(self,carnet,dpi,nombre,carrera,correo,password,creditos,edad,yearList):
        self.carnet=carnet
        self.dpi=dpi
        self.nombre=nombre
        self.carrera=carrera
        self.correo=correo
        self.password=password
        self.creditos=creditos
        self.edad=edad
        self.yearList=yearList

def buscar_y_agregar_tarea(lista, anio,mes,dia,hora,tarea):
    
    nodoAño = lista.buscar(anio)

    if nodoAño == None:
        lista.agregar(anio)
    
    nodoAño = lista.buscar(anio)

    if nodoAño.conexion1 == None:
        nodoAño.conexion1 = listaDoble()
    if nodoAño.conexion2 == None:
        nodoAño.conexion2 = listaDoble()

    nodoMes = nodoAño.conexion2.buscar(mes)
    if nodoMes == None:
        nodoAño.conexion2.agregar(mes)
    
    nodoMes = nodoAño.conexion2.buscar(mes)

    if nodoMes.conexion1 == None:
        nodoMes.conexion1 =  matrizDispersa()

    nodoMes.conexion1.agregar(int(hora),int(dia),tarea)


def buscar_matriz_dispersa(estudiante:Estudiantes, anio, mes):

    try:
        nodo_anio= estudiante.yearList.buscar(anio)

        if nodo_anio == None:
            return None
        else:
            nodo_mes = nodo_anio.conexion2.buscar(mes)

            if nodo_mes == None:
                return None
            else:
                return nodo_mes.conexion1
            
    except:
        return None


