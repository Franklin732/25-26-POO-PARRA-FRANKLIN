"""
Módulo Producto: Define la clase Producto para la gestión de items del inventario.

Este módulo contiene la clase Producto que representa un item individual en el inventario
con atributos como ID, nombre, cantidad y precio, además de métodos para obtener y
establecer estos atributos.
"""


class Producto:
    """
    Clase que representa un producto en el inventario.
    
    Atributos:
        id (int): Identificador único del producto
        nombre (str): Nombre del producto
        cantidad (int): Cantidad disponible del producto en el inventario
        precio (float): Precio unitario del producto
    """
    
    def __init__(self, id_producto: int, nombre: str, cantidad: int, precio: float):
        """
        Inicializa un nuevo producto.
        
        Args:
            id_producto (int): ID único del producto
            nombre (str): Nombre del producto
            cantidad (int): Cantidad disponible
            precio (float): Precio unitario
            
        Raises:
            ValueError: Si la cantidad o precio son negativos
        """
        if cantidad < 0 or precio < 0:
            raise ValueError("La cantidad y el precio no pueden ser negativos")
        
        self._id = id_producto
        self._nombre = nombre
        self._cantidad = cantidad
        self._precio = precio
    
    # Getters
    @property
    def id(self) -> int:
        """Retorna el ID del producto."""
        return self._id
    
    @property
    def nombre(self) -> str:
        """Retorna el nombre del producto."""
        return self._nombre
    
    @property
    def cantidad(self) -> int:
        """Retorna la cantidad disponible del producto."""
        return self._cantidad
    
    @property
    def precio(self) -> float:
        """Retorna el precio unitario del producto."""
        return self._precio
    
    # Setters
    @nombre.setter
    def nombre(self, nuevo_nombre: str) -> None:
        """Establece un nuevo nombre al producto."""
        if not nuevo_nombre or not isinstance(nuevo_nombre, str):
            raise ValueError("El nombre debe ser una cadena de texto válida")
        self._nombre = nuevo_nombre
    
    @cantidad.setter
    def cantidad(self, nueva_cantidad: int) -> None:
        """
        Establece una nueva cantidad al producto.
        
        Args:
            nueva_cantidad (int): Nueva cantidad
            
        Raises:
            ValueError: Si la cantidad es negativa
        """
        if nueva_cantidad < 0:
            raise ValueError("La cantidad no puede ser negativa")
        self._cantidad = nueva_cantidad
    
    @precio.setter
    def precio(self, nuevo_precio: float) -> None:
        """
        Establece un nuevo precio al producto.
        
        Args:
            nuevo_precio (float): Nuevo precio
            
        Raises:
            ValueError: Si el precio es negativo
        """
        if nuevo_precio < 0:
            raise ValueError("El precio no puede ser negativo")
        self._precio = nuevo_precio
    
    def obtener_valor_total(self) -> float:
        """Calcula el valor total del producto (cantidad * precio)."""
        return self._cantidad * self._precio
    
    def __str__(self) -> str:
        """Retorna una representación en string del producto."""
        return (f"ID: {self._id} | Nombre: {self._nombre} | "
                f"Cantidad: {self._cantidad} | Precio: ${self._precio:.2f} | "
                f"Valor Total: ${self.obtener_valor_total():.2f}")
    
    def __repr__(self) -> str:
        """Retorna una representación técnica del producto."""
        return (f"Producto(id={self._id}, nombre='{self._nombre}', "
                f"cantidad={self._cantidad}, precio={self._precio})")
    
    def a_diccionario(self) -> dict:
        """Convierte el producto a un diccionario para serialización."""
        return {
            'id': self._id,
            'nombre': self._nombre,
            'cantidad': self._cantidad,
            'precio': self._precio
        }
    
    @classmethod
    def desde_diccionario(cls, datos: dict) -> 'Producto':
        """Crea un producto desde un diccionario."""
        return cls(
            id_producto=datos['id'],
            nombre=datos['nombre'],
            cantidad=datos['cantidad'],
            precio=datos['precio']
        )
