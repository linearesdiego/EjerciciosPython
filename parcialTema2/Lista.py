from Nodo import Nodo
import csv
from os import path

from Autobus import Autobus
from Vane import Vane
class Lista:

    def __init__(self):
        self.__comienzo = None


    def leer_csv(self):
        archivo = open(path.dirname(__file__) + '/vehiculos.csv')
        reader = csv.reader(archivo, delimiter=";")
        reader.__next__()
        for fila in reader:
            if fila[0] == "A":
                vehiculo = Autobus(fila[1],fila[2],fila[3],fila[4],int(fila[5]),float(fila[6]),float(fila[7]),fila[8],fila[9])
            else:
                vehiculo = Vane(fila[1],fila[2],fila[3],fila[4],fila[5],fila[6],fila[7],fila[8])
            self.agregar(vehiculo)

    def agregar(self, vehiculo):
        nodo = Nodo(vehiculo)
        if self.__comienzo == None:
            self.__comienzo = nodo
        else:
            aux = self.__comienzo
            while aux.getSiguiente() != None:
                aux = aux.getSiguiente()
            aux.setSiguiente(nodo)

    def mostrar(self):
        aux = self.__comienzo
        while aux != None:
            print(aux.getDato())
            aux = aux.getSiguiente()
    
    def obtener(self,posicion):
        actual=self.__comienzo
        i=0
        while actual != None:
            if i==posicion:
                if(isinstance(actual.getDato(),Autobus)):
                    print(f'Posicion:{posicion}Autobus:{actual.getDato().getMarca()}')
                elif(isinstance(actual.getDato(),Vane)):
                    print(f'Posicion:{posicion}Vane:{actual.getDato().getMarca()}')
                return
            actual=actual.getSiguiente()
            i+=1
        print("No existe la publicacion")


    def contar(self):
        actual=self.__comienzo
        contadorA=0
        contadorV=0
        while actual != None:
            if(isinstance(actual.getDato(),Autobus)):
                contadorA+=1
            elif(isinstance(actual.getDato(),Vane)):
                contadorV+=1
            actual=actual.getSiguiente()
        print(f'Cantidad de Autobuses:{contadorA}')
        print(f'Cantidad de Vanes:{contadorV}')

    def mostrarVehiculos(self):
        actual=self.__comienzo
        while actual != None:
            print(f'Modelo:{actual.getDato().getModelo()}')
            print(f'Año de fabricacion:{actual.getDato().getAnio()}')
            print(f'Capacidad de pasajeros:{actual.getDato().getCapacidadPasajeros()}')
            print(f'Tarifa del servicio:{actual.getDato().calcularTarifa()}')
            actual=actual.getSiguiente()

    