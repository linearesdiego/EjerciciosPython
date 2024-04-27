import csv
from os import path
from Equipo import Equipo

class GestorEquipo:
    def __init__(self):
        self.__equipo = []

    def cargarObjeto(self):
        archivo = open(path.dirname(__file__) + '/equipos2024.csv')
        reader = csv.reader(archivo, delimiter=";")

        for fila in reader:
            equipo = Equipo(int(fila[0]),fila[1],int(fila[2]),int(fila[3]),int(fila[4]),int(fila[5]))
            self.__equipo.append(equipo) 

    def mostrar(self):
        for i in range(len(self.__list)):
            print(self.__list[i])

    def buscarNombre(self, nombre):
        indice=0
        valorDeRetorno = None
        bandera=False
        while not bandera and indice < len(self.__equipo):
            if self.__equipo[indice].getNombre() == nombre:
                bandera=True
                valorDeRetorno=self.__equipo[indice]
            else:
                indice+=1
        return valorDeRetorno
    
    def generarListador(self):
        pass
            
    def __gt__(self, other):
        if self.__puntos == other.__puntos:
            if self.__diferenciaGoles == other.__diferenciaGoles:
                if self.__golesAFavor == other.__golesAFavor:
                    return True
                else:
                    return self.__golesAFavor > other.__golesAFavor
            else:
                return self.__diferenciaGoles > other.__diferenciaGoles
        else:
            return self.__puntos > other.__puntos