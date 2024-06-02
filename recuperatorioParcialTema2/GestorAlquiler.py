import csv 
from os import path
from Alquiler import Alquiler
class GestorAlquiler:
    __lista = [] 

    def __init__(self):
        self.__lista = []

    def cargarAlquiler(self):
        archivo = open(path.dirname(__file__) + '/Alquiler.csv')
        reader = csv.reader(archivo, delimiter=";")
        reader.__next__()
        for fila in reader:
            alquiler = Alquiler(fila[0],fila[1],fila[2],int(fila[3]),int(fila[4]))
            self.__lista.append(alquiler)

    def getLista(self):
        return self.__lista
        
    def listar_reservas(self, GC):
        self.__lista=sorted(self.__lista,reverse=True)        
        print("Hora\tId de Cancha\tDuración alquiler\tImporte por hora\tImporte alquiler")
        i=0
        total = 0
        while i < len(self.__lista):
            duracion = self.__lista[i].getDuracion()
            importe_hora = GC.getImporte_Hora(self.__lista[i].getIdCancha())
            importe_alquiler = importe_hora * (duracion / 60)
            print(f"{self.__lista[i].getHora()}:{self.__lista[i].getMinutos()}\t{self.__lista[i].getIdCancha()}\t{duracion}\t{importe_hora}\t{importe_alquiler}")
            i+= 1
            total += importe_alquiler
        print(f"Total recaudado: {total}")

    def alquiler_total(self):
        id_cancha = input("Ingrese el id de la cancha: ")
        total_minutos = 0
        for alquiler in self.__lista:
            if alquiler.getIdCancha() == id_cancha:
                total_minutos += alquiler.getDuracion()
        print(f"La cancha {id_cancha} fue alquilada {total_minutos} minutos")

