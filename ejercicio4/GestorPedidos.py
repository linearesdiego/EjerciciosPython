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
            pedido = Pedido(fila[0],fila[1],fila[2],int(fila[3]),int(fila[4]),float(fila[5]))
            self.__list.append(pedido) 
    

    def mostrarObjeto(self):
        for i in range(len(self.__list)):
            print(self.__list[i])


    def asignarPedido(self, patente, idPedido, comida, tiempoEstimado, tiempoReal, precio):
        pedido = Pedido(patente,idPedido,comida,tiempoEstimado,tiempoReal,precio)
        self.__list.append(pedido)
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
    
    def tiempoPromedioReal(self, patente):
        suma = 0
        cantidad = 0
        for i in range(len(self.__list)):
            if self.__list[i].getPatente() == patente:
                suma += self.__list[i].getTiempoReal()
                cantidad += 1
        return suma/cantidad
        
    def generarListado(self):
        for i in range(len(self.__list)):
            print(f'Patente de Moto: {self.__list[i].getPatente()}')
            print(f'Conductor: {self.__list[i].getPatente()}')
            print(f'Identificador de pedido: {self.__list[i].getIdPedido()}')
            print(f'Tiempo estimado: {self.__list[i].getTiempoEstimado()}')
            print(f'Tiempo real: {self.__list[i].getTiempoReal()}')
            print(f'Precio: {self.__list[i].getPrecio()}')
            print(f'Total: {self.__list[i].getPrecio()}')
            print(f'Comisión: {float(self.__list[i].getPrecio()) * 0.2}')
            print("----------------------------------------------------")
    
        """ Ordenar de menor a mayor el Gestor de pedidos por número de patente, de modo que permita resolver eficientemente las búsquedas. Pare ello debe sobrecargar el operador < """
    def ordenar(self):
        self.__list.sort()
        print("Lista ordenada")
        