"""Pruebas para el sistema de gestion de inventarios con persistencia."""

import json
import os
import tempfile
import unittest
from unittest import mock

from inventario import Inventario
from producto import Producto


class InventarioTests(unittest.TestCase):
    """Valida persistencia y manejo de excepciones en Inventario."""

    def _ruta_tmp(self, tmp_dir):
        return os.path.join(tmp_dir, "inventario.txt")

    def test_crea_archivo_si_no_existe(self):
        """Debe crear el archivo cuando no existe."""
        with tempfile.TemporaryDirectory() as tmp_dir:
            ruta = self._ruta_tmp(tmp_dir)
            self.assertFalse(os.path.exists(ruta))
            inventario = Inventario(ruta)
            self.assertTrue(os.path.exists(ruta))
            ok, _ = inventario.obtener_estado_carga()
            self.assertTrue(ok)

    def test_carga_productos_desde_archivo(self):
        """Debe reconstruir el inventario desde un JSON valido."""
        with tempfile.TemporaryDirectory() as tmp_dir:
            ruta = self._ruta_tmp(tmp_dir)
            datos = [
                {"id": 1, "nombre": "Lapiz", "cantidad": 5, "precio": 1.2},
                {"id": 2, "nombre": "Borrador", "cantidad": 3, "precio": 0.8},
            ]
            with open(ruta, "w", encoding="utf-8") as archivo:
                json.dump(datos, archivo)

            inventario = Inventario(ruta)
            productos = inventario.mostrar_todos()
            self.assertEqual(len(productos), 2)
            self.assertEqual(productos[0].get_nombre(), "Lapiz")

    def test_agregar_guarda_en_archivo(self):
        """Agregar productos debe persistirlos en el archivo."""
        with tempfile.TemporaryDirectory() as tmp_dir:
            ruta = self._ruta_tmp(tmp_dir)
            inventario = Inventario(ruta)
            exito, _ = inventario.agregar_producto(Producto(1, "Cuaderno", 2, 3.5))
            self.assertTrue(exito)

            with open(ruta, "r", encoding="utf-8") as archivo:
                datos = json.load(archivo)
            self.assertEqual(len(datos), 1)
            self.assertEqual(datos[0]["nombre"], "Cuaderno")

    def test_actualizar_guarda_en_archivo(self):
        """Actualizar productos debe reflejarse en el archivo."""
        with tempfile.TemporaryDirectory() as tmp_dir:
            ruta = self._ruta_tmp(tmp_dir)
            inventario = Inventario(ruta)
            inventario.agregar_producto(Producto(1, "Libro", 1, 10.0))

            exito, _ = inventario.actualizar_producto(1, nueva_cantidad=4, nuevo_precio=12.0)
            self.assertTrue(exito)

            with open(ruta, "r", encoding="utf-8") as archivo:
                datos = json.load(archivo)
            self.assertEqual(datos[0]["cantidad"], 4)
            self.assertEqual(datos[0]["precio"], 12.0)

    def test_eliminar_guarda_en_archivo(self):
        """Eliminar productos debe reflejarse en el archivo."""
        with tempfile.TemporaryDirectory() as tmp_dir:
            ruta = self._ruta_tmp(tmp_dir)
            inventario = Inventario(ruta)
            inventario.agregar_producto(Producto(1, "Regla", 1, 1.0))

            exito, _ = inventario.eliminar_producto(1)
            self.assertTrue(exito)

            with open(ruta, "r", encoding="utf-8") as archivo:
                datos = json.load(archivo)
            self.assertEqual(datos, [])

    def test_archivo_corrupto_respaldo(self):
        """Un JSON invalido debe provocar respaldo y reinicio del archivo."""
        with tempfile.TemporaryDirectory() as tmp_dir:
            ruta = self._ruta_tmp(tmp_dir)
            with open(ruta, "w", encoding="utf-8") as archivo:
                archivo.write("{no_es_json}")

            inventario = Inventario(ruta)
            ok, _ = inventario.obtener_estado_carga()
            self.assertFalse(ok)

            respaldos = [
                nombre for nombre in os.listdir(tmp_dir)
                if nombre.startswith("inventario.txt.corrupto_")
            ]
            self.assertTrue(respaldos)

            with open(ruta, "r", encoding="utf-8") as archivo:
                datos = json.load(archivo)
            self.assertEqual(datos, [])

    def test_manejo_permission_error_escritura(self):
        """Debe informar error cuando falla la escritura por permisos."""
        with tempfile.TemporaryDirectory() as tmp_dir:
            ruta = self._ruta_tmp(tmp_dir)
            inventario = Inventario(ruta)

            with mock.patch("builtins.open", side_effect=PermissionError):
                exito, mensaje = inventario.agregar_producto(
                    Producto(1, "Tijeras", 1, 2.0)
                )

            self.assertFalse(exito)
            self.assertIn("permiso", mensaje.lower())

    def test_manejo_permission_error_lectura(self):
        """Debe informar error cuando falla la lectura por permisos."""
        with tempfile.TemporaryDirectory() as tmp_dir:
            ruta = self._ruta_tmp(tmp_dir)
            with open(ruta, "w", encoding="utf-8") as archivo:
                json.dump([], archivo)

            with mock.patch("builtins.open", side_effect=PermissionError):
                inventario = Inventario(ruta)

            ok, mensaje = inventario.obtener_estado_carga()
            self.assertFalse(ok)
            self.assertIn("permiso", mensaje.lower())


if __name__ == "__main__":
    unittest.main()
