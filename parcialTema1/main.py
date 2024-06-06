""" Parcial 2 - POO 
Tema 1 30-05-2024
Una Empresa Agroalimentaria se dedica a la venta de dos tipos de productos: productos 
refrigerados y productos congelados.
De todos los productos se registra:
Nombre del producto, fecha de envasado, fecha de vencimiento, temperatura de 
mantenimiento recomendada, país de origen, número de lote, costo base.
De los productos refrigerados: se registra, además: código del organismo de supervisión 
alimentaria.
De los productos congelados: composición del aire con que fue congelado (% de nitrógeno, % 
de oxígeno, % de dióxido de carbono y % de vapor de agua), y el método de congelación (frio
mecánico o frio criogénico).
El importe de venta de cada producto se calcula en función del precio base y de sus 
características.
Para ello se deben considerar las siguientes reglas de negocio:
Importe de venta de un producto refrigerado: el costo base, menos el 10% si la fecha de 
vencimiento es dentro de dos meses (Mes de vencimiento -Mes actual). Caso contrario el 
importe de venta es: precio base+ 1% 
Importe de venta de un producto Congelado: Si el método de congelación es mecánico
el importe de venta es: costo base + 15 %. Si el método de congelación es criogénico. el importe 
de venta es: costo base+ 15%.
El analista de la empresa le solicita a usted que desarrolle una aplicación con las siguientes 
restricciones.
a) Definir la jerarquía de clases con los métodos correspondientes a cada clase de la narrativa 
dada.
b) Crear una clase gestor de productos basado en una lista de python para almacenar cada uno 
de los productos que comercializa la empresa. Los datos de los productos están 
almacenados en un archivo con extensión .csv, denominado “productos.csv”. Cada fila del 
archivo representa un producto, la primera columna de la fila determina el tipo de producto 
(C-Congelado, R-Refrigerado).
c) Implementar un programa principal con un menú de opciones que permita testear las 
siguientes acciones:
1. Agregar productos al gestor de productos.
2. Dada una posición de la lista: Mostrar por pantalla qué tipo de producto se encuentra 
almacenado en dicha posición (usar la función isinstance()).
3. Mostrar la cantidad de productos de cada tipo.
4. Recorrer la colección y mostrar para todos los productos: Nombre, país de origen y 
temperatura de mantenimiento recomendada, e importe de venta.
Nota: 
a) El método que resuelve el item 4, deberá definirlo en la superclase.
b) Está terminantemente prohibido sacar sublistas del gestor de productos para resolver 
alguna funcionalidad solicitada o mostrar datos """

""" 
C;Tocino;10/4/2024;10/4/2025;-17.7;Estados Unidos;AD980;1400;77;20;1;2;mecanico
R;Leche Entera;20/1/2024;23/10/2024;5;Argentina;EF987;1399;AR-D004;;;;
R;Manteca;3/3/2024;8/9/2024;10;Argentina;EC654;1200;AR-G007;;;;
C;Nuggets de Pollo;12/5/2023;12/5/2024;-17.5;Argentina;IJ975;950;75;20;2;3;mecanico
R;Yogurt Natural;5/4/2024;8/6/2024;8;Argentina;AB456;780;AR-A001;;;;
C;Filete de Merluza;10/5/2024;10/7/2024;-15.5;Argentina;AB123;1800;78;20;0;2;mecanico
R;Jamon Serrano;18/4/2024;20/6/2024;2.5;Espania;GH654;1800;AR-E005;;;;
C;Hamburguesas Vegetarianas;11/5/2023;11/5/2024;-16;Argentina;AB579;1050;79;20;0;1;criogenico
R;Queso Cheddar;21/5/2024;10/7/2024;4;Argentina;MN789;1150;AR-H008;;;;
C;Frutos Rojos;3/5/2023;3/5/2024;-15;Argentina;QR813;1250;79;20;0;1;criogenico """
from GestorProducto import GestorProducto
from Congelados import Congelados
from Refrigerados import Refrigerados
def menu():
    print("1. Agregar producto a la colección")
    print("2. Dada una posición de la lista: Mostrar por pantalla qué tipo de vehículo se encuentra almacenado en dicha posición (usar la función isinstance()).")
    print("3. Mostrar la cantidad de vehículos de cada tipo.")
    print("4. Recorrer la colección y mostrar para todos los Vehículos: modelo, año de fabricación, capacidad de pasajeros y la tarifa del servicio.")
    print("5. Salir")
    opcion = int(input("Ingrese una opción: "))
    return opcion


def main():
    GP = GestorProducto()
    GP.leer_csv()
    opcion = menu()
    while opcion != 5:
        if opcion == 1:
            nombre = input('Ingrese el nombre del producto: ')
            fechaEnvasado = input('Ingrese la fecha de envasado: ')
            fechaVencimiento = input('Ingrese la fecha de vencimiento: ')
            temperaturaMantenimiento = float(input('Ingrese la temperatura de mantenimiento: '))
            paisOrigen = input('Ingrese el país de origen: ')
            numeroLote = input('Ingrese el número de lote: ')
            costoBase = float(input('Ingrese el costo base: '))

            tipo = input('Ingrese el tipo del producto (R/C): ')
            if tipo.upper() == 'R':
                codigoOrganismo = input('Ingrese el código del organismo de supervisión alimentaria: ')
                refrigerado = Refrigerados(nombre,fechaEnvasado,fechaVencimiento,temperaturaMantenimiento,paisOrigen,numeroLote,costoBase,codigoOrganismo)
                GP.agregarProducto(refrigerado)
                print('producto refrigerado agregada con exito.')
            elif tipo.upper() == 'C':
                composicionAire = input('Ingrese la composición del aire con que fue congelado: ')
                metodoCongelacion = input('Ingrese el método de congelación: ')
                congelado = Congelados(nombre,fechaEnvasado,fechaVencimiento,temperaturaMantenimiento,paisOrigen,numeroLote,costoBase,composicionAire,metodoCongelacion)
                GP.agregarProducto(congelado)
                print('producto congelado agregado con exito.')
            else:
                print('Tipo de producto incorrecto.')
        elif opcion == 2:
            posicion = int(input("Ingrese la posición: "))
            GP.obtener(posicion)
        elif opcion == 3:
            """ GP.contar()   """
        elif opcion == 4:
           """  GP.mostrarVehiculos() """
        opcion = menu()

if __name__ == "__main__":
    main()

