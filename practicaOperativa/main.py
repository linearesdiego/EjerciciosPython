""" Tema 1 – Práctico Unidad 2
Fecha: 08/05/2023
La Federación sanjuanina de patín ha organizado un campeonato provincial de patinaje
artístico. En el archivo “federados.csv” están registrados todos los patinadores federados, el
cual contiene los siguientes datos de cada patinador: apellido, nombre, DNI, edad, club al
que representa.
En el archivo “evaluacion.csv” se registraron los datos de la evaluación de cada
presentación en el campeonato, estos datos son: DNI del patinador, estilo de la
presentación (‘L’-libre, ‘E’-escuela) y la valoración dada por cada uno de los 3 jueces que
evalúan la presentación, (puntaje 1, puntaje 2, puntaje 3). Un mismo patinador puede
participar en los dos estilos (libre y escuela), pero en un estilo, un patinador se presenta una
vez.
Nota: Los archivos no presentan ningún orden en particular, y el separador utilizado es el “;”.
El analista de sistemas de la Federación le solicita a usted un programa en Python, para
procesar ambos archivos.
El programa debe:
1. Crear las clases Federado y Evaluacion. Los datos de los archivos representan el
estado de los objetos pertenecientes a estas clases.
2. Cargar los datos de los objetos que representan a los Federados en un
ManejadorFederados, leyendo los datos del archivo “federados.csv”, implemente el
manejador con una Lista Python.
3. Cargar los datos de los objetos que respresentan Evaluaciones en un
ManejadorEvaluaciones, leyendo los datos del archivo “evaluacion.csv”, implemente
el manejador con una Lista Python..
A través de un menú de opciones, llevar a cabo las siguientes funcionalidades:
a. Leer un estilo y una edad y listar apellido, nombre y DNI de cada patinador que
participó en el estilo dado.
b. Mostrar apellido y nombre del patinador, estilo y club al que representa el patinador
que obtuvo el mayor puntaje en la evaluación.
Regla de negocio: El puntaje es el promedio de las 3 valoraciones dadas por los
jueces. Además, para resolver esta funcionalidad, el analista le solicita que
sobrecargueel operador “>”.
c. Listar los datos de los patinadores que participaron en estilo libre y en escuela.
d. Dado el DNI de un inscripto y un estilo, mostrar las 3 valoraciones dadas por los
jueces.  """



from GestorEvaluacion import GestorEvaluacion
from GestorPatinador import GestorPatinador


   
def test():
    gestorPatinador = GestorPatinador()
    gestorEvaluacion = GestorEvaluacion()
    gestorPatinador.CargarArchivo()
    gestorEvaluacion.cargarArchivo()
    while True:
        print("1. Leer un estilo y una edad y listar apellido, nombre y DNI de cada patinador que participó en el estilo dado.")
        print("2. Mostrar apellido y nombre del patinador, estilo y club al que representa el patinador que obtuvo el mayor puntaje en la evaluación.")
        print("3. Listar los datos de los patinadores que participaron en estilo libre y en escuela.")
        print("4. Dado el DNI de un inscripto y un estilo, mostrar las 3 valoraciones dadas por los jueces.")
        print("5. Salir")
        opcion = int(input("Ingrese una opcion: "))
        if opcion == 1:
            estilo = input("Ingrese el estilo: ")
            edad = int(input("Ingrese la edad: "))
            
            gestorPatinador.listarPatinadores(estilo, edad, gestorEvaluacion.getListaEvaluaciones())
        elif opcion == 2:
            gestorPatinador.patinadorMayorPuntaje(gestorEvaluacion.getListaEvaluaciones())
        elif opcion == 3:
            gestorPatinador.listarPatinadoresEstilo(gestorEvaluacion.getListaEvaluaciones())
        elif opcion == 4:
            dni = input("Ingrese el DNI: ")
            estilo = input("Ingrese el estilo: ")
            gestorEvaluacion.mostrarValoraciones(dni, estilo)
        elif opcion == 5:
            break
        else:
            print("Opcion incorrecta")
    
if __name__ == '__main__':
    test()
    