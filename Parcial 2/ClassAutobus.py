from ClassVehiculo import Vehiculo

class Autobus(Vehiculo):
    __tipoServicio: str
    __turno: str
    
    def __init__(self,marca,modelo,año,capacidad,plazas,distRecorrida,tarifaBase,tipoServicio,turno):
        super().__init__(marca,modelo,año,capacidad,plazas,distRecorrida,tarifaBase)
        self.__tipoServicio = tipoServicio
        self.__turno = turno
        
    def getTipoServicio(self):
        return self.__tipoServicio
    def getTurno(self):
        return self.__turno
    
    def calcPorcentaje(self):
        if self.__turno == 'noche' and self.__tipoServicio == 'turismo':
            return 1.2
        else :
            return 1.05