import csv
from os import path
from Refrigerados import Refrigerados
from Congelados import Congelados
class GestorProducto:
    __listaProducto = []
    
    def __init__(self):
        self.__listaProducto = []
    
    def agregarProducto(self,producto):
        self.__listaProducto.append(producto)

    def leer_csv(self):
        archivo = open(path.dirname(__file__) + '/productos.csv')
        reader = csv.reader(archivo, delimiter=";")
        reader.__next__()
        for fila in reader:
            if fila[0] == "R":
                producto = Refrigerados(fila[1],fila[2],fila[3],float(fila[4]),fila[5],fila[6],float(fila[7]),fila[8])
            else:
                producto = Congelados(fila[1],fila[2],fila[3],float(fila[4]),fila[5],fila[6],float(fila[7]),(fila[8]),fila[9])
            self.agregarProducto(producto)

    def mostrar(self):
        for producto in self.__listaProducto:
            print(producto)

    
    def obtener(self,posicion):
        actual=self.__listaProducto[posicion]
        if(isinstance(actual,Refrigerados)):
            print(f'Posicion:{posicion} Refrigerado:{actual.getNombreProducto()}')
        elif(isinstance(actual,Congelados)):
            print(f'Posicion:{posicion} Congelado:{actual.getNombreProducto()}')
        else:
            print("No existe la publicacion")

    def contar(self):
        contadorR=0
        contadorC=0
        for producto in self.__listaProducto:
            if(isinstance(producto,Refrigerados)):
                contadorR+=1
            elif(isinstance(producto,Congelados)):
                contadorC+=1
        print(f'Cantidad de productos refrigerados: {contadorR}')
        print(f'Cantidad de productos congelados: {contadorC}')

    def mostrarProductos(self):
        pass


