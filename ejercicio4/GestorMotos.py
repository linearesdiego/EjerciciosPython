from Motos import Moto 
import csv
from os import path
class GestorMotos:

    def __init__(self) :
        self.__list = []

    def cargarObjeto(self):
        archivo = open(path.dirname(__file__) + '/datosMotos.csv')
        reader = csv.reader(archivo, delimiter=";")
        
        for fila in reader:
            motos = Moto(fila[0],fila[1],fila[2],fila[3],fila[4])
            self.__list.append(motos)
        

    def mostrar(self):
        for i in range(len(self.__list)):
            print(self.__list[i])

    def buscarMoto(self, patente):
        indice=0
        valorDeRetorno = None
        bandera=False
        while not bandera and indice < len(self.__list):
            if self.__list[indice].getPatente() == patente:
                bandera=True
                valorDeRetorno=self.__list[indice]
            else:
                indice+=1
        return valorDeRetorno
    
  
    