
"""
Sistema de Gestión de Tienda
Este programa modela una tienda utilizando los principios de Programación Orientada a Objetos (POO).


class Producto:
    """
    Clase que representa un producto de la tienda.
    """
    def __init__(self, nombre, precio, cantidad):
        """
        Inicializa un producto con nombre, precio y cantidad en stock.
        :param nombre: Nombre del producto (str).
        :param precio: Precio del producto (float).
        :param cantidad: Cantidad en stock (int).
        """
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def vender(self, cantidad):
        """
        Reduce la cantidad en stock si hay suficiente inventario.
        :param cantidad: Cantidad a vender (int).
        """
        if cantidad > self.cantidad:
            print(f"No hay suficiente stock de {self.nombre}. Disponible: {self.cantidad}.")
        else:
            self.cantidad -= cantidad
            print(f"Se vendieron {cantidad} unidades de {self.nombre}.")

    def reabastecer(self, cantidad):
        """
        Aumenta la cantidad en stock.
        :param cantidad: Cantidad a agregar (int).
        """
        self.cantidad += cantidad
        print(f"Se añadieron {cantidad} unidades de {self.nombre}. Stock actual: {self.cantidad}.")

    def __str__(self):
        """Devuelve una representación en cadena del producto."""
        return f"Producto: {self.nombre}, Precio: ${self.precio:.2f}, Stock: {self.cantidad}"


class Tienda:
    """
    Clase que representa una tienda.
    """
    def __init__(self, nombre):
        """
        Inicializa la tienda con un nombre y una lista de productos.
        :param nombre: Nombre de la tienda (str).
        """
        self.nombre = nombre
        self.productos = []

    def agregar_producto(self, producto):
        """
        Añade un producto a la tienda.
        :param producto: Objeto de la clase Producto.
        """
        self.productos.append(producto)
        print(f"Producto {producto.nombre} añadido a la tienda {self.nombre}.")

    def mostrar_productos(self):
        """Muestra todos los productos disponibles en la tienda."""
        print(f"\n--- Productos en {self.nombre} ---")
        for producto in self.productos:
            print(producto)

    def buscar_producto(self, nombre_producto):
        """
        Busca un producto por su nombre.
        :param nombre_producto: Nombre del producto a buscar (str).
        :return: Objeto Producto o None si no se encuentra.
        """
        for producto in self.productos:
            if producto.nombre.lower() == nombre_producto.lower():
                return producto
        print(f"Producto '{nombre_producto}' no encontrado.")
        return None


# Ejemplo de uso
if __name__ == "__main__":
    tienda = Tienda("Tienda Virtual")

    # Crear productos
    producto1 = Producto("Laptop", 800.00, 10)
    producto2 = Producto("Auriculares", 50.00, 30)
    producto3 = Producto("Ratón", 25.00, 50)

    # Agregar productos a la tienda
    tienda.agregar_producto(producto1)
    tienda.agregar_producto(producto2)
    tienda.agregar_producto(producto3)

    # Mostrar productos disponibles
    tienda.mostrar_productos()

    # Realizar una venta
    print("\nRealizando una venta:")
    producto_a_vender = tienda.buscar_producto("Laptop")
    if producto_a_vender:
        producto_a_vender.vender(3)

    # Mostrar productos después de la venta
    tienda.mostrar_productos()

    # Reabastecer un producto
    print("\nReabasteciendo producto:")
    producto_a_reabastecer = tienda.buscar_producto("Auriculares")
    if producto_a_reabastecer:
        producto_a_reabastecer.reabastecer(20)

    # Mostrar productos después de reabastecer
    tienda.mostrar_productos()
