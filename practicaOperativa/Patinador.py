

class Patinador:
    __apellido = str
    __nombre = str
    __dni = str
    __edad = int
    __club = str

    def __init__(self, apellido, nombre, dni, edad, club):
        self.__apellido = apellido
        self.__nombre = nombre
        self.__dni = dni
        self.__edad = edad
        self.__club = club
    def __str__(self) -> str:
        return f"{self.__apellido}, {self.__nombre}, {self.__dni}, {self.__edad}, {self.__club}"
    

    def getApellido(self):
        return self.__apellido
    def getNombre(self):
        return self.__nombre
    def getDni(self):
        return self.__dni
    def getEdad(self):
        return self.__edad
    def getClub(self):
        return self.__club
    
    def setApellido(self, apellido):
        self.__apellido = apellido
    def setNombre(self, nombre):
        self.__nombre = nombre
    def setDni(self, dni):
        self.__dni = dni
    def setEdad(self, edad):
        self.__edad = edad
    def setClub(self, club):
        self.__club = club
    