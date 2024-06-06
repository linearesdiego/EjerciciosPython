""" De todos los vehículos se registra: marca, modelo, año de fabricación, capacidad de pasajeros,
número de plazas, distancia recorrida y tarifa base. """

class Vehiculo:
    __marca = str 
    __modelo = str
    __anio = str
    __capacidadPasajeros = int
    __numeroPlazas = int
    __distanciaRecorrida = float
    __tarifaBase = float

    def __init__(self, marca:str, modelo:str, anio:int, capacidadPasajeros:int, numeroPlazas:int, distanciaRecorrida:float, tarifaBase:float):
        self.__marca = marca
        self.__modelo = modelo
        self.__anio = anio
        self.__capacidadPasajeros = capacidadPasajeros
        self.__numeroPlazas = numeroPlazas
        self.__distanciaRecorrida = distanciaRecorrida
        self.__tarifaBase = tarifaBase
    
    def getMarca(self):
        return self.__marca
    
    def getModelo(self):
        return self.__modelo
    
    def getAnio(self):
        return self.__anio
    
    def getCapacidadPasajeros(self):
        return self.__capacidadPasajeros
    
    def getNumeroPlazas(self):
        return self.__numeroPlazas
    
    def getDistanciaRecorrida(self):
        return self.__distanciaRecorrida
    
    def getTarifaBase(self):
        return self.__tarifaBase
    
    def __str__(self):
        return f"Marca: {self.__marca}, Modelo: {self.__modelo}, Año: {self.__anio}, Capacidad de Pasajeros: {self.__capacidadPasajeros}, Número de Plazas: {self.__numeroPlazas}, Distancia Recorrida: {self.__distanciaRecorrida}, Tarifa Base: {self.__tarifaBase}"