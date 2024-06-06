""" De los productos congelados: composición del aire con que fue congelado (% de nitrógeno, % 
de oxígeno, % de dióxido de carbono y % de vapor de agua), y el método de congelación (frio
mecánico o frio criogénico). """

from Producto import Producto

class Congelados(Producto):
    __composicionAire = str
    __metodoCongelacion = str

    def __init__(self, nombreProducto:str, fechaEnvasado:str, fechaVencimiento:str, temperaturaMantenimiento:float, paisOrigen:str, numeroLote:int, costoBase:float, composicionAire:dict, metodoCongelacion:str):
        super().__init__(nombreProducto, fechaEnvasado, fechaVencimiento, temperaturaMantenimiento, paisOrigen, numeroLote, costoBase)
        self.__composicionAire = composicionAire
        self.__metodoCongelacion = metodoCongelacion

    def getComposicionAire(self):
        return self.__composicionAire

    def getMetodoCongelacion(self):
        return self.__metodoCongelacion

    def __str__(self):
        return f"{super().__str__()}, Composición del Aire: {self.__composicionAire}, Método de Congelación: {self.__metodoCongelacion}"

    
    
    def calcularImporteVenta(self):
        resultado = 0
        if self.__metodoCongelacion == "mecanico":
            resultado = super().getCostoBase() + (super().getCostoBase() * 0.15)
        else:
            resultado = super().getCostoBase() + (super().getCostoBase() * 0.15)
        return resultado