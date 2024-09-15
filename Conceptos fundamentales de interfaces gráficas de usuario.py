import tkinter as tk
from tkinter import messagebox

# Función para agregar el texto ingresado a la lista
def agregar_dato():
    dato = entrada_texto.get()
    if dato:  # Verifica que el campo no esté vacío
        lista_datos.insert(tk.END, dato)
        entrada_texto.delete(0, tk.END)  # Limpia el campo de texto
    else:
        messagebox.showwarning("Advertencia", "El campo está vacío.")

# Función para limpiar la lista
def limpiar_lista():
    lista_datos.delete(0, tk.END)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Aplicación GUI Básica")

# Etiqueta para el campo de texto
label = tk.Label(ventana, text="Ingresa un dato:")
label.pack(pady=10)

# Campo de texto para ingresar datos
entrada_texto = tk.Entry(ventana, width=30)
entrada_texto.pack(pady=10)

# Botón para agregar el dato ingresado a la lista
boton_agregar = tk.Button(ventana, text="Agregar", command=agregar_dato)
boton_agregar.pack(pady=5)

# Lista para mostrar los datos ingresados
lista_datos = tk.Listbox(ventana, width=50, height=10)
lista_datos.pack(pady=10)

# Botón para limpiar la lista
boton_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar_lista)
boton_limpiar.pack(pady=5)

# Ejecutar la ventana principal
ventana.mainloop()
