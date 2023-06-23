
import tkinter as tk
from tkinter import scrolledtext
import funciones

def cerrar_ventana():
    ventana_noticia.destroy()



def abrir_estadisticas():
    global listfrecc2
    funciones.graficar_barras(listfrecc2)
    funciones.graficar_torta(listfrecc2)


def listas_frecuencias():

    ventanafreccuencia=tk.Tk()
    ventanafreccuencia.title("Listas de Frecuencias")

    global listfrecc

    resultado = funciones.obtener_palabras_frecuentes_todas(listfrecc)


    # Crear el Text widget
    textboxfrecc = scrolledtext.ScrolledText(ventanafreccuencia, height=10, width=45)
    textboxfrecc.pack()
    


    
    texto_resultado = ""
    for palabra, frecuencia in resultado:
        texto_resultado += f"Palabra: {palabra}, Frecuencia: {frecuencia}\n"

    textboxfrecc.delete("1.0", tk.END)  # Limpiar el contenido actual del textbox
    textboxfrecc.insert(tk.END, texto_resultado)


    ventanafreccuencia.mainloop()




def mostrar_noticia(titulo, resumen, contenido):
    global ventana_noticia

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
