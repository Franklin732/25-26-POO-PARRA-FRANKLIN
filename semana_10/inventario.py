"""inventario.py
Define la clase Inventario con persistencia en archivo JSON.
"""

import json
import os
import shutil
import time

from producto import Producto


class Inventario:
    """Gestiona productos y sincroniza cambios con un archivo JSON."""

    def __init__(self, ruta_archivo=None):
        """Inicializa el inventario y carga datos desde el archivo."""
        if ruta_archivo is None:
            ruta_archivo = os.path.join(os.path.dirname(__file__), "inventario.txt")
        self._ruta_archivo = ruta_archivo
        self._productos = []
        self._carga_ok = True
        self._mensaje_carga = "Inventario listo para usar."
        self._cargar_desde_archivo()

    def obtener_estado_carga(self):
        """Devuelve el resultado de la carga inicial del inventario."""
        return self._carga_ok, self._mensaje_carga

    def agregar_producto(self, producto):
        """Agrega un producto si el ID es unico y guarda en archivo."""
        if self._buscar_por_id(producto.get_id()) is not None:
            return False, "Error: ya existe un producto con ese ID."
        self._productos.append(producto)
        exito, mensaje_archivo = self._guardar_en_archivo()
        if not exito:
            self._productos.pop()
            return False, mensaje_archivo
        return True, "Producto agregado y guardado en archivo."

    def eliminar_producto(self, producto_id):
        """Elimina un producto por ID y guarda en archivo."""
        producto = self._buscar_por_id(producto_id)
        if producto is None:
            return False, "Error: no se encontro un producto con ese ID."
        self._productos.remove(producto)
        exito, mensaje_archivo = self._guardar_en_archivo()
        if not exito:
            self._productos.append(producto)
            return False, mensaje_archivo
        return True, "Producto eliminado y archivo actualizado."

    def actualizar_producto(self, producto_id, nueva_cantidad=None, nuevo_precio=None):
        """Actualiza cantidad, precio o ambos de un producto por ID."""
        producto = self._buscar_por_id(producto_id)
        if producto is None:
            return False, "Error: no se encontro un producto con ese ID."
        cantidad_anterior = producto.get_cantidad()
        precio_anterior = producto.get_precio()

        if nueva_cantidad is not None:
            producto.set_cantidad(nueva_cantidad)
        if nuevo_precio is not None:
            producto.set_precio(nuevo_precio)

        exito, mensaje_archivo = self._guardar_en_archivo()
        if not exito:
            producto.set_cantidad(cantidad_anterior)
            producto.set_precio(precio_anterior)
            return False, mensaje_archivo
        return True, "Producto actualizado y archivo sincronizado."

    def buscar_por_nombre(self, nombre):
        """Busca productos por nombre con coincidencia parcial e insensible a mayusculas."""
        nombre_normalizado = nombre.strip().lower()
        return [
            producto
            for producto in self._productos
            if nombre_normalizado in producto.get_nombre().lower()
        ]

    def mostrar_todos(self):
        """Devuelve una lista con todos los productos en el inventario."""
        return list(self._productos)

    def _buscar_por_id(self, producto_id):
        """Busca un producto por ID y lo devuelve o None si no existe."""
        for producto in self._productos:
            if producto.get_id() == producto_id:
                return producto
        return None

    def _cargar_desde_archivo(self):
        """Carga datos del archivo, manejando errores de lectura o formato."""
        try:
            if not os.path.exists(self._ruta_archivo):
                # Si no existe el archivo, se crea con una lista JSON vacia.
                self._escribir_datos([])
                self._carga_ok = True
                self._mensaje_carga = "Archivo de inventario creado." 
                return

            with open(self._ruta_archivo, "r", encoding="utf-8") as archivo:
                contenido = archivo.read().strip()

            if not contenido:
                # Un archivo vacio representa un inventario sin productos.
                self._productos = []
                self._carga_ok = True
                self._mensaje_carga = "Archivo vacio cargado correctamente." 
                return

            datos = json.loads(contenido)
            if not isinstance(datos, list):
                raise ValueError("El archivo no contiene una lista de productos.")

            self._productos = [Producto.from_dict(item) for item in datos]
            self._carga_ok = True
            self._mensaje_carga = "Inventario cargado desde archivo." 

        except FileNotFoundError:
            # Si el archivo se elimina entre la verificacion y la lectura,
            # se crea uno nuevo para continuar.
            self._productos = []
            self._carga_ok = False
            self._mensaje_carga = "Archivo no encontrado. Se creara uno nuevo."
            self._escribir_datos([])

        except PermissionError:
            # Falta de permisos de lectura: se informa y se mantiene inventario vacio.
            self._productos = []
            self._carga_ok = False
            self._mensaje_carga = "Permiso denegado al leer el archivo de inventario."

        except (json.JSONDecodeError, ValueError):
            # Un JSON invalido o estructura inesperada se considera archivo corrupto.
            self._productos = []
            self._carga_ok = False
            # Se respalda el archivo corrupto antes de reiniciar la data.
            self._respaldar_archivo_corrupto()
            self._escribir_datos([])
            self._mensaje_carga = (
                "Archivo corrupto detectado. Se respaldo y se creo un nuevo archivo."
            )

    def _guardar_en_archivo(self):
        """Serializa productos y los guarda en el archivo."""
        try:
            datos = [producto.to_dict() for producto in self._productos]
            # Escritura atomica simple al sobrescribir el archivo completo.
            self._escribir_datos(datos)
            return True, "Archivo actualizado correctamente."
        except FileNotFoundError:
            return False, "Error: archivo de inventario no encontrado."
        except PermissionError:
            return False, "Error: permiso denegado al escribir en el archivo."
        except OSError as exc:
            return False, f"Error inesperado al guardar el archivo: {exc}"

    def _escribir_datos(self, datos):
        """Escribe la lista de datos en el archivo de inventario en formato JSON."""
        with open(self._ruta_archivo, "w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, indent=4, ensure_ascii=True)

    def _respaldar_archivo_corrupto(self):
        """Respalda el archivo corrupto para permitir inspeccion posterior."""
        if not os.path.exists(self._ruta_archivo):
            return
        marca_tiempo = time.strftime("%Y%m%d_%H%M%S")
        destino = f"{self._ruta_archivo}.corrupto_{marca_tiempo}"
        try:
            shutil.copy2(self._ruta_archivo, destino)
        except (OSError, PermissionError):
            pass
