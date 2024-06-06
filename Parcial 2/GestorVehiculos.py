from ClassVehiculo import Vehiculo
from ClassAutobus import Autobus
from ClassVan import Van
from csv import reader

class GestorVehiculos:
    __listaVehiculos = []
    
    def __init__(self):
        self.__listaVehiculos = []
    
    def agregarVehiculo(self,vehiculo):
        self.__listaVehiculos.append(vehiculo)
        
    def leerVehiculos_desde_csv(self):
        encabezado = True
        with open('vehiculos.csv', newline='') as file:
            lector = reader(file, delimiter=';')
            for row in lector:
                if encabezado is True:
                    encabezado = False
                    continue
                if row[0] == 'V':
                    marca = row[1]
                    modelo = row[2]
                    año = row[3]
                    capacidad = row[4]
                    plazas = row[5]
                    distRecorrida = row[6]
                    tarifaBase = row[7]
                    tipoCarroceria = row[8]
                    newVan = Van(marca,modelo,int(año),int(capacidad),int(plazas),float(distRecorrida),float(tarifaBase),tipoCarroceria)
                    self.agregarVehiculo(newVan)
                else:
                    marca = row[1]
                    modelo = row[2]
                    año = row[3]
                    capacidad = row[4]
                    plazas = row[5]
                    distRecorrida = row[6]
                    tarifaBase = row[7]
                    tipoServicio = row[8]
                    turno = row[9]
                    newAutobus = Autobus(marca,modelo,int(año),int(capacidad),int(plazas),float(distRecorrida),float(tarifaBase),tipoServicio,turno)
                    self.agregarVehiculo(newAutobus)
    
    def verPosicion(self,pos):
        if isinstance(self.__listaVehiculos[pos], Autobus):
            print(f"En la poscion N°{pos+1}, hay un autobus")
        else:
            print(f"En la poscion N°{pos+1}, hay una van")
            
    def mostrarCantTipo(self):
        autobuses = 0
        vanes = 0
        for vehiculo in self.__listaVehiculos:
            if isinstance(vehiculo,Autobus):
                autobuses += 1
            else:
                vanes += 1
        print(f"Hay {vanes} vehiculos de tipo van en total")
        print(f"Hay {autobuses} vehiculos de tipo autobus en total")
    
    def mostrarTodos(self):
        for vehiculo in self.__listaVehiculos:
            print(f'Modelo: {vehiculo.getModelo()} - Año de fabricacion: {vehiculo.getAño()} - Capacidad: {vehiculo.getCapacidad()} pasajeros - Tarifa de servicio: ${vehiculo.tarifaServicio()}')