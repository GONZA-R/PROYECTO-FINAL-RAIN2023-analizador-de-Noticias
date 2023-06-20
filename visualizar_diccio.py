
"""

import tkinter as tk

ventana1 = None  # Declarar la variable ventana1 como global

def mostrar_principal():
    ventana_principal.deiconify()  # Mostrar la ventana principal
    ventana1.destroy()  # Cerrar la ventana 1

def mostrar_ventana1():
    global ventana1  # Declarar la variable ventana1 como global
    ventana_principal.withdraw()  # Ocultar la ventana principal
    ventana1 = tk.Toplevel(ventana_principal)
    ventana1.title("Ventana 1")
    ventana1.geometry("500x400")
    ventana1.resizable(False, False)
    
    btn_volver = tk.Button(ventana1, text="Volver", command=mostrar_principal)
    btn_volver.pack(pady=10)

    btn2_ventana1= tk.Button(ventana1,text="Noticias",command=mostrar_principal)
    btn2_ventana1.pack(pady=20)



ventana_principal = tk.Tk()
ventana_principal.title("Ventana Principal")
ventana_principal.geometry("400x300")
ventana_principal.resizable(False, False)

btn_ventana1 = tk.Button(ventana_principal, text="Ir a Ventana 1", command=mostrar_ventana1)
btn_ventana1.pack(pady=10)


ventana_principal.mainloop()

"""



import tkinter as tk
from tkinter import ttk

# Variable global para almacenar el item seleccionado
item_seleccionado = ""

def seleccionar_item(event):
    global item_seleccionado
    item_seleccionado = combo.get()
    print("Item seleccionado:", item_seleccionado)

# Crear ventana
ventana = tk.Tk()
ventana.title("Lista Desplegable")
ventana.geometry("300x200")


#exec(open('Sitio_Ambitos.py').read())

#from Sitio_Ambitos import listdiv  #Trae la lista de divs de la pagina Sitio_ambitos.py

from funciones import url_bases


# Crear lista desplegable
opciones = url_bases
combo = ttk.Combobox(ventana, values=opciones,width=30)
combo.pack(pady=40)


# Configurar evento de selección de item
combo.bind("<<ComboboxSelected>>", seleccionar_item)


# Iniciar bucle principal
ventana.mainloop()

# Imprimir el valor del item seleccionado después de cerrar la ventana
print("Valor del item seleccionado:", item_seleccionado)




"""
import tkinter as tk

# Crear la ventana principal
ventana = tk.Tk()

# Configurar el fondo blanco
ventana.configure(bg="white")

# Crear el cuadro de texto
texto = "Esta es una noticia muy importante que desea mostrar."
cuadro_texto = tk.Text(ventana, height=10, width=50, bg="white")
cuadro_texto.insert(tk.END, texto)
cuadro_texto.pack()

# Ejecutar el bucle principal de la ventana
ventana.mainloop()
"""