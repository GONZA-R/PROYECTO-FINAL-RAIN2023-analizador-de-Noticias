"""Análisis de noticias según un tema en particular, a partir de una búsqueda, realizada sobre 10 sitios de diarios digitales."""

import tkinter as tk
from tkinter import ttk

def iniciar():
    print("¡El botón de inicio ha sido presionado!")

# Crear una ventana
ventana = tk.Tk()
# Establecer el tamaño de la ventana
ventana.geometry("750x500")
# Cambiar el color de fondo de la ventana
ventana.configure(bg="lightblue")

# Crear un botón de inicio
boton_inicio = tk.Button(ventana, text="Iniciar", command=iniciar, width=10, height=2)
boton_inicio.place(relx=0.5, rely=0.5, anchor=tk.CENTER)



# Crear una etiqueta para el texto
etiqueta = ttk.Label(ventana, text="Proyecto Final RAIN 2023", foreground="blue", font=("Arial", 28))
etiqueta.place(relx=0.5, rely=0.3, anchor=tk.CENTER)



# Ejecutar el bucle principal de la ventana
ventana.mainloop()
