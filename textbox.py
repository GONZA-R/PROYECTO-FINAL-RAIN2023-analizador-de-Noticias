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
