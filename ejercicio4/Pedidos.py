class Pedido:
    __patente = str
    __idPedido = int
    __comidas = str
    __tiempoEstimado = int
    __tiempoReal = int
    __precio = float
    def __init__(self, patente, idPedido, comidas, tiempoEstimado, tiempoReal, precio):
        self.__patente = patente
        self.__idPedido = idPedido
        self.__comidas = comidas
        self.__tiempoEstimado = tiempoEstimado
        self.__tiempoReal = tiempoReal
        self.__precio = precio

    def __str__(self):
        return f'Patente: {self.__patente}, ID Pedido: {self.__idPedido}, Comidas: {self.__comidas}, Tiempo Estimado: {self.__tiempoEstimado}, Tiempo Real: {self.__tiempoReal}, Precio: {self.__precio}'
   
    def setTiempoReal(self, tiempoReal):        
        self.__tiempoReal = tiempoReal

    def getIdPedido(self):
        return self.__idPedido
    def getPrecio(self):
        return self.__precio
    def getTiempoReal(self):
        return self.__tiempoReal
    def getTiempoEstimado(self):
        return self.__tiempoEstimado
    def getComidas(self):
        return self.__comidas
    def getPatente(self):
        return self.__patente
    def getTiempoReal(self):
        return self.__tiempoReal
    
    def __lt__(self, otro):
        return self.__patente < otro.__patente