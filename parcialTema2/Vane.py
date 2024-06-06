""" De las Vanes: se registra, además, el tipo de carrocería (minivan, van). """

from Vehiculo import Vehiculo

class Vane(Vehiculo):
    __tipoCarroceria = str

    def __init__(self, marca:str, modelo:str, anio:int, capacidadPasajeros:int, numeroPlazas:int, distanciaRecorrida:float, tarifaBase:float, tipoCarroceria:str):
        super().__init__(marca, modelo, anio, capacidadPasajeros, numeroPlazas, distanciaRecorrida, tarifaBase)
        self.__tipoCarroceria = tipoCarroceria

    def getTipoCarroceria(self):
        return self.__tipoCarroceria


    """ Tarifa de Servicios de Vanes: tarifa base, menos el 10% de descuento, si el servicio se realiza en

    una minivan, caso contrario: tarifa base+2.5%. """

    def calcularTarifa(self):
        tarifa = float(super().getTarifaBase())
        if self.__tipoCarroceria == "minivan":
            tarifa -= tarifa * 0.10
        else:
            tarifa += tarifa * 0.025
        return tarifa