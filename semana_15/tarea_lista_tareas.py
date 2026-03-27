"""Aplicación de lista de tareas usando Tkinter.
Permite al usuario añadir tareas, marcarlas como completadas y eliminarlas.
"""

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class ListaTareasApp:
    """Clase principal de la aplicación de tareas."""

    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Lista de Tareas - Semana 15")
        self.root.geometry("420x380")
        self.root.resizable(False, False)

        # Modelo de datos: lista de tuplas (texto, completada)
        self.tareas = []

        self._crear_widgets()
        self._conectar_eventos()

    def _crear_widgets(self) -> None:
        """Crear los widgets de la interfaz y organizarlos en el contenedor."""
        main_frame = ttk.Frame(self.root, padding=12)
        main_frame.pack(fill=tk.BOTH, expand=True)

        title_label = ttk.Label(main_frame, text="Gestor de Tareas", font=("Segoe UI", 14, "bold"))
        title_label.pack(pady=(0, 10))

        entry_frame = ttk.Frame(main_frame)
        entry_frame.pack(fill=tk.X, pady=(0, 10))

        self.tarea_entry = ttk.Entry(entry_frame)
        self.tarea_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 6))
        self.tarea_entry.focus()

        self.btn_anadir = ttk.Button(entry_frame, text="Añadir Tarea")
        self.btn_anadir.pack(side=tk.RIGHT)

        self.lista_tareas = tk.Listbox(main_frame, height=12, activestyle="none", selectmode=tk.SINGLE)
        self.lista_tareas.pack(fill=tk.BOTH, expand=True, pady=(0, 10))

        botones_frame = ttk.Frame(main_frame)
        botones_frame.pack(fill=tk.X)

        self.btn_completar = ttk.Button(botones_frame, text="Marcar como Completada")
        self.btn_completar.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 6))

        self.btn_eliminar = ttk.Button(botones_frame, text="Eliminar Tarea")
        self.btn_eliminar.pack(side=tk.RIGHT, fill=tk.X, expand=True)

        ayuda_label = ttk.Label(main_frame,
                                text="Presiona Enter para añadir tarea. Doble clic para alternar completado.",
                                font=("Segoe UI", 8), foreground="gray")
        ayuda_label.pack(pady=(8, 0))

    def _conectar_eventos(self) -> None:
        """Conectar los eventos de los widgets a los manejadores."""
        self.btn_anadir.config(command=self.anadir_tarea)
        self.btn_completar.config(command=self.completar_tarea)
        self.btn_eliminar.config(command=self.eliminar_tarea)
        self.tarea_entry.bind("<Return>", self._evento_entrada)
        self.lista_tareas.bind("<Double-Button-1>", self._doble_clic_tarea)

    def anadir_tarea(self) -> None:
        """Agregar una tarea nueva a la lista y actualizar la vista."""
        texto = self.tarea_entry.get().strip()
        if not texto:
            messagebox.showinfo("Atención", "Escribe una tarea antes de añadirla.")
            return

        self.tareas.append((texto, False))
        self.tarea_entry.delete(0, tk.END)
        self._actualizar_lista()

    def _evento_entrada(self, event: tk.Event) -> None:
        """Manejador para la tecla Enter en el campo de entrada."""
        self.anadir_tarea()

    def _doble_clic_tarea(self, event: tk.Event) -> None:
        """Alternar el estado completado al hacer doble clic sobre una tarea."""
        self.completar_tarea()

    def completar_tarea(self) -> None:
        """Marcar la tarea seleccionada como completada o pendiente."""
        indice = self._obtener_indice_seleccionado()
        if indice is None:
            messagebox.showwarning("Seleccionar tarea", "Seleccione una tarea para marcarla como completada.")
            return

        texto, completada = self.tareas[indice]
        self.tareas[indice] = (texto, not completada)
        self._actualizar_lista()

    def eliminar_tarea(self) -> None:
        """Eliminar la tarea seleccionada de la lista."""
        indice = self._obtener_indice_seleccionado()
        if indice is None:
            messagebox.showwarning("Seleccionar tarea", "Seleccione una tarea para eliminarla.")
            return

        del self.tareas[indice]
        self._actualizar_lista()

    def _obtener_indice_seleccionado(self) -> int | None:
        """Retornar el índice de la tarea seleccionada o None si no hay selección."""
        seleccion = self.lista_tareas.curselection()
        if not seleccion:
            return None
        return seleccion[0]

    def _actualizar_lista(self) -> None:
        """Refrescar los elementos visibles en el Listbox con el estado actualizado."""
        self.lista_tareas.delete(0, tk.END)
        for texto, completada in self.tareas:
            item_text = texto
            if completada:
                item_text = f"✓ {texto}"
            self.lista_tareas.insert(tk.END, item_text)

            if completada:
                self.lista_tareas.itemconfig(tk.END, fg="green")


def main() -> None:
    """Punto de entrada para ejecutar la aplicación."""
    root = tk.Tk()
    app = ListaTareasApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
