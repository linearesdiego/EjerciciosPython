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
        for i in range(len(self.__equipo)):
            print(self.__equipo[i])

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
    
    
    def buscarIdentificador(self, identificador):
        indice=0
        valorDeRetorno = None
        bandera=False
        while not bandera and indice < len(self.__equipo):
            if self.__equipo[indice].getIdentificador() == identificador:
                bandera=True
                valorDeRetorno=self.__equipo[indice]
            else:
                indice+=1
        return valorDeRetorno
    
    def getEquipo(self):
        return self.__equipo
    def ordenarTable(self):
        self.__equipo.sort(reverse=True)
        for i in range(len(self.__equipo)):
            print(self.__equipo[i])
        archivo = open(path.dirname(__file__) + '/tablaPosiciones.csv', 'w')
        writer = csv.writer(archivo, delimiter=";")
        for i in range(len(self.__equipo)):
            writer.writerow([self.__equipo[i].getIdentificador(), self.__equipo[i].getNombre(), self.__equipo[i].getGolesAFavor(), self.__equipo[i].getGolesEnContra(), self.__equipo[i].getDiferenciaGoles(), self.__equipo[i].getPuntos()])
        archivo.close()
        """ c. Leer el nombre de un equipo y obtener un listado con el siguiente formato
        Equipo: xxxxxxxxxxxxxxxx
        Fecha Goles a Favor Goles en Contra Diferencia de Goles Puntos
        xx/xx/xxxx xx xx xx xx
        xx/xx/xxxx xx xx xx xx
        -------------------------------------------------------------------------------------------------------
        Totales: xx xx xx xx """
    def generarLista(self, indice, gestorFechaEquipo):
        df=0 
        dc=0
        dg=0
        p=0
        print("---------------------------------------------------------------------------")
        print("Equipo: ",indice.getNombre())
        print("Fecha\tGoles a favor\tGoles en contra\tDiferencia de goles\tPuntos")
        for fecha in gestorFechaEquipo:
            if fecha.getIdentificadorEquipoLocal() == indice.getIdentificador():
                if fecha.getGolesEquipoLocal() > fecha.getGolesEquipoVisitante():
                    p+=3
                elif fecha.getGolesEquipoLocal() == fecha.getGolesEquipoVisitante():
                    p+=1
                df+=fecha.getGolesEquipoLocal()
                dc+=fecha.getGolesEquipoVisitante()
                dg+=fecha.getGolesEquipoLocal()-fecha.getGolesEquipoVisitante()
                print(fecha.getFecha(),'\t',fecha.getGolesEquipoLocal(),'\t',fecha.getGolesEquipoVisitante(),'\t',fecha.getGolesEquipoLocal()-fecha.getGolesEquipoVisitante(),'\t',p)
            elif fecha.getIdentificadorEquipoVisitante() == indice.getIdentificador():
                if fecha.getGolesEquipoLocal() < fecha.getGolesEquipoVisitante():
                    p+=3
                elif fecha.getGolesEquipoLocal() == fecha.getGolesEquipoVisitante():
                    p+=1
                df+=fecha.getGolesEquipoVisitante()
                dc+=fecha.getGolesEquipoLocal()
                dg+=fecha.getGolesEquipoVisitante()-fecha.getGolesEquipoLocal()
                print(fecha.getFecha(),'\t',fecha.getGolesEquipoVisitante(),'\t',fecha.getGolesEquipoLocal(),'\t',fecha.getGolesEquipoVisitante()-fecha.getGolesEquipoLocal(),'\t',p)


        print("totales: asdasdasdsa")
        print("---------------------------------------------------------------------------")
       
    
        

            