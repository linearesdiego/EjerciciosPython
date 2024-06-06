from ClassVehiculo import Vehiculo

class Van(Vehiculo):
    __tipoCarroceria: str
    
    def __init__(self,marca,modelo,año,capacidad,plazas,distRecorrida,tarifaBase,tipoCarroceria):
        super().__init__(marca,modelo,año,capacidad,plazas,distRecorrida,tarifaBase)
        self.__tipoCarroceria = tipoCarroceria
        
    def getTipoCarroceria(self):
        return self.__tipoCarroceria
    
    def calcPorcentaje(self):
        if self.__tipoCarroceria == 'minivan':
            return 0.9
        else:
            return 1.025