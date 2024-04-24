import numpy as np


class GestorVenta: 

    def __init__(self):
        self.gestor_ventas = np.zeros(shape=(5, 7))

    def ingresar_factura(self, dia, sucursal, importe):
        self.gestor_ventas[sucursal - 1][dia - 1] += importe

    def mostrarGestor(self):
        print("Gestor de ventas:")
        for fila in self.gestor_ventas:
            print(fila)

    def calcular_total(self, sucursal):
        total = 0
        for dia in range(7):
            total += self.gestor_ventas[sucursal - 1][dia]
        return total
    def sucursal_mas_facturacion_dia(self, dia):
        maximo = -1
        sucursal = 0
        for i in range(5):
            if self.gestor_ventas[i][dia] > maximo:
                maximo = self.gestor_ventas[i][dia]
                sucursal = i + 1
        return sucursal
    def sucursal_menos_facturacion_semana(self):
        minimo = np.sum(self.gestor_ventas[0])
        sucursal = 1
        for i in range(1, 5):
            total = np.sum(self.gestor_ventas[i])
            if total < minimo:
                minimo = total
                sucursal = i + 1
        return sucursal
    def total_facturado_semana(self):
        return np.sum(self.gestor_ventas)


