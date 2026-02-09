"""producto.py
Define la clase Producto para el sistema de inventarios.
"""


class Producto:
    """Representa un producto con identificador único, nombre, cantidad y precio."""

    def __init__(self, producto_id, nombre, cantidad, precio):
        """Inicializa un producto con sus atributos principales."""
        self._id = producto_id
        self._nombre = nombre
        self._cantidad = cantidad
        self._precio = precio

    # Getter y setter para id
    def get_id(self):
        """Devuelve el identificador único del producto."""
        return self._id

    def set_id(self, producto_id):
        """Actualiza el identificador único del producto."""
        self._id = producto_id

    # Getter y setter para nombre
    def get_nombre(self):
        """Devuelve el nombre del producto."""
        return self._nombre

    def set_nombre(self, nombre):
        """Actualiza el nombre del producto."""
        self._nombre = nombre

    # Getter y setter para cantidad
    def get_cantidad(self):
        """Devuelve la cantidad disponible del producto."""
        return self._cantidad

    def set_cantidad(self, cantidad):
        """Actualiza la cantidad disponible del producto."""
        self._cantidad = cantidad

    # Getter y setter para precio
    def get_precio(self):
        """Devuelve el precio unitario del producto."""
        return self._precio

    def set_precio(self, precio):
        """Actualiza el precio unitario del producto."""
        self._precio = precio
