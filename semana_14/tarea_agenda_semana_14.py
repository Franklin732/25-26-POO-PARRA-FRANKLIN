"""Tarea semana 14: Agenda personal GUI con Tkinter.

La aplicación permite agregar, ver y eliminar eventos/tareas programadas.

Requisitos:
- Interfaz gráfica con Treeview para mostrar eventos (fecha, hora, descripción)
- Entradas para fecha, hora y descripción
- Botones para agregar evento, eliminar seleccionado y salir
- DatePicker (tkcalendar DateEntry) para seleccionar fechas
- Organización con Frames
- Confirmación al eliminar un evento
"""

import json
import pathlib
import tkinter as tk
from tkinter import ttk, messagebox

try:
    from tkcalendar import DateEntry
except ImportError:
    DateEntry = None


class AgendaApp(tk.Tk):
    """Ventana principal de la agenda personal."""

    def __init__(self):
        super().__init__()
        self.title("Agenda Personal - Semana 14")
        self.geometry("650x450")
        self.resizable(False, False)

        # Estructura de Frames
        self._create_frames()
        # Widgets de entrada
        self._create_input_widgets()
        # Treeview de eventos
        self._create_event_tree()
        # Botones de acción
        self._create_action_buttons()

        # Archivo local para persistencia de eventos
        self.data_file = pathlib.Path(__file__).resolve().parent / "agenda_data.json"
        self._load_events()

    def _create_frames(self):
        """Crear frames para organizar la UI."""
        self.frame_eventos = ttk.LabelFrame(self, text="Eventos")
        self.frame_eventos.pack(fill="both", expand=True, padx=10, pady=(10, 5))

        self.frame_entrada = ttk.LabelFrame(self, text="Agregar nuevo evento")
        self.frame_entrada.pack(fill="x", padx=10, pady=5)

        self.frame_acciones = ttk.Frame(self)
        self.frame_acciones.pack(fill="x", padx=10, pady=(5, 10))

    def _create_input_widgets(self):
        """Crear campos para ingresar fecha, hora y descripción."""
        # Fecha
        ttk.Label(self.frame_entrada, text="Fecha:").grid(row=0, column=0, sticky="w", pady=5, padx=(10, 2))
        if DateEntry:
            self.date_entry = DateEntry(self.frame_entrada, width=14, date_pattern="yyyy-mm-dd")
        else:
            # Fallback si no hay tkcalendar disponible
            self.date_entry = ttk.Entry(self.frame_entrada)
            self.date_entry.insert(0, "YYYY-MM-DD")
        self.date_entry.grid(row=0, column=1, sticky="w", pady=5)

        # Hora
        ttk.Label(self.frame_entrada, text="Hora (HH:MM):").grid(row=0, column=2, sticky="w", pady=5, padx=(20, 2))
        self.time_entry = ttk.Entry(self.frame_entrada, width=10)
        self.time_entry.grid(row=0, column=3, sticky="w", pady=5)

        # Descripción
        ttk.Label(self.frame_entrada, text="Descripción:").grid(row=1, column=0, sticky="w", pady=5, padx=(10, 2))
        self.desc_entry = ttk.Entry(self.frame_entrada, width=50)
        self.desc_entry.grid(row=1, column=1, columnspan=3, sticky="w", pady=5)

    def _create_event_tree(self):
        """Crear Treeview que muestra la lista de eventos."""
        columns = ("fecha", "hora", "descripcion")
        self.event_tree = ttk.Treeview(
            self.frame_eventos,
            columns=columns,
            show="headings",
            selectmode="browse",
            height=10,
        )

        self.event_tree.heading("fecha", text="Fecha")
        self.event_tree.column("fecha", width=120, anchor="center")
        self.event_tree.heading("hora", text="Hora")
        self.event_tree.column("hora", width=80, anchor="center")
        self.event_tree.heading("descripcion", text="Descripción")
        self.event_tree.column("descripcion", width=400, anchor="w")

        # Barra de desplazamiento vertical
        scrollbar = ttk.Scrollbar(
            self.frame_eventos, orient="vertical", command=self.event_tree.yview
        )
        self.event_tree.configure(yscroll=scrollbar.set)
        self.event_tree.pack(side="left", fill="both", expand=True, padx=(10, 0), pady=10)
        scrollbar.pack(side="right", fill="y", padx=(0, 10), pady=10)

    def _create_action_buttons(self):
        """Agregar botones para acciones sobre los eventos."""
        self.btn_add = ttk.Button(
            self.frame_acciones, text="Agregar Evento", command=self.agregar_evento
        )
        self.btn_add.pack(side="left", padx=(0, 10))

        self.btn_delete = ttk.Button(
            self.frame_acciones, text="Eliminar Evento Seleccionado", command=self.eliminar_evento
        )
        self.btn_delete.pack(side="left", padx=(0, 10))

        self.btn_exit = ttk.Button(self.frame_acciones, text="Salir", command=self.quit)
        self.btn_exit.pack(side="right")

    def agregar_evento(self):
        """Agregar un nuevo evento a la lista (Treeview)."""
        fecha = self._get_fecha()
        hora = self.time_entry.get().strip()
        descripcion = self.desc_entry.get().strip()

        if not fecha or not hora or not descripcion:
            messagebox.showwarning(
                "Campos incompletos", "Por favor ingresa fecha, hora y descripción del evento."
            )
            return

        # Agregar al Treeview
        self.event_tree.insert("", "end", values=(fecha, hora, descripcion))

        # Guardar en disco y limpiar campos de entrada
        self._save_events()
        self._limpiar_campos()

    def _get_fecha(self) -> str:
        """Obtener la fecha del widget DateEntry o del Entry de fallback."""
        if DateEntry:
            return self.date_entry.get_date().strftime("%Y-%m-%d")
        return self.date_entry.get().strip()

    def _limpiar_campos(self):
        """Limpiar los campos de entrada para agregar un nuevo evento."""
        if DateEntry:
            self.date_entry.set_date("")
        else:
            self.date_entry.delete(0, tk.END)

        self.time_entry.delete(0, tk.END)
        self.desc_entry.delete(0, tk.END)

    def _load_events(self):
        """Cargar eventos desde el archivo JSON y mostrarlos en el Treeview."""
        if not self.data_file.exists():
            return

        try:
            with self.data_file.open("r", encoding="utf-8") as f:
                datos = json.load(f)
        except (json.JSONDecodeError, OSError):
            return

        for evento in datos:
            self.event_tree.insert(
                "", "end", values=(
                    evento.get("fecha", ""),
                    evento.get("hora", ""),
                    evento.get("descripcion", ""),
                ),
            )

    def _save_events(self):
        """Guardar los eventos actuales del Treeview en el archivo JSON."""
        eventos = []
        for item_id in self.event_tree.get_children():
            fecha, hora, descripcion = self.event_tree.item(item_id, "values")
            eventos.append({"fecha": fecha, "hora": hora, "descripcion": descripcion})

        try:
            with self.data_file.open("w", encoding="utf-8") as f:
                json.dump(eventos, f, ensure_ascii=False, indent=2)
        except OSError:
            messagebox.showerror("Error", "No se pudo guardar el archivo de datos.")

    def eliminar_evento(self):
        """Eliminar el evento seleccionado del Treeview."""
        seleccionado = self.event_tree.selection()
        if not seleccionado:
            messagebox.showinfo("Eliminar evento", "Selecciona primero un evento de la lista.")
            return

        item_id = seleccionado[0]
        valores = self.event_tree.item(item_id, "values")
        pregunta = (
            f"¿Seguro que deseas eliminar el evento:\n\n"
            f"Fecha: {valores[0]}\nHora: {valores[1]}\nDescripción: {valores[2]}"
        )

        if messagebox.askyesno("Confirmar eliminación", pregunta):
            self.event_tree.delete(item_id)
            self._save_events()


def main():
    app = AgendaApp()
    app.mainloop()


if __name__ == "__main__":
    main()
