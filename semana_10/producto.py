"""producto.py
Define la clase Producto para el sistema de inventarios con serializacion JSON.
"""


class Producto:
    """Representa un producto con identificador, nombre, cantidad y precio."""

    def __init__(self, producto_id, nombre, cantidad, precio):
        """Inicializa un producto con sus atributos principales."""
        self._id = producto_id
        self._nombre = nombre
        self._cantidad = cantidad
        self._precio = precio

    def get_id(self):
        """Devuelve el identificador unico del producto."""
        return self._id

    def set_id(self, producto_id):
        """Actualiza el identificador unico del producto."""
        self._id = producto_id

    def get_nombre(self):
        """Devuelve el nombre del producto."""
        return self._nombre

    def set_nombre(self, nombre):
        """Actualiza el nombre del producto."""
        self._nombre = nombre

    def get_cantidad(self):
        """Devuelve la cantidad disponible del producto."""
        return self._cantidad

    def set_cantidad(self, cantidad):
        """Actualiza la cantidad disponible del producto."""
        self._cantidad = cantidad

    def get_precio(self):
        """Devuelve el precio unitario del producto."""
        return self._precio

    def set_precio(self, precio):
        """Actualiza el precio unitario del producto."""
        self._precio = precio

    def to_dict(self):
        """Convierte el producto a un diccionario serializable en JSON."""
        return {
            "id": self._id,
            "nombre": self._nombre,
            "cantidad": self._cantidad,
            "precio": self._precio,
        }

    @staticmethod
    def from_dict(data):
        """Crea un producto desde un diccionario validando claves esperadas."""
        return Producto(
            data["id"],
            data["nombre"],
            data["cantidad"],
            data["precio"],
        )
