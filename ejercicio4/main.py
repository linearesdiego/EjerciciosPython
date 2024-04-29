""" La empresa “RapiPedido”, lo contrata para desarrollar un sistema que debe procesar los
    pedidos que llevan las motos que dispone para el delibery de comida.
    Cada moto registra: patente, marca, nombre y apellido del conductor, kilometraje.
    De cada pedido se registran: patente de la moto que lo tuvo asignado, identificador de
    pedido, comidas pedidas, tiempo estimado de entrega (en minutos), tiempo real de entrega
    (se inicializa en cero), precio del pedido.
    El sistema debe proveer un menú de opciones que permita:
    1. Leer los datos de las motos, desde un archivo denominado “datosMotos.csv” y cargarlos
    en un Gestor de Motos.
    2. Leer los datos de los pedidos, desde un archivo denominado “datosPedidos.csv”, y
    cargarlos en el Gestor de Pedidos.
    3. Cargar nuevos pedidos, leer los datos por teclado, y asignar a una moto el pedido, al
    solicitar la patente de la moto para asignarla, validar que la moto existe.
    4. Leer por teclado número de patente, identificador de pedido, y tiempo real de entrega,
    modificar en el Gestor de Pedidos, el tiempo real de entrega para ese pedido.
    4. Leer por una patente de una moto, mostrar los datos del conductor y el tiempo promedio
    real de entrega de los pedidos que hizo.
    5. Generar un listado para cada moto, para el pago de comisiones a los conductores de las
    motos:
    Patente de Moto: xxxx-xxx
    Conductor: xxxxxxxxxxxxxxxxxxxxxxxxxx
    Identificador de pedido Tiempo estimado Tiempo real Precio
    xxx xxx xxx $ xxxx.xx
    xxx xxx xxx $ xxxx.xx
    xxx xxx xxx $ xxxx.xx
    Total: $ xxxx.xx
    Comisión: $ xxxx.xx (20% del total)
    Regla de negocio:
    Los archivos no presentan un orden en particular
    Ordenar de menor a mayor el Gestor de pedidos por número de patente, de modo que
    permita resolver eficientemente las búsquedas. Pare ello debe sobrecargar el operador <
(__lt__). """
from GestorMotos import GestorMotos
from GestorPedidos import GestorPedido
def test():
    gestorMotos = GestorMotos()
    gestorPedidos = GestorPedido()
    gestorMotos.cargarObjeto()
    gestorPedidos.cargarObjeto()
    
    while True:
        print("1) Cargar nuevos pedidos")
        print("2) Modificar tiempo real de entrega de un pedido")
        print("3) mostrar datos del conductor y tiempo promedio real de entrega de los pedidos que hizo")
        print("4) Generar listado para el pago de comisiones a los conductores de las motos")
        print("5) ordenamiento por patentee y salir")

        opcion= input("Seleccione una opcion \n")

        if opcion == "1":
            patente = input("Ingrese la patente de la moto \n")
            idPedido = input("Ingrese el id del pedido \n")
            comidas = input("Ingrese las comidas \n")
            tiempoEstimado = input("Ingrese el tiempo estimado \n")
            tiempoReal = input("Ingrese el tiempo real \n")
            precio = input("Ingrese el precio \n")

            indice = gestorMotos.buscarMoto(patente)
           
            if indice != None:
                gestorPedidos.asignarPedido(patente, idPedido, comidas, tiempoEstimado, tiempoReal, precio)
            else:
                print("No se encontro la moto con la patente ingresada".format(patente))
        if opcion == "2":
            
            patente = input("Ingrese la patente de la moto \n")
            idPedido = input("Ingrese el id del pedido \n")
            tiempoReal = input("Ingrese el tiempo real \n")

            gestorPedidos.modificarTiempoReal(patente, idPedido, tiempoReal)
        if opcion == "3":
            """mostrar datos del conductor y tiempo promedio real de entrega de los pedidos que hizo"""            
            patente = input("Ingrese la patente de la moto \n")
            indice= gestorMotos.buscarMoto(patente)
            if indice != None:
                print("Datos del conductor: ")
                print("Nombre: {}".format(indice.getNombre()))
                print("Apellido: {}".format(indice.getApellido()))

                print("Tiempo promedio real de entrega de los pedidos que hizo: {}".format(gestorPedidos.tiempoPromedioReal(patente)))
            
        if opcion == "4":
            gestorPedidos.generarListado(gestorPedidos)
        

        if opcion == "5":
            gestorPedidos.ordenar()
            gestorPedidos.mostrarObjeto()
            print("Saliendoooo!!")
            break
if __name__ == "__main__":

    test()

    
        

 


