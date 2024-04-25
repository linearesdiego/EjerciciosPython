from Pedidos import Pedido
import csv
from os import path


class GestorPedido:
    
    
    def __init__(self):
            self.__list =[]

    def cargarObjeto(self):
        archivo = open(path.dirname(__file__) + '/datosPedidos.csv')
        reader = csv.reader(archivo, delimiter=";")

        for fila in reader:
            pedido = Pedido(fila[0],fila[1],fila[2],fila[3],fila[4],fila[5])
            self.__list.append(pedido) 
    

    def mostrar(self):
        for i in range(len(self.__list)):
            print(self.__list[i])


    def asignarPedido(self, patente, idPedido, comida, tiempoEstimado, tiempoReal, precio):
        
        with open(path.dirname(__file__) + '/datosPedidos.csv', 'a', newline='') as archivo:
            writer = csv.writer(archivo, delimiter=";")
            writer.writerow([patente, idPedido, comida, tiempoEstimado, tiempoReal, precio])
        print("Pedido asignado")

    def modificarTiempoReal(self, patente, idPedido, tiempoReal):
        indice = self.buscarPedido(patente, idPedido)
        if indice != None:
            self.__list[indice].setTiempoReal(tiempoReal)
            print("Tiempo real modificado")
        else:
            print("No se encontro el pedido")

    def buscarPedido(self, patente, idPedido):
        indice=0
        valorDeRetorno = None
        bandera=False
        while not bandera and indice < len(self.__list):
            if self.__list[indice].getPatente() == patente and self.__list[indice].getIdPedido() == idPedido:
                bandera=True
                valorDeRetorno=indice
            else:
                indice+=1
        return valorDeRetorno
        