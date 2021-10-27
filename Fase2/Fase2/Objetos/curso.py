class Curso:
    def __init__(self) -> "constructor":
        self.codigo=None
        self.nombre=None
        self.creditos=None
        self.pre_requisitos=None
        self.lista_pre_requisitos=[]
        self.obligatorio = None
        
    #Se usara para el grafo de los cursos
    def iniciar(self,codigo,nombre,creditos,lista):
        self.codigo=codigo
        self.nombre=nombre
        self.creditos=creditos        
        self.lista_pre_requisitos=lista        