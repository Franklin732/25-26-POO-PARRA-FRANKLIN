"""inventario.py
Define la clase Inventario que administra una colección de productos.
"""

from producto import Producto


class Inventario:
    """Gestiona la lista de productos y las operaciones del inventario."""

    def __init__(self):
        """Inicializa el inventario con una lista vacía de productos."""
        self._productos = []

    def agregar_producto(self, producto):
        """Agrega un producto si el ID es único. Devuelve True si agrega, False si existe."""
        if self._buscar_por_id(producto.get_id()) is not None:
            return False
        self._productos.append(producto)
        return True

    def eliminar_producto(self, producto_id):
        """Elimina un producto por ID. Devuelve True si elimina, False si no existe."""
        producto = self._buscar_por_id(producto_id)
        if producto is None:
            return False
        self._productos.remove(producto)
        return True

    def actualizar_producto(self, producto_id, nueva_cantidad=None, nuevo_precio=None):
        """Actualiza cantidad, precio o ambos de un producto por ID."""
        producto = self._buscar_por_id(producto_id)
        if producto is None:
            return False
        if nueva_cantidad is not None:
            producto.set_cantidad(nueva_cantidad)
        if nuevo_precio is not None:
            producto.set_precio(nuevo_precio)
        return True

    def buscar_por_nombre(self, nombre):
        """Busca productos por nombre con coincidencia parcial e insensible a mayúsculas."""
        nombre_normalizado = nombre.strip().lower()
        resultados = []
        for producto in self._productos:
            if nombre_normalizado in producto.get_nombre().lower():
                resultados.append(producto)
        return resultados

    def mostrar_todos(self):
        """Devuelve una lista con todos los productos en el inventario."""
        return list(self._productos)

    def _buscar_por_id(self, producto_id):
        """Busca un producto por ID y lo devuelve o None si no existe."""
        for producto in self._productos:
            if producto.get_id() == producto_id:
                return producto
        return None
