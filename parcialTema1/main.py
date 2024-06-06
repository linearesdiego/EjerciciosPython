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

