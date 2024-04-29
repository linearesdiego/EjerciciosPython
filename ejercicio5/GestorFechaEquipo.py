
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
            equipo = FechaEquipo(fila[0],fila[1],fila[2],fila[3],fila[4])
            self.__fechaEquipo.append(equipo) 

    def mostrar(self):
        for i in range(len(self.__fechaEquipo)):
            print(self.__fechaEquipo[i])