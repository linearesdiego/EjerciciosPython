class FechaEquipo:
    __fecha = str
    __identificadorEquipoLocal = int
    __identificadorEquipoVisitante = int
    __golesEquipoLocal = int
    __golesEquipoVisitante = int

    def __init__(self, fecha, identificadorEquipoLocal, identificadorEquipoVisitante, golesEquipoLocal, golesEquipoVisitante):
        self.__fecha = fecha
        self.__identificadorEquipoLocal = identificadorEquipoLocal
        self.__identificadorEquipoVisitante = identificadorEquipoVisitante
        self.__golesEquipoLocal = golesEquipoLocal
        self.__golesEquipoVisitante = golesEquipoVisitante

    def __str__(self):
        return f'Fecha: {self.__fecha}, Identificador Equipo Local: {self.__identificadorEquipoLocal}, Identificador Equipo Visitante: {self.__identificadorEquipoVisitante}, Goles Equipo Local: {self.__golesEquipoLocal}, Goles Equipo Visitante: {self.__golesEquipoVisitante}'

    def getFecha(self):
        return self.__fecha

    def getIdentificadorEquipoLocal(self):
        return self.__identificadorEquipoLocal

    def getIdentificadorEquipoVisitante(self):
        return self.__identificadorEquipoVisitante

    def getGolesEquipoLocal(self):
        return self.__golesEquipoLocal

    def getGolesEquipoVisitante(self):
        return self.__golesEquipoVisitante

    def setGolesEquipoLocal(self, golesEquipoLocal):
        self.__golesEquipoLocal = golesEquipoLocal

    def setGolesEquipoVisitante(self, golesEquipoVisitante):
        self.__golesEquipoVisitante = golesEquipoVisitante