import tkinter as tk
from tkinter import ttk, scrolledtext


    

def abrir_ventana_principal():
    import tkinter as tk
    from tkinter import ttk, scrolledtext

    # Opciones de la primera lista desplegable
    from funciones2 import url_bases
    opciones_lista1 = list(url_bases)

    # Diccionario de opciones para la segunda lista desplegable
    opciones_dict = {}

    def seleccionar_opcion_lista1(event):
        # Obtener la opción seleccionada de la primera lista
        opcion_seleccionada = combo_lista1.get()

        global gurlbase
        gurlbase=opcion_seleccionada


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
            import Sitio_Ambitos2
            opciones_dict[opcion_seleccionada] = Sitio_Ambitos2.web_scrapping_div(opcion_seleccionada)

        elif opcion_seleccionada == "https://www.eldestapeweb.com":
            import Sitio_Eldestape2
            opciones_dict[opcion_seleccionada] = Sitio_Eldestape2.web_scrapping_div(opcion_seleccionada)

        elif opcion_seleccionada == "Opción 3":
            opciones_dict[opcion_seleccionada] = ["Elemento 3-1", "Elemento 3-2", "Elemento 3-3"]

        # Devolver los elementos correspondientes para la segunda lista
        return opciones_dict.get(opcion_seleccionada, [])


    def enviar_opcion_lista2():
        # Obtener la opción seleccionada de la segunda lista
        opcion_seleccionada = combo_lista2.get()

        # Llamar a la función deseada con la opción seleccionada
        mi_funcion(opcion_seleccionada)



    def mi_funcion(opcion_seleccionada):
        # Aquí puedes realizar las acciones que desees con la opción seleccionada

        global gurlbase

        if gurlbase == "https://www.ambito.com":
            import Sitio_Ambitos2
            listurl, textobusq = Sitio_Ambitos2.obtener_lista_url_completa(gurlbase, opcion_seleccionada)
            
            llenartextboxlisturl(listurl,textobusq)
            

        elif gurlbase == "https://www.eldestapeweb.com":
            import Sitio_Eldestape2
            listurl, textobusq = Sitio_Eldestape2.obtener_lista_url_completa(gurlbase, opcion_seleccionada)
            llenartextboxlisturl(listurl,textobusq)



    def llenartextboxlisturl(listurl,opcion_seleccionada):
        global glisturl
        glisturl=listurl
        global gtextbusq
        gtextbusq=opcion_seleccionada
        # Borrar el contenido actual del TextBox
        text_box.delete("1.0", tk.END)
        # Llenar el TextBox con la nueva lista
        for item in listurl:
            text_box.insert(tk.END, item + "\n\n")




    def enviar_seleccion(event):
        # Verificar si hay texto seleccionado en el TextBox
        if text_box.tag_ranges(tk.SEL):
            # Obtener el texto seleccionado del TextBox
            texto_seleccionado = text_box.get(tk.SEL_FIRST, tk.SEL_LAST)
            # Llamar a la función deseada con el texto seleccionado
            otra_funcion2(texto_seleccionado)

    def otra_funcion2(texto_seleccionado):
        # Aquí puedes realizar las acciones que desees con el texto seleccionado
        print("Texto seleccionado:", texto_seleccionado)
        import webbrowser
        webbrowser.open(texto_seleccionado)
        


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

    # Crear botón "Enviar"
    btn_enviar = ttk.Button(ventana, text="Obtener URLs", command=enviar_opcion_lista2)
    btn_enviar.pack(pady=10)

    # Crear TextBox
    text_box = scrolledtext.ScrolledText(ventana, width=70, height=20)
    text_box.pack(padx=10, pady=10)

    # Configurar evento de selección en el TextBox
    text_box.bind("<ButtonRelease-1>", enviar_seleccion)

    ################################################################################
    # Variable global para almacenar el valor cargado
    global valor_cargado
    valor_cargado = ""

    # Función para obtener el valor del cuadro de diálogo de entrada
    def obtener_valor():
        valor = cuadro_texto.get()
        cargar_valor(valor)

    # Función para cargar el valor en la variable global y en el cuadro de texto de salida
    def cargar_valor(valor):
        global valor_cargado  # Acceder a la variable global
        valor_cargado = valor
        
        otra_funcion3()

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
    cuadro_salida = scrolledtext.ScrolledText(ventana, height=20, width=70)
    cuadro_salida.pack()

    # Función que utiliza el valor cargado en la variable global
    def otra_funcion3():
        global gurlbase
    
        global glisturl

        global gtextbusq

        global valor_cargado

        if gurlbase == "https://www.ambito.com":
            import Sitio_Ambitos2
            list_dicc=Sitio_Ambitos2.web_scraping(glisturl,gtextbusq,gurlbase)
            llenartextboxnoticoincidente(list_dicc)

        elif gurlbase == "https://www.eldestapeweb.com":
            import Sitio_Eldestape2
            list_dicc=Sitio_Eldestape2.web_scraping(glisturl,gtextbusq,gurlbase)
            llenartextboxnoticoincidente(list_dicc)
            



    def llenartextboxnoticoincidente(list_dicc):
        import funciones2
        funciones2.procesar_noticias(list_dicc)
        indice_invertido = funciones2.crear_indice_invertido(list_dicc)
        noticias_diccionario = []
        noticias_diccionario=funciones2.buscar_y_guardar_noticias(indice_invertido,valor_cargado)

        cuadro_salida.delete("1.0", tk.END)  # Borrar contenido actual del cuadro de salida
        
        # Recorrer el diccionario y agregar el título y el enlace al textbox
        for valor in noticias_diccionario.values():
            titulo = valor.get('titulo', '')
            enlace = valor.get('link', '')
            cuadro_salida.insert(tk.END, f"Título: {titulo}\n")
            cuadro_salida.insert(tk.END, f"Enlace: {enlace}\n")
            cuadro_salida.insert(tk.END, "**********************\n")

    ##############################################################################33333


    # Iniciar bucle principal
    ventana.mainloop()

    




def abrir_ventana_bienvenida():
    ventana_bienvenida = tk.Tk()
    ventana_bienvenida.title("Bienvenido")


    # Establecer el tamaño de la ventana
    ventana_bienvenida.geometry("400x300")  # Cambia las dimensiones según tus necesidades


    # Etiqueta de bienvenida
    etiqueta_bienvenida = tk.Label(ventana_bienvenida, text="¡Bienvenido!")
    etiqueta_bienvenida.pack(pady=10)

    # Botón para acceder a la ventana principal
    boton_acceder = tk.Button(ventana_bienvenida, text="Acceder", command=abrir_ventana_principal)
    boton_acceder.pack(pady=10)

    # Iniciar bucle principal de la ventana de bienvenida
    ventana_bienvenida.mainloop()

# Llamar a la función para abrir la ventana de bienvenida

abrir_ventana_bienvenida()
