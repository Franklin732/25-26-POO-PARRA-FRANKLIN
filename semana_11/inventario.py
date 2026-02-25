"""
Módulo Inventario: Define la clase Inventario para la gestión de múltiples productos.

Este módulo contiene la clase Inventario que utiliza colecciones (diccionarios) para
almacenar y gestionar productos, con métodos para operaciones CRUD (Create, Read, Update, Delete)
y almacenamiento persistente en archivos JSON.
"""

import json
import os
from typing import Dict, List, Optional
from producto import Producto


class Inventario:
    """
    Clase que gestiona una colección de productos.
    
    Utiliza un diccionario para almacenar productos con su ID como clave,
    permitiendo búsquedas rápidas y eficientes. Soporta serialización a JSON
    para almacenamiento persistente.
    """
    
    def __init__(self, ruta_archivo: str = "inventario.json"):
        """
        Inicializa el inventario.
        
        Args:
            ruta_archivo (str): Ruta del archivo JSON para almacenar/cargar el inventario
        """
        self._productos: Dict[int, Producto] = {}
        self._ruta_archivo = ruta_archivo
        self._siguiente_id = 1
        
        # Cargar inventario existente si el archivo existe
        if os.path.exists(ruta_archivo):
            self.cargar_desde_archivo()
    
    def obtener_siguiente_id(self) -> int:
        """Obtiene el siguiente ID disponible para un nuevo producto."""
        max_id = max(self._productos.keys()) if self._productos else 0
        self._siguiente_id = max(self._siguiente_id, max_id + 1)
        return self._siguiente_id
    
    def añadir_producto(self, nombre: str, cantidad: int, precio: float) -> int:
        """
        Añade un nuevo producto al inventario.
        
        Args:
            nombre (str): Nombre del producto
            cantidad (int): Cantidad inicial
            precio (float): Precio unitario
            
        Returns:
            int: ID del producto creado
            
        Raises:
            ValueError: Si los parámetros no son válidos
        """
        id_producto = self.obtener_siguiente_id()
        producto = Producto(id_producto, nombre, cantidad, precio)
        self._productos[id_producto] = producto
        self._siguiente_id += 1
        return id_producto
    
    def eliminar_producto(self, id_producto: int) -> bool:
        """
        Elimina un producto del inventario por su ID.
        
        Args:
            id_producto (int): ID del producto a eliminar
            
        Returns:
            bool: True si se eliminó, False si no existía
        """
        if id_producto in self._productos:
            del self._productos[id_producto]
            return True
        return False
    
    def actualizar_cantidad(self, id_producto: int, nueva_cantidad: int) -> bool:
        """
        Actualiza la cantidad de un producto.
        
        Args:
            id_producto (int): ID del producto
            nueva_cantidad (int): Nueva cantidad
            
        Returns:
            bool: True si se actualizó, False si el producto no existe
            
        Raises:
            ValueError: Si la cantidad es negativa
        """
        if id_producto in self._productos:
            self._productos[id_producto].cantidad = nueva_cantidad
            return True
        return False
    
    def actualizar_precio(self, id_producto: int, nuevo_precio: float) -> bool:
        """
        Actualiza el precio de un producto.
        
        Args:
            id_producto (int): ID del producto
            nuevo_precio (float): Nuevo precio
            
        Returns:
            bool: True si se actualizó, False si el producto no existe
            
        Raises:
            ValueError: Si el precio es negativo
        """
        if id_producto in self._productos:
            self._productos[id_producto].precio = nuevo_precio
            return True
        return False
    
    def buscar_por_id(self, id_producto: int) -> Optional[Producto]:
        """
        Busca un producto por su ID.
        
        Args:
            id_producto (int): ID del producto
            
        Returns:
            Producto: El producto si existe, None en caso contrario
        """
        return self._productos.get(id_producto)
    
    def buscar_por_nombre(self, nombre: str) -> List[Producto]:
        """
        Busca productos por nombre (búsqueda parcial, sin importar mayúsculas/minúsculas).
        
        Args:
            nombre (str): Nombre o parte del nombre a buscar
            
        Returns:
            List[Producto]: Lista de productos que coinciden con la búsqueda
        """
        nombre_lower = nombre.lower()
        return [
            producto for producto in self._productos.values()
            if nombre_lower in producto.nombre.lower()
        ]
    
    def obtener_todos_productos(self) -> List[Producto]:
        """
        Obtiene todos los productos en el inventario.
        
        Returns:
            List[Producto]: Lista de todos los productos
        """
        return list(self._productos.values())
    
    def obtener_cantidad_productos(self) -> int:
        """Retorna la cantidad total de productos diferentes en el inventario."""
        return len(self._productos)
    
    def obtener_cantidad_items(self) -> int:
        """Retorna la cantidad total de items (suma de todas las cantidades)."""
        return sum(producto.cantidad for producto in self._productos.values())
    
    def obtener_valor_total_inventario(self) -> float:
        """Calcula el valor total del inventario."""
        return sum(
            producto.obtener_valor_total()
            for producto in self._productos.values()
        )
    
    def producto_existe(self, id_producto: int) -> bool:
        """Verifica si un producto existe en el inventario."""
        return id_producto in self._productos
    
    def obtener_estadisticas(self) -> Dict:
        """
        Obtiene estadísticas del inventario.
        
        Returns:
            Dict: Diccionario con estadísticas del inventario
        """
        productos = self.obtener_todos_productos()
        return {
            'cantidad_productos': self.obtener_cantidad_productos(),
            'cantidad_items_totales': self.obtener_cantidad_items(),
            'valor_total_inventario': self.obtener_valor_total_inventario(),
            'precio_promedio': (
                sum(p.precio for p in productos) / len(productos)
                if productos else 0
            )
        }
    
    def guardar_en_archivo(self) -> None:
        """Guarda el inventario en un archivo JSON."""
        datos = {
            'productos': [
                producto.a_diccionario()
                for producto in self._productos.values()
            ],
            'siguiente_id': self._siguiente_id
        }
        
        try:
            with open(self._ruta_archivo, 'w', encoding='utf-8') as archivo:
                json.dump(datos, archivo, indent=4, ensure_ascii=False)
            print(f"✓ Inventario guardado exitosamente en '{self._ruta_archivo}'")
        except IOError as e:
            print(f"✗ Error al guardar el inventario: {e}")
    
    def cargar_desde_archivo(self) -> None:
        """Carga el inventario desde un archivo JSON."""
        try:
            with open(self._ruta_archivo, 'r', encoding='utf-8') as archivo:
                datos = json.load(archivo)
            
            self._productos.clear()
            for datos_producto in datos.get('productos', []):
                producto = Producto.desde_diccionario(datos_producto)
                self._productos[producto.id] = producto
            
            self._siguiente_id = datos.get('siguiente_id', 1)
            print(f"✓ Inventario cargado exitosamente desde '{self._ruta_archivo}'")
        except IOError as e:
            print(f"✗ Error al cargar el inventario: {e}")
        except json.JSONDecodeError as e:
            print(f"✗ Error al decodificar JSON: {e}")
    
    def __str__(self) -> str:
        """Retorna una representación en string del inventario."""
        return f"Inventario con {self.obtener_cantidad_productos()} productos diferentes"
    
    def __repr__(self) -> str:
        """Retorna una representación técnica del inventario."""
        return f"Inventario(productos={len(self._productos)})"
