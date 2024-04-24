from GestorVenta import GestorVenta
from opciones import opciones



if __name__ == '__main__':

    gestor = GestorVenta()
    opcion = opciones()

        
    while True:
        
        if opcion == "a":
            dia = int(input("Ingrese el día de la semana (1-7): "))
            sucursal = int(input("Ingrese el número de sucursal (1-5): "))
            importe = float(input("Ingrese el importe de la factura: "))
            gestor.ingresar_factura(dia, sucursal, importe)
            gestor.mostrarGestor()
        elif opcion == "b":
            sucursal = int(input("Ingrese el número de sucursal (1-5): "))
            print("Total facturado para la sucursal", sucursal, ":", gestor.calcular_total(sucursal))
        elif opcion == "c":
            dia = int(input("Ingrese el día de la semana (1-7): "))
            print("La sucursal que más facturó para el día", dia, "es la sucursal", gestor.sucursal_mas_facturacion_dia(dia))

        elif opcion == "d":
            print("La sucursal con menos facturación durante toda la semana es la sucursal", gestor.sucursal_menos_facturacion_semana())
        elif opcion == "e":
            print("El total facturado por todas las sucursales durante toda la semana es:", gestor.total_facturado_semana())

        elif opcion == "x":
            print("Saliendo del programa...")
            break

        else:
     
            print("Opción inválida. Por favor, seleccione una opción válida.")
        opcion = opciones()
