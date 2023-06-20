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
ventana.geometry("500x400")


#exec(open('Sitio_Ambitos.py').read())



from funciones import url_bases


# Crear lista desplegable
opciones = url_bases
combo = ttk.Combobox(ventana, values=opciones,width=30)
combo.pack(pady=40)

# Configurar evento de selección de item
combo.bind("<<ComboboxSelected>>", seleccionar_item)



if item_seleccionado == "https://www.ambito.com":
    # Realizar acciones correspondientes a la opción A
    from Sitio_Ambitos import listdiv  #Trae la lista de divs de la pagina Sitio_ambitos.py
    opciones=listdiv
elif item_seleccionado == "B":
    print("Seleccionaste la opción B")
    # Realizar acciones correspondientes a la opción B
elif item_seleccionado == "C":
    print("Seleccionaste la opción C")
    # Realizar acciones correspondientes a la opción C
else:
    print("Opción inválida")



combo2 = ttk.Combobox(ventana, values=opciones,width=30)
combo2.pack(pady=50)





# Iniciar bucle principal
ventana.mainloop()








# Imprimir el valor del item seleccionado después de cerrar la ventana
print("Valor del item seleccionado:", item_seleccionado)
"""
import tkinter as tk
from tkinter import ttk

from funciones import url_bases

# Variable global para almacenar el item seleccionado
item_seleccionado = ""
opciones_combo2 = []  # Lista de opciones para la segunda lista desplegable

def seleccionar_item(event):
    global item_seleccionado
    item_seleccionado = combo.get()
    print("Item seleccionado:", item_seleccionado)

    global opciones_combo2
    if item_seleccionado == "https://www.ambito.com":
        #from Sitio_Ambitos import listdiv  # Importar la lista de divs de la página Sitio_Ambitos
        import Sitio_Ambitos
        #from Sitio_Ambitos import web_scrapping_div
        opciones_combo2 = Sitio_Ambitos.web_scrapping_div(item_seleccionado)
    else:
        opciones_combo2 = []  # Opciones vacías si no se selecciona "https://www.ambito.com"

    # Actualizar las opciones de la segunda lista desplegable
    combo2['values'] = opciones_combo2

# Crear ventana
ventana = tk.Tk()
ventana.title("Lista Desplegable")
ventana.geometry("500x400")

# Crear lista desplegable 1
opciones = url_bases
combo = ttk.Combobox(ventana, values=opciones, width=30)
combo.pack(pady=40)

# Configurar evento de selección de item para la lista desplegable 1
combo.bind("<<ComboboxSelected>>", seleccionar_item)

# Crear lista desplegable 2
combo2 = ttk.Combobox(ventana, values=opciones_combo2, width=30)
combo2.pack(pady=50)

# Iniciar bucle principal
ventana.mainloop()

# Imprimir el valor del item seleccionado después de cerrar la ventana
print("Valor del item seleccionado:", item_seleccionado)
