import tkinter as tk
from tkinter import messagebox

class TaskManagerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Tareas")
        self.root.geometry("480x420")

        self.frame = tk.Frame(self.root)
        self.frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.entry = tk.Entry(self.frame, font=("Arial", 12))
        self.entry.pack(fill=tk.X, pady=5)
        self.entry.focus_set()

        self.button_add = tk.Button(self.frame, text="Añadir tarea", command=self.add_task, bg="#4caf50", fg="white")
        self.button_add.pack(fill=tk.X, pady=5)

        self.listbox = tk.Listbox(self.frame, selectmode=tk.SINGLE, font=("Arial", 12), activestyle="dotbox", height=15)
        self.listbox.pack(fill=tk.BOTH, expand=True, pady=5)

        self.button_complete = tk.Button(self.frame, text="Marcar como completada", command=self.complete_task, bg="#2196f3", fg="white")
        self.button_complete.pack(fill=tk.X, pady=3)

        self.button_delete = tk.Button(self.frame, text="Eliminar tarea", command=self.delete_task, bg="#f44336", fg="white")
        self.button_delete.pack(fill=tk.X, pady=3)

        self.status = tk.Label(self.root, text="Atajos: Enter=Agregar | C=Completar | D=Eliminar | Esc=Salir", anchor="w")
        self.status.pack(fill=tk.X, padx=10, pady=(0, 10))

        self.root.bind('<Return>', lambda event: self.add_task())
        self.root.bind('<c>', lambda event: self.complete_task())
        self.root.bind('<C>', lambda event: self.complete_task())
        self.root.bind('<d>', lambda event: self.delete_task())
        self.root.bind('<D>', lambda event: self.delete_task())
        self.root.bind('<Delete>', lambda event: self.delete_task())
        self.root.bind('<Escape>', lambda event: self.root.quit())

    def add_task(self):
        task_text = self.entry.get().strip()
        if task_text:
            self.listbox.insert(tk.END, task_text)
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Entrada vacía", "Escribe una tarea antes de agregar.")

    def complete_task(self):
        selected = self.listbox.curselection()
        if not selected:
            messagebox.showinfo("Sin selección", "Selecciona primero una tarea.")
            return

        idx = selected[0]
        task = self.listbox.get(idx)
        if task.endswith(' ✅'):
            messagebox.showinfo("Ya completada", "La tarea ya está marcada como completada.")
            return

        self.listbox.delete(idx)
        self.listbox.insert(idx, task + ' ✅')
        self.listbox.itemconfig(idx, fg='gray')

    def delete_task(self):
        selected = self.listbox.curselection()
        if not selected:
            messagebox.showinfo("Sin selección", "Selecciona primero una tarea.")
            return

        idx = selected[0]
        self.listbox.delete(idx)


if __name__ == '__main__':
    root = tk.Tk()
    app = TaskManagerGUI(root)
    root.mainloop()
