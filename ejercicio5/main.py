""" Ejercicio 5
La Liguilla de Rawson lo contrata a usted como programador para desarrollar un sistema que
actualice y mantener los datos de la tabla de posiciones.
De cada Equipo se registran: identificador del equipo, nombre del equipo, goles a favor, goles en
contra, diferencia de goles, y puntos
De cada Fecha de fútbol se registran: fecha del partido, identificador de equipo local, identificador
de equipo visitante, cantidad de goles que hizo el equipo local, cantidad de goles que hizo el equipo
visitante.
La aplicación que debe desarrollar se debe ajustar a los siguientes requerimientos:
1. Crear una clase Equipo, con los atributos identificados y los métodos necesarios para
resolver la problemática planteada
2. Crear una clase Fecha de Fútbol, con los atributos identificados y los métodos necesarios
para resolver la problemática planteada.
3. Crear un Gestor de Equipos, basado en lista Python, que permita almacenar los datos de los
Equipos de fútbol que intervienen en el torneo. Los datos de los equipos están almacenados
en un archivo .csv, denominado “equipos2024.csv”.
4. Crear un Gestor de Fechas de Fútbol, que permita almacenar los datos de las Fechas de
fútbol que se han disputado. Los datos de los partidos disputados y los resultados obtenidos,
están almacenados en un archivo .csv, denominado “fechasFutbol.csv”.
5. Crear un menú de opciones que permita:
a. Leer los datos de los equipos del archivo y almacenarlos en el Gestor de Equipos.
b. Leer los datos de las Fechas de Fútbol, y almacenarlos en el Gestor de Fechas.
c. Leer el nombre de un equipo y obtener un listado con el siguiente formato
Equipo: xxxxxxxxxxxxxxxx
Fecha Goles a Favor Goles en Contra Diferencia de Goles Puntos
xx/xx/xxxx xx xx xx xx
xx/xx/xxxx xx xx xx xx
-------------------------------------------------------------------------------------------------------
Totales: xx xx xx xx
d. Actualizar la tabla de todos los equipos, con los resultados de las fechas disputadas.
e. Ordenar la tabla de posiciones de mayor a menor, para ello deberá sobrecargar el
operador mayor que (__gt__), bajo el siguiente criterio:
a. Si los puntos de dos equipos son iguales, se debe verificar la diferencia de goles,
si la diferencia de goles entre ambos equipos es igual, se debe verificar la
cantidad de goles a favor.
f. Almacenar la tabla de posiciones ordenada en el punto anterior en un archivo .csv.
Reglas de negocio:
El empate, otorga un punto a cada equipo, la victoria otorga tres puntos al equipo ganador y 0
puntos al equipo perdedor.
Por cada partido disputado, hay una fila en el archivo “fechasFutbol.csv”, cada fila tiene el
identificador de los equipos que disputaron el partido y la cantidad de goles que marcó cada equipo,
si la cantidad de goles es igual hubo empate, sino hubo un ganador, que es el equipo que hizo más
goles.
Proveer donde crea conveniente, los destructores que permitan liberar memoria.  """

from GestorEquipo import GestorEquipo
from GestorFechaEquipo import GestorFechaEquipo



if __name__ == '__main__':

    gestorEquipo = GestorEquipo()
    gestorFechaEquipo = GestorFechaEquipo()

    gestorFechaEquipo.cargarObjeto()
    gestorEquipo.cargarObjeto()
    
    while True:

 
        print("c. Leer el nombre de un equipo y obtener un listado \n")
        print("d. Actualizar la tabla de todos los equipos, con los resultados de las fechas disputadas. \n")
        print("e. Ordenar la tabla de posiciones de mayor a menor \n")
        print("f. Almacenar la tabla de posiciones ordenada en un archivo .csv. \n")
        print("g. Salir")

        opcion= input("Seleccione una opcion \n")
        if opcion== 'c':
            """  Equipo: xxxxxxxxxxxxxxxx
                Fecha Goles a Favor Goles en Contra Diferencia de Goles Puntos
                xx/xx/xxxx xx xx xx xx
                xx/xx/xxxx xx xx xx xx
                -------------------------------------------------------------------------------------------------------
                Totales: xx xx xx xx """
            nombre = input("Ingrese el nombre del equipo \n")
            indice= gestorEquipo.buscarNombre(nombre)
            if indice != None:
                pass
            else:
                print("no se encontro")
        if opcion== 'd':
            print("Tabla actualizada")

        if opcion== 'e':
            print("Tabla ordenada")
        if opcion== 'f':
            print("Tabla almacenada")
        if opcion== 'g':
            break
