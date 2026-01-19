"""Demostración simple de constructores y destructores en Python."""
from __future__ import annotations

import gc
from datetime import datetime


class TemporaryResource:
    """Recurso que simula apertura y cierre, mostrando su ciclo de vida."""

    def __init__(self, name: str, resource_type: str) -> None:
        # El constructor se ejecuta al crear la instancia y prepara el estado inicial.
        self.name = name
        self.resource_type = resource_type
        self.created_at = datetime.now()
        print(f"[CREADO] Recurso '{self.name}' de tipo '{self.resource_type}' inicializado a las {self.created_at:%H:%M:%S}.")

    def use(self) -> None:
        """Simula el uso del recurso."""
        print(f"[USO] Trabajando con '{self.name}'. Estado listo para operar.")

    def __del__(self) -> None:
        # El destructor se dispara cuando el recolector de basura elimina la instancia.
        # Aquí solo mostramos un mensaje, pero en un caso real cerraría archivos o conexiones.
        print(f"[DESTRUIDO] Recurso '{self.name}' liberado; limpieza completada.")


def demo_lifecycle() -> None:
    """Crea, usa y elimina explícitamente un recurso para observar el destructor."""
    recurso = TemporaryResource(name="ConexionBD", resource_type="Base de Datos")
    recurso.use()

    print("[INFO] Eliminando la referencia principal con 'del'.")
    del recurso  # Se elimina la referencia; el objeto queda elegible para recolección.

    print("[INFO] Forzando recolección de basura con gc.collect() para ver __del__ en acción.")
    gc.collect()  # Suele ser suficiente para disparar el destructor de objetos elegibles.


if __name__ == "__main__":
    demo_lifecycle()
