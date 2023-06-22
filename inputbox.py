"""
import tkinter as tk

# Crear ventana
ventana = tk.Tk()

# Función para obtener el valor del cuadro de diálogo de entrada
def obtener_valor():
    valor = cuadro_texto.get()
    cargar_valor(valor)

# Función para cargar el valor en otra función
def cargar_valor(valor):
    print("Valor cargado:", valor)

# Función para borrar el contenido del cuadro de texto
def borrar_contenido():
    cuadro_texto.delete(0, tk.END)

# Crear cuadro de texto de entrada
cuadro_texto = tk.Entry(ventana)
cuadro_texto.pack()

# Crear botón para obtener el valor del cuadro de texto
boton_cargar = tk.Button(ventana, text="Cargar", command=obtener_valor)
boton_cargar.pack()

# Crear botón para borrar el contenido del cuadro de texto
boton_borrar = tk.Button(ventana, text="Borrar", command=borrar_contenido)
boton_borrar.pack()

# Iniciar bucle principal
ventana.mainloop()
"""

import tkinter as tk

# Crear ventana
ventana = tk.Tk()

# Variable global para almacenar el valor cargado
valor_cargado = ""

# Función para obtener el valor del cuadro de diálogo de entrada
def obtener_valor():
    valor = cuadro_texto.get()
    cargar_valor(valor)

# Función para cargar el valor en la variable global y en el cuadro de texto de salida
def cargar_valor(valor):
    global valor_cargado  # Acceder a la variable global
    valor_cargado = valor
    cuadro_salida.delete("1.0", tk.END)  # Borrar contenido actual del cuadro de salida
    cuadro_salida.insert(tk.END, "Valor cargado: " + valor)
    otra_funcion()

# Función para borrar el contenido del cuadro de texto
def borrar_contenido():
    cuadro_salida.delete("1.0", tk.END)
    cuadro_texto.delete(0, tk.END)
    global valor_cargado  # Acceder a la variable global
    valor_cargado = ""

# Crear cuadro de texto de entrada
cuadro_texto = tk.Entry(ventana)
cuadro_texto.pack()

# Crear botón para obtener el valor del cuadro de texto
boton_cargar = tk.Button(ventana, text="Cargar", command=obtener_valor)
boton_cargar.pack()

# Crear botón para borrar el contenido del cuadro de texto
boton_borrar = tk.Button(ventana, text="Borrar", command=borrar_contenido)
boton_borrar.pack()

# Crear cuadro de texto de salida
cuadro_salida = tk.Text(ventana, height=5, width=30)
cuadro_salida.pack()

# Función que utiliza el valor cargado en la variable global
def otra_funcion():
    global valor_cargado
    print("Valor cargado:", valor_cargado)




# Iniciar bucle principal
ventana.mainloop()
