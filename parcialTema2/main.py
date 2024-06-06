""" arcial 2 - POO 
Tema 2 30-05-2024
En una empresa de servicios de transporte, se manejan diferentes tipos de vehículos para el 
traslado de pasajeros. Estos vehículos se clasifican en dos categorías principales: autobuses y 
vanes.
De todos los vehículos se registra: marca, modelo, año de fabricación, capacidad de pasajeros,
número de plazas, distancia recorrida y tarifa base. 
De los Autobuses: se registra, además, el tipo de servicio (interurbano, turismo, etc) y turno en 
el que se brindó el servicio (mañana, tarde, noche).
De las Vanes: se registra, además, el tipo de carrocería (minivan, van).
La tarifa de cada servicio de transporte, se calcula en función de la tarifa base y de sus 
características: 
Tarifa de Servicio de Autobuses: tarifa base, más un recargo el 20%, si el servicio se realiza en 
horario nocturno y es de tipo turismo, caso contrario: tarifa base + 5%
Tarifa de Servicios de Vanes: tarifa base, menos el 10% de descuento, si el servicio se realiza en 
una minivan, caso contrario: tarifa base+2.5%.
El analista de la empresa le solicita a usted que desarrolle una aplicación con las siguientes 
restricciones.
a) Definir la jerarquía de clases con los métodos correspondientes a cada clase de la narrativa 
dada.
b) Crear una clase gestor de vehículos basado en una lista de python para almacenar cada uno 
de los vehículos que ofrecen servicios de trasporte. Los datos de los vehículos están 
almacenados en un archivo con extensión .csv, denominado “vehiculos.csv”. Cada fila del 
archivo representa un vehículo, la primera columna de la fila determina el tipo de vehículo 
(A-Autobús, V-Van).
c) Implementar un programa principal con un menú de opciones que permita testear las 
siguientes acciones:
1. Agregar vehículos a la colección
2. Dada una posición de la lista: Mostrar por pantalla qué tipo de vehículo se encuentra 
almacenado en dicha posición (usar la función isinstance()).
3. Mostrar la cantidad de vehículos de cada tipo.
4. Recorrer la colección y mostrar para todos los Vehículos: modelo, año de fabricación, 
capacidad de pasajeros y la tarifa del servicio. 
Nota:
a) El método que resuelve el item 4, deberá definirlo en la superclase.
b) Está terminantemente prohibido sacar sublistas del gestor de productos para resolver 
alguna funcionalidad solicitada o mostrar datos. """

""" tipo;marca;modelo;aniofabri;cappasaj;nroplazas;distancia;tarifabase;tiposerv;turno
A;Mercedes-Benz;OC 500;2022;66;11;250.135;360000;turismo;ma�ana
V;Hyundai;Staria;2023;10;7;110.400;120000;minivan;
A;Scania;K400;2020;58;10;195.900;320000;interurbano;tarde
V;Toyota;Hiace;2023;8;7;130.500;125000;minivan;
V;Mercedes-Benz;Sprinter;2024;18;7;130;150000;van;
A;Scania;K360;2019;58;10;155.360;320000;interurbano;noche
A;Mercedes-Benz;OF 1721;2021;60;9;130;340000;turismo;noche
V;Ford;Transit;2023;16;8;125.550;160000;van;
V;Kia;Carnival;2024;10;9;144.600;118000;minivan;
A;Volvo;Piso elevado 15 Mts;2024;58;10;250.800;330000;turismo;ma�ana """

from Lista import Lista

def menu():
    print("1. Agregar vehículos a la colección")
    print("2. Dada una posición de la lista: Mostrar por pantalla qué tipo de vehículo se encuentra almacenado en dicha posición (usar la función isinstance()).")
    print("3. Mostrar la cantidad de vehículos de cada tipo.")
    print("4. Recorrer la colección y mostrar para todos los Vehículos: modelo, año de fabricación, capacidad de pasajeros y la tarifa del servicio.")
    print("5. Salir")
    opcion = int(input("Ingrese una opción: "))
    return opcion

def main():
    lista = Lista()
    lista.leer_csv()
    opcion = menu()
    while opcion != 5:
        if opcion == 1:
            lista.mostrar()
        elif opcion == 2:
            posicion = int(input("Ingrese la posición: "))
            lista.obtener(posicion)
        elif opcion == 3:
            lista.contar()  
        elif opcion == 4:
            lista.mostrarVehiculos()
        opcion = menu()

if __name__ == "__main__":
    main()

