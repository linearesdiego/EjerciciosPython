
class Moto:
    __patente = str
    __marca = str
    __nombre = str
    __apellido = str
    __kilometraje = float
    def __init__(self, patente, marca, nombre, apellido, kilometraje):
        self.__patente = patente
        self.__marca = marca
        self.__nombre = nombre
        self.__apellido = apellido
        self.__kilometraje = kilometraje

    def __str__(self):
        return f'Patente: {self.__patente}, Marca: {self.__marca}, Nombre: {self.__nombre}, Apellido: {self.__apellido}, Kilometraje: {self.__kilometraje}'
    def getPatente(self):
        return self.__patente
    def getNombre(self):
        return self.__nombre    
    def getApellido(self): 
        return self.__apellido   
    def getKilometraje(self):
        return self.__kilometraje
    def getMarca(self):
        return self.__marca
    
    def setKilometraje(self, kilometraje):
        self.__kilometraje = kilometraje
    def setNombre(self, nombre):
        self.__nombre = nombre
    def setApellido(self, apellido):
        self.__apellido = apellido
    def setMarca(self, marca):
        self.__marca = marca
    def setPatente(self, patente):
        self.__patente = patente
    
