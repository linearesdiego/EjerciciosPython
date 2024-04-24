from Pedidos import Pedido
import csv

class GestorPedido:
    __list:list[Pedido]
    
    
    def __init__(self):
            self.__list = self.cargarObjeto()

    def cargarObjeto():
        archivo = open('/datosPedidos.csv')
        reader = csv.reader(archivo, delimiter=";")

        for fila in reader:
            pedido = Pedido(fila[0],fila[1],fila[2],fila[3],fila[4],fila[5])
    

    def mostrar(self):
        for i in range(len(self.__list)):
            print(self.__list[i])