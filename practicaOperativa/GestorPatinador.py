from os import path
import csv
from Patinador import Patinador
class GestorPatinador:
    __listPatinadores = []

    def __init__(self):
        self.__listPatinadores = []

    def CargarArchivo(self):
        archivo = open(path.dirname(__file__) + '/federados.csv')
        reader = csv.reader(archivo, delimiter=";")

        for fila in reader:
            patinador = Patinador(fila[0],fila[1],fila[2],int(fila[3]),fila[4])
            self.__listPatinadores.append(patinador)
    def mostrar(self):
        for i in range(len(self.__listPatinadores)):
            print(self.__listPatinadores[i])

    def listarPatinadores(self, estilo, edad,listEvaluaciones):
        for patinador in self.__listPatinadores:
            for evaluacion in listEvaluaciones:
                if patinador.getDni() == evaluacion.getDniPatinador() and evaluacion.getEstilo() == estilo and patinador.getEdad() == edad:
                    print(patinador.getApellido(), patinador.getNombre(), patinador.getDni())
    

    print("2. Mostrar apellido y nombre del patinador, estilo y club al que representa el patinador que obtuvo el mayor puntaje en la evaluación.")

    
    def patinadorMayorPuntaje(self, listEvaluaciones):
        mayor = 0
        for evaluacion in listEvaluaciones:
            if evaluacion.getValoracion() > mayor:
                mayor = evaluacion.getValoracion()
                dni = evaluacion.getDniPatinador()
        for patinador in self.__listPatinadores:
            if patinador.getDni() == dni:
                print(patinador.getApellido(), patinador.getNombre(), evaluacion.getEstilo(), patinador.getClub())

    def listarPatinadoresEstilo(self, listEvaluaciones):
        for patinador in self.__listPatinadores:
            libre = False
            escuela = False
            for evaluacion in listEvaluaciones:
                if patinador.getDni() == evaluacion.getDniPatinador() and evaluacion.getEstilo() == "libre":
                    libre = True
                elif patinador.getDni() == evaluacion.getDniPatinador() and evaluacion.getEstilo() == "escuela":
                    escuela = True
            if libre and escuela:
                print(patinador.getApellido(), patinador.getNombre(), patinador.getDni(), patinador.getEdad(), patinador.getClub())