"""
import tkinter as tk

def seleccionar_elemento(event):
    # Obtener el índice del elemento seleccionado
    indice = lista.curselection()
    if indice:
        elemento_seleccionado = lista.get(indice)
        print("Elemento seleccionado:", elemento_seleccionado)

# Crear la ventana principal
ventana = tk.Tk()

# Crear la lista de texto
lista = tk.Listbox(ventana)
lista.pack()

# Agregar elementos a la lista
elementos = ["Elemento 1", "Elemento 2", "Elemento 3", "Elemento 4"]
for elemento in elementos:
    lista.insert(tk.END, elemento)

# Asociar la función de selección al evento de doble clic en un elemento
lista.bind("<Double-Button-1>", seleccionar_elemento)

# Ejecutar el bucle principal de la ventana
ventana.mainloop()
"""
import tkinter as tk
from tkinter import scrolledtext, messagebox

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Seleccionar elementos del TextBox")

# Definir lista de elementos
lista_elementos = ["Elemento 1", "Elemento 2", "Elemento 3"]

# Función para obtener la selección
def obtener_seleccion():
    seleccionados = text_box.selection_get().split("\n")
    messagebox.showinfo("Elementos seleccionados", f"Elementos seleccionados: {', '.join(seleccionados)}")

# Crear TextBox
text_box = scrolledtext.ScrolledText(ventana, width=40, height=10)
text_box.pack(padx=10, pady=10)

# Cargar elementos en el TextBox
for elemento in lista_elementos:
    text_box.insert(tk.END, elemento + "\n")

# Botón para obtener la selección
boton_obtener_seleccion = tk.Button(ventana, text="Obtener selección", command=obtener_seleccion)
boton_obtener_seleccion.pack(pady=10)

# Iniciar bucle principal
ventana.mainloop()

