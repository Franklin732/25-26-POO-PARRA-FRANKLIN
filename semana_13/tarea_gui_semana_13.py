"""Tarea Semana 13 - Aplicación GUI Básica (Tkinter)

Descripción:
Este programa crea una aplicación de escritorio con una interfaz gráfica
que permite al usuario agregar entradas de texto a una lista, verlas en una
lista gráfica y limpiar la entrada o la lista completa.

Requisitos cumplidos:
- Ventana principal con título descriptivo.
- Uso de labels, buttons, entry (campo de texto) y listbox (lista de datos).
- Botón "Agregar" para adicionar datos desde el campo de texto a la lista.
- Botón "Limpiar" para borrar la entrada activa o la lista completa.
- Botones "Guardar" y "Cargar" para persistencia en disco.
- Manejo de eventos de clic.

Cómo usar:
1) Ejecute el script: python tarea_gui_semana_13.py
2) Escriba texto en el campo y presione "Agregar".
3) Seleccione un elemento y presione "Limpiar" para borrarlo.
4) Presione "Limpiar todo" para vaciar la lista completa.

Notas de diseño:
- Se utiliza un layout con grid para posicionar componentes en filas/columnas.
- La lista (Listbox) muestra los datos ingresados, permitiendo selección.
- Se validan entradas vacías para evitar agregar textos vacíos.
"""

import tkinter as tk
from tkinter import messagebox
from pathlib import Path


class AplicacionGUI:
    """Clase principal de la aplicación GUI."""

    def __init__(self, root: tk.Tk):
        """Inicializa la ventana principal y configura los componentes."""
        self.root = root
        self.root.title("Tarea Semana 13 - GUI Básica")
        self.root.resizable(False, False)

        # --- Archivo de datos ---
        self._data_file = Path(__file__).resolve().parent / "datos.txt"

        # --- Diseño y componentes ---
        self._crear_widgets()
        self._configurar_layout()

        # Cargar datos si existe el archivo
        self._cargar_lista()

    def _crear_widgets(self) -> None:
        """Crea los widgets de la interfaz."""
        self.lbl_instruccion = tk.Label(
            self.root, text="Ingresa un dato y presiona Agregar:", font=("Segoe UI", 10)
        )

        self.entry_dato = tk.Entry(self.root, width=40)

        self.btn_agregar = tk.Button(
            self.root, text="Agregar", width=12, command=self._agregar_dato
        )

        self.btn_limpiar = tk.Button(
            self.root, text="Limpiar selección", width=15, command=self._limpiar_seleccion
        )

        self.btn_limpiar_todo = tk.Button(
            self.root, text="Limpiar todo", width=15, command=self._limpiar_todo
        )

        self.btn_guardar = tk.Button(
            self.root, text="Guardar lista", width=15, command=self._guardar_lista
        )

        self.btn_cargar = tk.Button(
            self.root, text="Cargar lista", width=15, command=self._cargar_lista
        )

        self.lista_datos = tk.Listbox(self.root, width=55, height=10, activestyle="none")

        # Barra de scroll para la lista
        self.scroll_lista = tk.Scrollbar(self.root, command=self.lista_datos.yview)
        self.lista_datos.configure(yscrollcommand=self.scroll_lista.set)

    def _configurar_layout(self) -> None:
        """Organiza los widgets en la ventana usando grid."""
        # Fila 0: etiqueta
        self.lbl_instruccion.grid(row=0, column=0, columnspan=3, padx=12, pady=(12, 4), sticky="w")

        # Fila 1: campo de texto y botón Agregar
        self.entry_dato.grid(row=1, column=0, columnspan=2, padx=(12, 4), pady=4, sticky="we")
        self.btn_agregar.grid(row=1, column=2, padx=(4, 12), pady=4)

        # Fila 2: lista y scroll
        self.lista_datos.grid(row=2, column=0, columnspan=2, padx=(12, 0), pady=4, sticky="nsew")
        self.scroll_lista.grid(row=2, column=2, padx=(4, 12), pady=4, sticky="ns")

        # Fila 3: botones de limpiar
        self.btn_limpiar.grid(row=3, column=0, padx=12, pady=(4, 12), sticky="w")
        self.btn_limpiar_todo.grid(row=3, column=1, padx=12, pady=(4, 12), sticky="w")

        # Fila 4: guardar/cargar
        self.btn_guardar.grid(row=4, column=0, padx=12, pady=(0, 12), sticky="w")
        self.btn_cargar.grid(row=4, column=1, padx=12, pady=(0, 12), sticky="w")

        # Configurar columna 0 y 1 para expandirse con la ventana
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)

    def _agregar_dato(self) -> None:
        """Agrega el texto del entry a la lista, validando que no esté vacío."""
        texto = self.entry_dato.get().strip()
        if not texto:
            messagebox.showwarning(
                "Entrada vacía", "Por favor ingresa algún texto antes de agregar."
            )
            return

        self.lista_datos.insert(tk.END, texto)
        self.entry_dato.delete(0, tk.END)
        self.entry_dato.focus()

    def _limpiar_seleccion(self) -> None:
        """Elimina el elemento seleccionado en la lista."""
        seleccion = self.lista_datos.curselection()
        if not seleccion:
            messagebox.showinfo(
                "Sin selección", "Selecciona un elemento en la lista para eliminar."
            )
            return

        # Eliminar desde el índice más alto hacia abajo para evitar reindexado
        for idx in reversed(seleccion):
            self.lista_datos.delete(idx)

    def _limpiar_todo(self) -> None:
        """Limpia todos los elementos de la lista."""
        if self.lista_datos.size() == 0:
            messagebox.showinfo("Lista vacía", "No hay elementos para limpiar.")
            return

        confirmar = messagebox.askyesno(
            "Confirmar", "¿Deseas borrar todos los elementos de la lista?"
        )
        if confirmar:
            self.lista_datos.delete(0, tk.END)

    def _guardar_lista(self) -> None:
        """Guarda el contenido de la lista en un archivo de texto."""
        try:
            with open(self._data_file, "w", encoding="utf-8") as f:
                for i in range(self.lista_datos.size()):
                    f.write(self.lista_datos.get(i) + "\n")
            messagebox.showinfo("Guardado", "Lista guardada correctamente.")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo guardar el archivo:\n{e}")

    def _cargar_lista(self) -> None:
        """Carga el contenido del archivo en la lista (si existe)."""
        if not self._data_file.exists():
            return

        try:
            self.lista_datos.delete(0, tk.END)
            with open(self._data_file, "r", encoding="utf-8") as f:
                for linea in f:
                    texto = linea.rstrip("\n")
                    if texto:
                        self.lista_datos.insert(tk.END, texto)
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo cargar el archivo:\n{e}")


def main() -> None:
    """Punto de entrada del programa."""
    root = tk.Tk()
    app = AplicacionGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
