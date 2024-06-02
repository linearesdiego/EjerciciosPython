""" Cada Cancha: identificador, tipo de piso, importe por hora.
 """
class Cancha:
    __id_cancha = str 
    __tipo = str
    __importe = float

    def __init__(self, id_cancha, tipo, precio_hora):
        self.__id_cancha = id_cancha
        self.__tipo = tipo
        self.__importe = precio_hora

    def __str__(self):
        return f"{self.id_cancha} {self.tipo} {self.iluminacion} {self.precio_hora}"
    
    def getIdCancha(self):
        return self.__id_cancha
    def getTipo(self):
        return self.__tipo
    def getImporte(self):
        return self.__importe
    