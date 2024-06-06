""" De los productos refrigerados: se registra, además: código del organismo de supervisión 
alimentaria. """
from datetime import datetime
from Producto import Producto

class Refrigerados(Producto):
    __codigoOrganismo = str

    def __init__(self, nombreProducto:str, fechaEnvasado:str, fechaVencimiento:str, temperaturaMantenimiento:float, paisOrigen:str, numeroLote:int, costoBase:float, codigoOrganismo:str):
        super().__init__(nombreProducto, fechaEnvasado, fechaVencimiento, temperaturaMantenimiento, paisOrigen, numeroLote, costoBase)
        self.__codigoOrganismo = codigoOrganismo

    def getCodigoOrganismo(self):
        return self.__codigoOrganismo

    def __str__(self):
        return f"{super().__str__()}, Código del Organismo de Supervisión Alimentaria: {self.__codigoOrganismo}"
    
    def calcularImporteVenta(self): 
        """tengo que usar el datetime para calcular la diferencia de meses , la fecha de vencimiento esta en la superclase"""
        resultado = 0
        fechaVencimiento = datetime.strptime(super().getFechaVencimiento(), "%d/%m/%Y")
        fechaActual = datetime.now()
        diferenciaMeses = fechaVencimiento.month - fechaActual.month
        if diferenciaMeses <= 2:
            resultado= super().getCostoBase() - (super().getCostoBase() * 0.1)
        else:
            resultado= super().getCostoBase() + (super().getCostoBase() * 0.01)

        return resultado

        
        
    