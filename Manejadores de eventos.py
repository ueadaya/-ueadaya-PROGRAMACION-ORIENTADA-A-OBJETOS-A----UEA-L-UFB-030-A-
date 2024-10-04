import tkinter as tk
from tkinter import messagebox, Listbox, Scrollbar, END

class TaskManagerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Gestor de Tareas")

        # Campo de entrada
        self.task_input = tk.Entry(master, width=40)
        self.task_input.pack(pady=10)

        # Botones
        self.add_task_button = tk.Button(master, text="Añadir Tarea", command=self.add_task)
        self.add_task_button.pack(pady=5)

        self.complete_task_button = tk.Button(master, text="Marcar como Completada", command=self.complete_task)
        self.complete_task_button.pack(pady=5)

        self.delete_task_button = tk.Button(master, text="Eliminar Tarea", command=self.delete_task)
        self.delete_task_button.pack(pady=5)

        # Lista de tareas
        self.task_listbox = Listbox(master, selectmode=tk.SINGLE, width=50, height=10)
        self.task_listbox.pack(pady=10)

        # Scrollbar para la lista de tareas
        self.scrollbar = Scrollbar(master)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.task_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.task_listbox.yview)

        # Bindings de teclado
        self.master.bind("<Return>", self.add_task_event)
        self.master.bind("<c>", self.complete_task_event)
        self.master.bind("<Delete>", self.delete_task_event)
        self.master.bind("<Escape>", self.close_app)

    def add_task(self):
        task = self.task_input.get()
        if task:
            self.task_listbox.insert(END, task)
            self.task_input.delete(0, END)  # Limpiar el campo de entrada
        else:
            messagebox.showwarning("Advertencia", "Por favor, introduce una tarea.")

    def add_task_event(self, event):
        self.add_task()

    def complete_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            task = self.task_listbox.get(selected_task_index)
            completed_task = f"{task} (Completada)"
            self.task_listbox.delete(selected_task_index)
            self.task_listbox.insert(selected_task_index, completed_task)
        except IndexError:
            messagebox.showwarning("Advertencia", "Por favor, selecciona una tarea para marcar como completada.")

    def complete_task_event(self, event):
        self.complete_task()

    def delete_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            self.task_listbox.delete(selected_task_index)
        except IndexError:
            messagebox.showwarning("Advertencia", "Por favor, selecciona una tarea para eliminar.")

    def delete_task_event(self, event):
        self.delete_task()

    def close_app(self, event):
        self.master.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.mainloop()
