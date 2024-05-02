from Evaluacion import Evaluacion
import csv
from os import path
class GestorEvaluacion:
    __listaEvaluaciones = []

    def __init__(self):
        self.__listaEvaluaciones = []
    
    def cargarArchivo(self):
        archivo = open(path.dirname(__file__) + '/evaluacion.csv')
        reader = csv.reader(archivo, delimiter=";")

        for fila in reader:
            evaluacion = Evaluacion(fila[0],fila[1],int(fila[2]))
            self.__listaEvaluaciones.append(evaluacion) 

    def mostrar(self):
        for i in range(len(self.__listaEvaluaciones)):
            print(self.__listaEvaluaciones[i])
    
    def getListaEvaluaciones(self):
        return self.__listaEvaluaciones