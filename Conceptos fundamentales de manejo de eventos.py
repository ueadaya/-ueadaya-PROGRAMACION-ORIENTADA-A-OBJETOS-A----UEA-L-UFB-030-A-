import tkinter as tk
from tkinter import messagebox

# Crear la ventana principal
root = tk.Tk()
root.title("Lista de Tareas")
root.geometry("400x400")

# Función para añadir una tarea
def add_task(event=None):
    task = task_entry.get()
    if task:
        tasks_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "No se puede añadir una tarea vacía.")

# Función para marcar una tarea como completada
def mark_completed():
    try:
        selected_index = tasks_listbox.curselection()[0]
        task = tasks_listbox.get(selected_index)
        tasks_listbox.delete(selected_index)
        tasks_listbox.insert(tk.END, f"[Completada] {task}")
    except IndexError:
        messagebox.showwarning("Advertencia", "Seleccione una tarea para marcar como completada.")

# Función para eliminar una tarea
def delete_task():
    try:
        selected_index = tasks_listbox.curselection()[0]
        tasks_listbox.delete(selected_index)
    except IndexError:
        messagebox.showwarning("Advertencia", "Seleccione una tarea para eliminar.")

# Campo de entrada para nuevas tareas
task_entry = tk.Entry(root, width=40)
task_entry.pack(pady=10)
task_entry.bind("<Return>", add_task)  # Permitir añadir tarea al presionar Enter

# Botones para añadir, marcar completada y eliminar tareas
button_frame = tk.Frame(root)
button_frame.pack()

add_button = tk.Button(button_frame, text="Añadir Tarea", command=add_task)
add_button.grid(row=0, column=0, padx=5)

mark_button = tk.Button(button_frame, text="Marcar como Completada", command=mark_completed)
mark_button.grid(row=0, column=1, padx=5)

delete_button = tk.Button(button_frame, text="Eliminar Tarea", command=delete_task)
delete_button.grid(row=0, column=2, padx=5)

# Listbox para mostrar las tareas actuales
tasks_listbox = tk.Listbox(root, width=50, height=15, selectmode=tk.SINGLE)
tasks_listbox.pack(pady=10)

# Iniciar el bucle principal de la aplicación
root.mainloop()
