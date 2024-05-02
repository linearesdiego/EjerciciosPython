class Evaluacion:
    __dniPatinador = str
    __estilo = str
    __valoracion = [int, int, int]

    def __init__(self, dniPatinador, estilo, valoracion):
        self.__dniPatinador = dniPatinador
        self.__estilo = estilo
        self.__valoracion = valoracion
    def __str__(self) -> str:
        return f"{self.__dniPatinador}, {self.__estilo}, {self.__valoracion}"
    

    def getDniPatinador(self):
        return self.__dniPatinador
    def getEstilo(self):
        return self.__estilo
    def getValoracion(self):
        return self.__valoracion
    
    def setDniPatinador(self, dniPatinador):
        self.__dniPatinador = dniPatinador
    def setEstilo(self, estilo):
        self.__estilo = estilo
    def setValoracion(self, valoracion):
        self.__valoracion = valoracion
   
    

