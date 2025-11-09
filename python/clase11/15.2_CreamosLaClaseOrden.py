class Orden:
    contador_ordenes = 0

    def __init__(self, productos):
        Orden.contador_ordenes += 1
        self.id_orden = Orden.contador_ordenes
        self.productos = list(productos)

    def agregar_producto(self, producto):
        self.productos.append(producto) # Esto es para agregar un nuevo producto
    def calcular_total(self):
        total = 0 # Variable temporal para almacenar el total temporal
        for producto in self._productos:
            total += producto.precio
        return total

    def __str__(self):
        productos_str = ''
        for producto in self._productos:
            productos_str += producto.__str__() + ' | '
        return f'Orden: {self.id_orden}, \nProducto: {productos_str}'
    
if __name__ == '__main__':
    producto1 = Producto('Camiseta', 1000.00)
    producto2 = Producto('Pantalon', 1500.00)
    productos1 = [producto1, producto2] # Lista de productos
    orden1 = Orden(productos1) # Primer objeto orden pasando la lista de productos
    print(orden1)
    orden2 = Orden(productos1)
    print(orden2)

# Tarea: Modificar la orden2, ingresando nuevos productos con sus nombres y precios
# crear una nueva lista de productos y agregarla a la orden2
#Creamos nuevos productos
    producto3 = Producto('Zapatos', 3500.50)
    producto4 = Producto('Gorra', 450.00)
    producto5 = Producto("Chaqueta", 4000.00)
    producto6 = Producto("Medias", 200.00)
# Utilizamos el método 'agregar_producto' de la clase Orden
    orden2.agregar_producto(producto3)
    orden2.agregar_producto(producto4)
    orden2.agregar_producto(producto5)
    orden2.agregar_producto(producto6)