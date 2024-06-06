""" Nombre del producto, fecha de envasado, fecha de vencimiento, temperatura de 
mantenimiento recomendada, país de origen, número de lote, costo base.
alimentaria. """
import abc 
class Producto(abc.ABC):
    __nombreProducto = str
    __fechaEnvasado = str
    __fechaVencimiento = str
    __temperaturaMantenimiento = float
    __paisOrigen = str
    __numeroLote = str
    __costoBase = float

    def __init__(self, nombreProducto:str, fechaEnvasado:str, fechaVencimiento:str, temperaturaMantenimiento:float, paisOrigen:str, numeroLote:int, costoBase:float):
        self.__nombreProducto = nombreProducto
        self.__fechaEnvasado = fechaEnvasado
        self.__fechaVencimiento = fechaVencimiento
        self.__temperaturaMantenimiento = temperaturaMantenimiento
        self.__paisOrigen = paisOrigen
        self.__numeroLote = numeroLote
        self.__costoBase = costoBase
    
    def getNombreProducto(self):
        return self.__nombreProducto
    
    def getFechaEnvasado(self):
        return self.__fechaEnvasado
    
    def getFechaVencimiento(self):
        return self.__fechaVencimiento
    
    def getTemperaturaMantenimiento(self):
        return self.__temperaturaMantenimiento
    
    def getPaisOrigen(self):
        return self.__paisOrigen
    
    def getNumeroLote(self):
        return self.__numeroLote
    
    def getCostoBase(self):
        return self.__costoBase
    
    def __str__(self):
        return f"Nombre del Producto: {self.__nombreProducto}, Fecha de Envasado: {self.__fechaEnvasado}, Fecha de Vencimiento: {self.__fechaVencimiento}, Temperatura de Mantenimiento: {self.__temperaturaMantenimiento}, País de Origen: {self.__paisOrigen}, Número de Lote: {self.__numeroLote}, Costo Base: {self.__costoBase}"

    """     El importe de venta de cada producto se calcula en función del precio base y de sus 
    características.
    Para ello se deben considerar las siguientes reglas de negocio:
    Importe de venta de un producto refrigerado: el costo base, menos el 10% si la fecha de 
    vencimiento es dentro de dos meses (Mes de vencimiento -Mes actual). Caso contrario el 
    importe de venta es: precio base+ 1%  """

    @abc.abstractmethod
    def calcularImporteVenta(self):
        pass

    



    