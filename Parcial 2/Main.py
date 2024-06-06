from GestorVehiculos import GestorVehiculos
from ClassVan import Van
from ClassAutobus import Autobus

def test():
    gesVehiculos = GestorVehiculos()
    gesVehiculos.leerVehiculos_desde_csv()
    
    op = None
    while op != '5':
        print('1. Agregar un nuevo vehiculo.')
        print('2. Mostrar que tipo de vehiculo hay en determinada posicion.')
        print('3. Mostrar la cantidad de vehiculos de cada tipo.')
        print('4. Mostrar todos los vehiculos')
        op = input('>>>> ')
        
        if op == '1':
            marca = input('Ingrese la marca del vehiculo que desea agregar: ')
            modelo = input('Ingrese el modelo: ')
            año = int(input('Ingrese el año: '))
            capacidad = int(input('Ingrese la capacidad: '))
            plazas = int(input('Ingrese las plazas: '))
            distRecorrida = float(input('Ingrese la distancia recorrida: '))
            tarifaBase = float(input('Ingrese la tarifa base: '))
            tipo = input('Ingrese el tipo del vehiculo (V/A): ')
            if tipo.upper() == 'V':
                tipoCarroceria = input('Ingrese el tipo de carroceria: ')
                newVan = Van(marca,modelo,año,capacidad,plazas,distRecorrida,tarifaBase,tipoCarroceria)
                gesVehiculos.agregarVehiculo(newVan)
                print('Van agregada con exito.')
            elif tipo.upper() == 'A':
                tipoServicio = input('Ingrese el tipo de servicio: ')
                turno = input('Ingrese el turno: ')
                newAutobus = Autobus(marca,modelo,año,capacidad,plazas,distRecorrida,tarifaBase,tipoServicio,turno)
                gesVehiculos.agregarVehiculo(newAutobus)
                print('Autobus agregado con exito.')
            else:
                print('Tipo de vehiculo incorrecto.')
        
        elif op == '2':
            pos = int(input('Ingrese la posicion que desea ver: '))
            pos -= 1
            gesVehiculos.verPosicion(pos)

        elif op == '3':
            gesVehiculos.mostrarCantTipo()
            
        elif op == '4':
            gesVehiculos.mostrarTodos()
            
        elif op == '5':
            pass
        
        else:
            print('Opcion no valida')            

if __name__ == '__main__':
    test()