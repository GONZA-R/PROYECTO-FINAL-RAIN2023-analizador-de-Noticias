
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


import tkinter as tk


def cerrar_ventana():
    ventana_noticia.destroy()

def mostrar_noticia(titulo, resumen, contenido):
    global ventana_noticia

    ventana_noticia = tk.Tk()
    ventana_noticia.title("Noticia")

    # Título de la noticia
    etiqueta_titulo = tk.Label(ventana_noticia, text=titulo, font=("Helvetica", 16, "bold"))
    etiqueta_titulo.pack(pady=10)

    # Resumen de la noticia
    etiqueta_resumen = tk.Label(ventana_noticia, text=resumen, wraplength=400)
    etiqueta_resumen.pack(pady=10)

    # Contenido de la noticia
    etiqueta_contenido = tk.Label(ventana_noticia, text=contenido, wraplength=400)
    etiqueta_contenido.pack(pady=10)

    # Botón de cierre
    boton_cerrar = tk.Button(ventana_noticia, text="Cerrar", command=cerrar_ventana)
    boton_cerrar.pack(pady=10)

    # Iniciar bucle principal de la ventana de la noticia
    ventana_noticia.mainloop()



# Ejemplo de uso
titulo_noticia = "Título de la noticia"
resumen_noticia = "Resumen de la noticia"
contenido_noticia = "Contenido de la noticia"

mostrar_noticia(titulo_noticia, resumen_noticia, contenido_noticia)




"""import tkinter as tk
from PIL import ImageTk, Image
import requests
from io import BytesIO

def cerrar_ventana():
    ventana_noticia.destroy()

def mostrar_noticia(titulo, resumen, imagen_url, contenido):
    global ventana_noticia
    #global imagen_url
    #magen_url=url
    print("La url es:",imagen_url)

    ventana_noticia = tk.Tk()
    ventana_noticia.title("Noticia")

    # Título de la noticia
    etiqueta_titulo = tk.Label(ventana_noticia, text=titulo, font=("Helvetica", 16, "bold"))
    etiqueta_titulo.pack(pady=10)

    # Resumen de la noticia
    etiqueta_resumen = tk.Label(ventana_noticia, text=resumen, wraplength=400)
    etiqueta_resumen.pack(pady=10)



    # Descargar la imagen desde la URL
    response = requests.get(imagen_url)
    imagen_data = response.content
    imagen = Image.open(BytesIO(imagen_data))

    # Mostrar la imagen de la noticia
    imagen_noticia = ImageTk.PhotoImage(imagen)
    etiqueta_imagen = tk.Label(ventana_noticia, image=imagen_noticia)
    etiqueta_imagen.pack(pady=10)

    # Contenido de la noticia
    etiqueta_contenido = tk.Label(ventana_noticia, text=contenido, wraplength=400)
    etiqueta_contenido.pack(pady=10)

    # Botón de cierre
    boton_cerrar = tk.Button(ventana_noticia, text="Cerrar", command=cerrar_ventana)
    boton_cerrar.pack(pady=10)

    # Iniciar bucle principal de la ventana de la noticia
    ventana_noticia.mainloop()

# Ejemplo de uso
titulo_noticia = "Título de la noticia"
resumen_noticia = "Resumen de la noticia"
global imagen_url
imagen_url = "https://media.ambito.com/p/a44de4200a4c87a01ed73995ca711d24/adjuntos/239/imagenes/040/173/0040173506/billeteras-digitalesjpg.jpg"  # URL de la imagen
contenido_noticia = "Contenido de la noticia"

mostrar_noticia(titulo_noticia, resumen_noticia, imagen_url, contenido_noticia)
"""
