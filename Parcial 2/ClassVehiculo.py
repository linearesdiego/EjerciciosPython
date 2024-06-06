import abc
from abc import ABC
class Vehiculo(ABC):
    __marca:str
    __modelo: str
    __año: int
    __capacidad: int
    __plazas: int
    __distRecorrida: float
    __tarifaBase: float
    
    def __init__(self,marca,modelo,año,capacidad,plazas,distRecorrida,tarifaBase):
        self.__marca = marca
        self.__modelo = modelo
        self.__año = año
        self.__capacidad = capacidad
        self.__plazas = plazas
        self.__distRecorrida = distRecorrida
        self.__tarifaBase = tarifaBase
    
    #getters
    def getMarca(self):
        return self.__marca
    def getModelo(self):
        return self.__modelo
    def getAño(self):
        return self.__año
    def getCapacidad(self):
        return self.__capacidad
    def getPlazas(self):
        return self.__plazas
    def getDistRecorrida(self):
        return self.__distRecorrida
    def getTarifaBase(self):
        return self.__tarifaBase
    
    @abc.abstractmethod
    def calcPorcentaje(self):
        pass
    
    def tarifaServicio(self):
        return self.__tarifaBase * self.calcPorcentaje()