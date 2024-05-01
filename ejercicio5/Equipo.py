class Equipo:
    __identificador = int
    __nombre = str
    __golesAFavor = int
    __golesEnContra = int
    __diferenciaGoles = int
    __puntos = int

    def __init__(self, identificador, nombre, golesAFavor, golesEnContra, diferenciaGoles, puntos):
        self.__identificador = identificador
        self.__nombre = nombre
        self.__golesAFavor = golesAFavor
        self.__golesEnContra = golesEnContra
        self.__diferenciaGoles = diferenciaGoles
        self.__puntos = puntos

    def __str__(self):
        return f'Equipo: {self.__nombre}, Fecha: {self.__identificador}, Goles a Favor: {self.__golesAFavor}, Goles en Contra: {self.__golesEnContra}, Diferencia de Goles: {self.__diferenciaGoles}, Puntos: {self.__puntos}'

    def getIdentificador(self):
        return self.__identificador

    def getNombre(self):
        return self.__nombre

    def getGolesAFavor(self):
        return self.__golesAFavor

    def getGolesEnContra(self):
        return self.__golesEnContra

    def getDiferenciaGoles(self):
        return self.__diferenciaGoles

    def getPuntos(self):
        return self.__puntos

    def setGolesAFavor(self, golesAFavor):
        self.__golesAFavor = golesAFavor

    def setGolesEnContra(self, golesEnContra):
        self.__golesEnContra = golesEnContra

    def setDiferenciaGoles(self, diferenciaGoles):
        self.__diferenciaGoles = diferenciaGoles

    def setPuntos(self, puntos):
        self.__puntos = puntos

   
    def __gt__(self, otro):
        if self.__puntos == otro.getPuntos():
            if self.__diferenciaGoles == otro.getDiferenciaGoles():
                return self.__golesAFavor > otro.getGolesAFavor()
            return self.__diferenciaGoles > otro.getDiferenciaGoles()
        return self.__puntos > otro.getPuntos()