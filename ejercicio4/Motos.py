
class Motos:
    __patente = str
    __marca = str
    __nombre = str
    __apellido = str
    __kilometraje = float
    def __init__(self, patente, marca, nombre, apellido, kilometraje):
        self.__patente = patente
        self.__marca = marca
        self.__nombre = nombre
        self.__apellido = apellido
        self.__kilometraje = kilometraje

    def __str__(self):
        return f'Patente: {self.__patente}, Marca: {self.__marca}, Nombre: {self.__nombre}, Apellido: {self.__apellido}, Kilometraje: {self.__kilometraje}'
    


