""" De los Autobuses: se registra, además, el tipo de servicio (interurbano, turismo, etc) y turno en 
el que se brindó el servicio (mañana, tarde, noche). """
from Vehiculo import Vehiculo
class Autobus(Vehiculo):
    __tipoServicio = str
    __turno = str

    def __init__(self, marca:str, modelo:str, anio:int, capacidadPasajeros:int, numeroPlazas:int, distanciaRecorrida:float, tarifaBase:float, tipoServicio:str, turno:str):
        super().__init__(marca, modelo, anio, capacidadPasajeros, numeroPlazas, distanciaRecorrida, tarifaBase)
        self.__tipoServicio = tipoServicio
        self.__turno = turno

    def getTipoServicio(self):
        return self.__tipoServicio
    
    def getTurno(self):
        return self.__turno
    

    """ Tarifa de Servicio de Autobuses: tarifa base, más un recargo el 20%, si el servicio se realiza en 
    horario nocturno y es de tipo turismo, caso contrario: tarifa base + 5% """

    def calcularTarifa(self):
        tarifa = float(super().getTarifaBase())
        if self.__turno == "noche" and self.__tipoServicio == "turismo":
            tarifa += tarifa * 0.20
        else:
            tarifa += tarifa * 0.05
        return tarifa
    
    def __str__(self):
        return f"{super().__str__()}, Tipo de Servicio: {self.__tipoServicio}, Turno: {self.__turno}"
