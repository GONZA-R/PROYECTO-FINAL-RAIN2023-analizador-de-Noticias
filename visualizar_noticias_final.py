
import tkinter as tk
from tkinter import scrolledtext
import funciones

def cerrar_ventana():
    ventana_noticia.destroy()



def abrir_estadisticas():
    global listfrecc2
    funciones.graficar_barras(listfrecc2)
    funciones.graficar_torta(listfrecc2)

    
###################################333
def obtener_palabra_seleccionada(event):
    global textboxfrecc
    if textboxfrecc.tag_ranges(tk.SEL):
        palabra_seleccionada = textboxfrecc.get(tk.SEL_FIRST, tk.SEL_LAST)
        resaltar_palabra(palabra_seleccionada)


import re

def resaltar_palabra(palabra_seleccionada):
    global texto_contenido
    try:
        if palabra_seleccionada:
            contenido_resaltado = texto_contenido.get("1.0", "end")
            #contenido_resaltado = contenido_resaltado.replace(palabra_seleccionada, f"{palabra_seleccionada}", 1)
            contenido_resaltado = re.sub(re.escape(palabra_seleccionada), f"{palabra_seleccionada}", contenido_resaltado, flags=re.IGNORECASE)

            texto_contenido.delete("1.0", "end")
            texto_contenido.insert("1.0", contenido_resaltado)
            inicio = "1.0"
            while True:
                inicio = texto_contenido.search(palabra_seleccionada, inicio, "end")
                if not inicio:
                    break
                fin = f"{inicio}+{len(palabra_seleccionada)}c"
                texto_contenido.tag_add("highlight", inicio, fin)
                inicio = fin
    except tk.TclError:
        pass
#########################################



def listas_frecuencias():
    global textboxfrecc################

    ventanafreccuencia=tk.Tk()
    ventanafreccuencia.title("Listas de Frecuencias")

    global listfrecc

    resultado = funciones.obtener_palabras_frecuentes_todas(listfrecc)


    # Crear el Text widget
    textboxfrecc = scrolledtext.ScrolledText(ventanafreccuencia, height=10, width=45)
    textboxfrecc.pack()
    
    
    texto_resultado = ""
    for palabra, frecuencia in resultado:
        texto_resultado += f"Palabra: {palabra} , Frecuencia: {frecuencia}\n"

    textboxfrecc.delete("1.0", tk.END)  # Limpiar el contenido actual del textbox
    textboxfrecc.insert(tk.END, texto_resultado)

    textboxfrecc.bind("<Button-1>", obtener_palabra_seleccionada) ########


    ventanafreccuencia.mainloop()


from datetime import datetime

def mostrar_noticia(titulo, resumen, contenido):
    global ventana_noticia
    global texto_contenido #########

    ventana_noticia = tk.Tk()
    ventana_noticia.title("Noticia")

    # Establecer el tamaño de la ventana
    ventana_noticia.geometry("900x500")  # Cambia las dimensiones según tus necesidades

    ventana_noticia.configure(bg="lightblue")


    etiqueta_titulo = tk.Label(ventana_noticia, text=titulo, font=("Helvetica", 16, "bold"))
    etiqueta_titulo.pack(pady=10)

    etiqueta_resumen = tk.Label(ventana_noticia, text=resumen, wraplength=400)
    etiqueta_resumen.pack(pady=10)

    texto_contenido = scrolledtext.ScrolledText(ventana_noticia, wrap=tk.WORD, width=90, height=12)
    texto_contenido.insert(tk.INSERT, contenido)
    texto_contenido.pack(pady=10)


    texto_contenido.tag_configure("highlight", background="yellow")#######################3

    


    boton_cerrar = tk.Button(ventana_noticia, text="Cerrar", command=cerrar_ventana)
    boton_cerrar.place(x=100, y=350)


    boton_estadistica = tk.Button(ventana_noticia, text="Estadisticas", command=abrir_estadisticas)
    boton_estadistica.place(x=350, y=350)

    boton_listas_frecc = tk.Button(ventana_noticia, text="Frecuencias", command=listas_frecuencias)
    boton_listas_frecc.place(x=220, y=350)

    global listfrecc
    listfrecc=funciones.procesar_noticias_freccuencia(contenido)


    global listfrecc2
    listfrecc2=funciones.obtener_palabras_frecuentes(listfrecc)

    
    ventana_noticia.mainloop()
