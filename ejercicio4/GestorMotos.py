from Motos import Motos 
import csv
class GestorMotos:

    def __init__(self) :
        self.__list = []

    def cargarObjeto(self):
        archivo = open('datosMotos.csv')
        reader = csv.reader(archivo, delimiter=";")

        for fila in reader:
            motos = Motos(fila[0],fila[1],fila[2],fila[3],fila[4])
            self.__list.append(motos)
        

    def mostrar(self):
        for i in range(len(self.__list)):
            print(self.__list[i])