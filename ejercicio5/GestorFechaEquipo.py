
import csv
from os import path
from FechaEquipo import FechaEquipo
class GestorFechaEquipo:
    def __init__(self):
        self.__fechaEquipo = []
    
    
    def cargarObjeto(self):
        archivo = open(path.dirname(__file__) + '/fechasFutbol.csv')
        reader = csv.reader(archivo, delimiter=";")

        for fila in reader:
            equipo = FechaEquipo(str(fila[0]),int(fila[1]),int(fila[2]),int(fila[3]),int(fila[4]))
            self.__fechaEquipo.append(equipo) 

    def mostrar(self):
        for i in range(len(self.__list)):
            print(self.__list[i])