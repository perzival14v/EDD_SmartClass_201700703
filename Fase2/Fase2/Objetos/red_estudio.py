from Fase2.Objetos.curso import *



class redEstudio(object):

    def cargar_cursos(self):

        #Estructura -> codigo curso, nombre curso, creditos que da el curso, prerequisitos

        #Primer Semestre        
        self.red_de_estudio["017"]=["017","Social Humanistica 1","4",[]]
        self.red_de_estudio["101"]=["101","Mate Basica 1","7",[]]
        self.red_de_estudio["069"]=["069","Tecnica Complementaria 1","3",[]]
        self.red_de_estudio["348"]=["348","Quimica General","3",[]]

        #Segundo Semestre

        self.red_de_estudio["019"]=["019","Social Humanistica 2","4",["017"]]
        self.red_de_estudio["103"]=["103","Mate Basica 2","7",["101"]]
        self.red_de_estudio["005"]=["005","Tecnicas de estudio e investigacion","3",[]]
        self.red_de_estudio["147"]=["147","Fisica Basica","5",["101"]]
        
        #Tercer Semestre
        self.red_de_estudio["795"]=["795","Logica de sistemas","2",["103"]]
        self.red_de_estudio["960"]=["960","Mate Computo 1","5",["103"]]
        self.red_de_estudio["770"]=["770","IPC 1","4",["103"]]
        self.red_de_estudio["107"]=["107","Mate Intermedia 1","10",["103"]]
        self.red_de_estudio["150"]=["150","Fisica 1","6",["103","147"]]

        #Cuarto Semestre
        self.red_de_estudio["732"]=["732","Estadistica 1","5",["107","005"]]
        self.red_de_estudio["796"]=["796","Lenguajes Formales y de Programacion","3",["770","795","960"]]
        self.red_de_estudio["962"]=["962","Mate Computo 2","5",["960","770","795"]]
        self.red_de_estudio["771"]=["771","IPC 2","5",["107","770","795","960"]]
        self.red_de_estudio["112"]=["112","Mate Intermedia 2","5",["107"]]
        self.red_de_estudio["114"]=["114","Mate Intermedia 3","5",["107"]]
        self.red_de_estudio["152"]=["152","Fisica 2","6",["107","150"]]
        self.red_de_estudio["2025"]=["2025","Practica Inicial","0",["103","770"]]

        #Quinto Semestre
        self.red_de_estudio["736"]=["736","Analisis Probabilistico","4",["732"]]
        self.red_de_estudio["777"]=["777","ORG. Lenguajes y Compiladores 1","4",["771","796","962"]]
        self.red_de_estudio["964"]=["964","Organizacion Computacional","3",["152","771","962"]]
        self.red_de_estudio["772"]=["772","Estructura de Datos","5",["771","796","962"]]
        self.red_de_estudio["116"]=["116","Mate Aplicada 3","5",["112","114"]]
        self.red_de_estudio["118"]=["118","Mate Aplicada 1","6",["112","114"]]

        #Sexto Semestre
        self.red_de_estudio["722"]=["722","Teoria de Sistemas 1","5",["732","772","116","118"]]
        self.red_de_estudio["601"]=["601","Investigacion de Operaciones 1","5",["771","732"]]
        self.red_de_estudio["014"]=["014","Economia","4",["732"]]
        self.red_de_estudio["781"]=["781","ORG. Lenguajes y Compiladores 2","5",["777","772"]]
        self.red_de_estudio["778"]=["778","ARQ. Compu y Ensambladores 1","5",["796","964"]]
        self.red_de_estudio["773"]=["773","Manejo e Implementacion de Archivos","4",["772","796"]]

        #Septimo Semestre
        self.red_de_estudio["724"]=["724","Teoria de sistemas 2","5",["722","601","736"]]
        self.red_de_estudio["603"]=["603","Investigacion de Operaciones 2","5",["601"]]
        self.red_de_estudio["281"]=["281","Sistemas Operativos 1","5",["781","778"]]
        self.red_de_estudio["779"]=["779","ARQ. Compu y Ensambladores 2","4",["778"]]
        self.red_de_estudio["970"]=["970","Redes de Computadoras 1","4",["773","778"]]
        self.red_de_estudio["774"]=["774","Sistemas de Bases de Datos 1","5",["773"]]
        self.red_de_estudio["2036"]=["2036","Practica Intermedia","0",["778","777","773","2025"]]


        #Octavo Semestre
        self.red_de_estudio["285"]=["285","Sistemas Operativos 2","4",["281"]]
        self.red_de_estudio["975"]=["975","Redes de Computadoras 2","4",["970"]]
        self.red_de_estudio["775"]=["775","Sistemas de Bases de Datos 2","4",["281","774"]]
        self.red_de_estudio["283"]=["283","Analisis y Diseño de Sistemas 1","5",["774"]]
        self.red_de_estudio["797"]=["797","Seminario de Sistemas 1","4",["724"]]
        


        #Noveno Semestre
        self.red_de_estudio["729"]=["729","Modelacion y Simulacion 1","5",["724","603"]]
        self.red_de_estudio["786"]=["786","Sistemas Organizacionales y Gerenciales 1","4",["283","722"]]
        self.red_de_estudio["972"]=["972","Inteligencia Artificial 1","4",["781","775","724"]]
        self.red_de_estudio["785"]=["785","Analisis y Diseño de Sistemas 2","5",["283"]]
        self.red_de_estudio["798"]=["798","Seminario de Sistemas 2","3",["797"]]
        self.red_de_estudio["2037"]=["2037","Practica Final","0",["2036"]]


        #Decimo Semestre
        self.red_de_estudio["786"]=["786","Sistemas Organizacionales y Gerenciales 2","4",["786"]]
        self.red_de_estudio["720"]=["720","Modelacion y Simulacion 2","5",["729"]]
        self.red_de_estudio["780"]=["780","Software Avanzado","6",["785"]]
        self.red_de_estudio["799"]=["799","Seminario de Investigacion","3",["798"]]
        

    def __init__(self):        
        self.red_de_estudio = {}
        self.cargar_cursos()



