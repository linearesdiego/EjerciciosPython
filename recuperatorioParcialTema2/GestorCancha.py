from os import path
import csv
from Cancha import Cancha
import numpy as np
class GestorCancha: 
    __listaCancha = np.ndarray
    __dimension = int
    __incremento = int
    __cantidad = int

    def __init__(self):
        self.__dimension = 0
        self.__incremento = 1
        self.__cantidad = 0
        self.__listaCancha = np.empty([0], dtype = Cancha)


    def agregarCancha(self, cancha):
        if self.__dimension == 0:
            self.__dimension += self.__incremento
            self.__listaCancha = np.resize(self.__listaCancha, self.__dimension)
        elif self.__dimension == self.__cantidad:
            self.__dimension += self.__incremento
            self.__listaCancha = np.resize(self.__listaCancha, self.__dimension)
        self.__listaCancha[self.__cantidad] = cancha
        self.__cantidad += 1

    def cargarCancha(self):
        archivo = open(path.dirname(__file__) + '/Canchas.csv')
        reader = csv.reader(archivo, delimiter=";")
        reader.__next__()

        for fila in reader:
            cancha = Cancha(fila[0],fila[1],float(fila[2]))
            self.agregarCancha(cancha)
        archivo.close()


    def getImporte_Hora(self,id):
        """con while sin doble return"""
        i = 0
        while i < len(self.__listaCancha):
            if self.__listaCancha[i].getIdCancha() == id:
                return self.__listaCancha[i].getImporte()
            i += 1