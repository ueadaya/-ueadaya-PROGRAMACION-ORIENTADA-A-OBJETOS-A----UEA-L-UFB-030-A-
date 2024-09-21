import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry  # Asegúrate de tener instalado 'tkcalendar'

class AgendaApp:
    def __init__(self, root):
        """Inicializa la ventana principal y todos los widgets."""
        self.root = root
        self.root.title("Agenda Personal")

        # --- Frame para la lista de eventos ---
        self.frame_list = tk.Frame(root)
        self.frame_list.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        # --- Frame para la entrada de datos (Fecha, Hora, Descripción) ---
        self.frame_entry = tk.Frame(root)
        self.frame_entry.pack(padx=10, pady=10, fill=tk.X)

        # --- Frame para los botones (Agregar, Eliminar, Salir) ---
        self.frame_actions = tk.Frame(root)
        self.frame_actions.pack(padx=10, pady=10, fill=tk.X)

        # --- Configuración de TreeView para mostrar los eventos ---
        self.tree = ttk.Treeview(self.frame_list, columns=("Fecha", "Hora", "Descripción"), show='headings')
        self.tree.heading("Fecha", text="Fecha")
        self.tree.heading("Hora", text="Hora")
        self.tree.heading("Descripción", text="Descripción")
        self.tree.pack(fill=tk.BOTH, expand=True)

        # --- Configuración de los campos de entrada ---
        # Etiqueta y campo de selección de fecha
        tk.Label(self.frame_entry, text="Fecha").grid(row=0, column=0, padx=5, pady=5)
        self.date_entry = DateEntry(self.frame_entry, width=12)  # Utiliza un widget de calendario para la selección de fechas
        self.date_entry.grid(row=0, column=1, padx=5, pady=5)

        # Etiqueta y campo de entrada de la hora
        tk.Label(self.frame_entry, text="Hora").grid(row=1, column=0, padx=5, pady=5)
        self.time_entry = tk.Entry(self.frame_entry)  # Entrada para la hora del evento
        self.time_entry.grid(row=1, column=1, padx=5, pady=5)

        # Etiqueta y campo de entrada de la descripción
        tk.Label(self.frame_entry, text="Descripción").grid(row=2, column=0, padx=5, pady=5)
        self.desc_entry = tk.Entry(self.frame_entry)  # Entrada para la descripción del evento
        self.desc_entry.grid(row=2, column=1, padx=5, pady=5)

        # --- Botones para agregar, eliminar y salir ---
        tk.Button(self.frame_actions, text="Agregar Evento", command=self.add_event).pack(side=tk.LEFT, padx=5, pady=5)
        tk.Button(self.frame_actions, text="Eliminar Evento Seleccionado", command=self.delete_event).pack(side=tk.LEFT, padx=5, pady=5)
        tk.Button(self.frame_actions, text="Salir", command=root.quit).pack(side=tk.RIGHT, padx=5, pady=5)

    def add_event(self):
        """Agrega un nuevo evento a la lista (TreeView) si todos los campos están completos."""
        date = self.date_entry.get()  # Obtener la fecha seleccionada
        time = self.time_entry.get()  # Obtener la hora ingresada
        description = self.desc_entry.get()  # Obtener la descripción ingresada

        # Verificar que todos los campos estén completos
        if date and time and description:
            # Insertar los datos en la lista de eventos (TreeView)
            self.tree.insert("", tk.END, values=(date, time, description))
            # Limpiar los campos de entrada
            self.time_entry.delete(0, tk.END)
            self.desc_entry.delete(0, tk.END)
        else:
            # Mostrar advertencia si faltan datos
            messagebox.showwarning("Advertencia", "Por favor, rellena todos los campos.")

    def delete_event(self):
        """Elimina el evento seleccionado de la lista, con confirmación del usuario."""
        selected_item = self.tree.selection()  # Obtener el evento seleccionado
        if selected_item:
            # Confirmar si el usuario desea eliminar el evento
            if messagebox.askyesno("Confirmación", "¿Estás seguro de que deseas eliminar el evento seleccionado?"):
                self.tree.delete(selected_item)  # Eliminar el evento
        else:
            # Mostrar advertencia si no hay selección
            messagebox.showwarning("Advertencia", "Selecciona un evento para eliminar.")

if __name__ == "__main__":
    root = tk.Tk()  # Crear la ventana principal de la aplicación
    app = AgendaApp(root)  # Instanciar la clase de la aplicación
    root.mainloop()  # Ejecutar el bucle principal de la interfaz gráfica
