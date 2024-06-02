class Alquiler: 
    __nombre= str
    __idCancha= str
    __hora= str
    __minutos= int
    __duracion= int

    def __init__(self, nombre, idCancha, hora, minutos, duracion):
        self.__nombre= nombre
        self.__idCancha= idCancha
        self.__hora= hora
        self.__minutos= minutos
        self.__duracion= duracion

    def __gt__(self, otro):
        if self.__hora > otro.__hora:
            return True
        elif self.__hora == otro.__hora:
            if self.__minutos > otro.__minutos:
                return True
            else:
                return False
        else:
            return False

    def __str__(self):
        return f"{self.hora}:{self.minutos} {self.idCancha} {self.duracion} {self.nombre}"

    def getDuracion(self):
        return self.__duracion

    def getIdCancha(self):
        return self.__idCancha
    def getNombre(self):
        return self.__nombre
    def getHora(self):
        return self.__hora
    def getMinutos(self):
        return self.__minutos
    
