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
"""
"""

import tkinter as tk
from tkinter import ttk

# Opciones de la primera lista desplegable

from funciones import url_bases
opciones_lista1 = ["Opción 1", "Opción 2", "Opción 3"]
opciones_lista1=list(url_bases)



# Diccionario de opciones para la segunda lista desplegable
opciones_dict = {
    "https://www.ambito.com": ["Elemento 1-1", "Elemento 1-2", "Elemento 1-3"],
    "Opción 2": ["Elemento 2-1", "Elemento 2-2", "Elemento 2-3"],
    "Opción 3": ["Elemento 3-1", "Elemento 3-2", "Elemento 3-3"]
}



def seleccionar_opcion_lista1(event):
    # Obtener la opción seleccionada de la primera lista
    opcion_seleccionada = combo_lista1.get()

    # Enviar la opción seleccionada a una función
    mi_funcion(opcion_seleccionada)

    # Obtener los elementos correspondientes de la segunda lista
    opciones_lista2 = opciones_dict.get(opcion_seleccionada, [])

    # Actualizar las opciones de la segunda lista desplegable
    combo_lista2['values'] = opciones_lista2


def seleccionar_opcion_lista2(event):
    # Obtener la opción seleccionada de la segunda lista
    opcion_seleccionada = combo_lista2.get()

    # Enviar la opción seleccionada a una función
    mi_funcion(opcion_seleccionada)



def mi_funcion(opcion_seleccionada):
    # Realizar acciones con la opción seleccionada

    print("Opción seleccionada:", opcion_seleccionada)

# Crear ventana
ventana = tk.Tk()
ventana.title("Listas Desplegables")

# Crear primera lista desplegable
combo_lista1 = ttk.Combobox(ventana, values=opciones_lista1)
combo_lista1.pack(pady=10)

# Configurar evento de selección para la primera lista desplegable
combo_lista1.bind("<<ComboboxSelected>>", seleccionar_opcion_lista1)

# Crear segunda lista desplegable
combo_lista2 = ttk.Combobox(ventana)
combo_lista2.pack(pady=10)

# Configurar evento de selección para la segunda lista desplegable
combo_lista2.bind("<<ComboboxSelected>>", seleccionar_opcion_lista2)

# Iniciar bucle principal
ventana.mainloop()
"""

import tkinter as tk
from tkinter import ttk

# Opciones de la primera lista desplegable
#opciones_lista1 = ["Opción 1", "Opción 2", "Opción 3"]
from funciones import url_bases
#opciones_lista1 = ["Opción 1", "Opción 2", "Opción 3"]
opciones_lista1=list(url_bases)


# Diccionario de opciones para la segunda lista desplegable
opciones_dict = {}

def seleccionar_opcion_lista1(event):
    # Obtener la opción seleccionada de la primera lista
    opcion_seleccionada = combo_lista1.get()

    # Obtener los elementos correspondientes para la segunda lista
    opciones_lista2 = obtener_opciones_lista2(opcion_seleccionada)

    # Actualizar las opciones de la segunda lista desplegable
    combo_lista2['values'] = opciones_lista2

def obtener_opciones_lista2(opcion_seleccionada):
    # Obtener los elementos correspondientes para la segunda lista según la opción seleccionada
    # Aquí puedes implementar la lógica para obtener las opciones de la segunda lista
    # Puedes realizar consultas a una base de datos, leer un archivo, hacer cálculos, etc.

    # Ejemplo: llenar el diccionario opciones_dict a partir de la opción seleccionada
    if opcion_seleccionada == "https://www.ambito.com":
        #from Sitio_Ambitos import web_scrapping_div
        from Sitio_Ambitos2 import web_scrapping_div
        #import Sitio_Ambitos

        #from Sitio_Ambitos import listdiv
        opciones_dict[opcion_seleccionada] = web_scrapping_div(opcion_seleccionada)

    elif opcion_seleccionada == "https://www.eldestapeweb.com":
        from Sitio_Eldestape2 import web_scrapping_div
        opciones_dict[opcion_seleccionada] = web_scrapping_div(opcion_seleccionada)
    elif opcion_seleccionada == "Opción 3":
        opciones_dict[opcion_seleccionada] = ["Elemento 3-1", "Elemento 3-2", "Elemento 3-3"]

    # Devolver los elementos correspondientes para la segunda lista
    return opciones_dict.get(opcion_seleccionada, [])

# Crear ventana
ventana = tk.Tk()
ventana.title("Listas Desplegables")

# Crear primera lista desplegable
combo_lista1 = ttk.Combobox(ventana, values=opciones_lista1)
combo_lista1.pack(pady=10)

# Configurar evento de selección para la primera lista desplegable
combo_lista1.bind("<<ComboboxSelected>>", seleccionar_opcion_lista1)

# Crear segunda lista desplegable
combo_lista2 = ttk.Combobox(ventana)
combo_lista2.pack(pady=10)

# Iniciar bucle principal
ventana.mainloop()
