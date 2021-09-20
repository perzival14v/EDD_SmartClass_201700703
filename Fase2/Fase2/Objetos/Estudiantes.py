class estudiante:
    def __init__(self):
        self.carnet=None
        self.dpi=None
        self.nombre=None
        self.carrera=None
        self.correo=None
        self.password=None
        self.creditos=None
        self.edad=None
        self.yearList=None

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