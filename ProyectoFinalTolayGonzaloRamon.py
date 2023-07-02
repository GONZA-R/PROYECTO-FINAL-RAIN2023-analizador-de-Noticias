import tkinter as tk
from tkinter import ttk, scrolledtext


    

def abrir_ventana_principal():
    
    global ventana_bienvenida
    ventana_bienvenida.destroy()

    import tkinter as tk
    from tkinter import ttk, scrolledtext

    # Opciones de la primera lista desplegable
    from funciones import url_bases
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
            import Sitio_Ambitos
            opciones_dict[opcion_seleccionada] = Sitio_Ambitos.web_scrapping_div(opcion_seleccionada)

        elif opcion_seleccionada == "https://www.eldestapeweb.com":
            import Sitio_Eldestape
            opciones_dict[opcion_seleccionada] = Sitio_Eldestape.web_scrapping_div(opcion_seleccionada)

        elif opcion_seleccionada == "https://www.eldiarioar.com/":
            from Sitio_Eldiarioar import listdiv
            opciones_dict[opcion_seleccionada] = listdiv

        elif opcion_seleccionada == "https://tn.com.ar":
            from Sitio_Tn import listdiv
            opciones_dict[opcion_seleccionada] = listdiv

        elif opcion_seleccionada == "https://www.perfil.com/":
            import Sitio_Elperfil
            opciones_dict[opcion_seleccionada] = Sitio_Elperfil.web_scrapping_div(opcion_seleccionada)

        elif opcion_seleccionada == "https://www.eltribuno.com":
            from Sitio_Eltribuno import listdiv
            opciones_dict[opcion_seleccionada] = listdiv
        
        elif opcion_seleccionada == "https://www.infobae.com":
            import Sitio_Infobae
            opciones_dict[opcion_seleccionada] = Sitio_Infobae.web_scrapping_div(opcion_seleccionada)

        elif opcion_seleccionada == "https://www.lanacion.com.ar":
            from Sitio_Lanacion import listdiv
            opciones_dict[opcion_seleccionada] = listdiv
        
        elif opcion_seleccionada == "https://www.pagina12.com.ar":
            import Sitio_Pagina12
            opciones_dict[opcion_seleccionada] = Sitio_Pagina12.web_scrapping_div(opcion_seleccionada)

        elif opcion_seleccionada == "https://www.tiempoar.com.ar":
            from Sitio_Tiempoar import listdiv
            opciones_dict[opcion_seleccionada] = listdiv




        




            

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
            import Sitio_Ambitos
            listurl, textobusq = Sitio_Ambitos.obtener_lista_url_completa(gurlbase, opcion_seleccionada) 
            llenartextboxlisturl(listurl,textobusq)
            

        elif gurlbase == "https://www.eldestapeweb.com":
            import Sitio_Eldestape
            listurl, textobusq = Sitio_Eldestape.obtener_lista_url_completa(gurlbase, opcion_seleccionada)
            llenartextboxlisturl(listurl,textobusq)

        elif gurlbase == "https://www.eldiarioar.com/":
            import Sitio_Eldiarioar
            listurl, textobusq = Sitio_Eldiarioar.obtener_lista_url_completa(gurlbase, opcion_seleccionada)
            llenartextboxlisturl(listurl,textobusq)

        elif gurlbase == "https://tn.com.ar":
            import Sitio_Tn
            listurl, textobusq = Sitio_Tn.obtener_lista_url_completa(gurlbase, opcion_seleccionada)
            llenartextboxlisturl(listurl,textobusq)

        elif gurlbase == "https://www.perfil.com/":
            import Sitio_Elperfil
            listurl, textobusq = Sitio_Elperfil.obtener_lista_url_completa(gurlbase, opcion_seleccionada)
            llenartextboxlisturl(listurl,textobusq)

        elif gurlbase == "https://www.eltribuno.com":
            import Sitio_Eltribuno
            listurl, textobusq = Sitio_Eltribuno.obtener_lista_url_completa(gurlbase, opcion_seleccionada)
            llenartextboxlisturl(listurl,textobusq)

        elif gurlbase == "https://www.infobae.com":
            import Sitio_Infobae
            listurl, textobusq = Sitio_Infobae.obtener_lista_url_completa(gurlbase, opcion_seleccionada)
            llenartextboxlisturl(listurl,textobusq)
        
        elif gurlbase == "https://www.lanacion.com.ar":
            import Sitio_Lanacion
            listurl, textobusq = Sitio_Lanacion.obtener_lista_url_completa(gurlbase, opcion_seleccionada)
            llenartextboxlisturl(listurl,textobusq)
        
        elif gurlbase == "https://www.pagina12.com.ar":
            import Sitio_Pagina12
            listurl, textobusq = Sitio_Pagina12.obtener_lista_url_completa(gurlbase, opcion_seleccionada)
            llenartextboxlisturl(listurl,textobusq)

        elif gurlbase == "https://www.tiempoar.com.ar":
            import Sitio_Tiempoar
            listurl, textobusq = Sitio_Tiempoar.obtener_lista_url_completa(gurlbase, opcion_seleccionada)
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
        completarNoticia()
        global list_dicc2
        
        for lista in list_dicc2:
            elemento=lista['link']
            if texto_seleccionado==elemento:
                titulo_noticia=lista['titulo']
                resumen_noticia=lista['resumen']
                contenido_noticia=lista['contenido']

        
        list_dicc2=[]

        import visualizar_noticias_final
        visualizar_noticias_final.mostrar_noticia(titulo_noticia, resumen_noticia, contenido_noticia)




    #############################################################################################    
    # Crear ventana
    ventana = tk.Tk()
    ventana.title("NOTICIAS WEB")

    # Establecer el tamaño de la ventana
    ventana.geometry("1100x650")  # Cambia las dimensiones según tus necesidades
    # Cambiar el color de fondo de la ventana
    ventana.configure(bg="lightblue")

    # Crear primera lista desplegable
    label1 = tk.Label(ventana, text="Seleccione un sitio de los diarios digitales")
    label1.place(x=100, y=30)

    combo_lista1 = ttk.Combobox(ventana, values=opciones_lista1,width=28)
    #combo_lista1.pack(pady=10)
    combo_lista1.place(x=100, y=60)
    

    # Configurar evento de selección para la primera lista desplegable
    combo_lista1.bind("<<ComboboxSelected>>", seleccionar_opcion_lista1)

    # Crear segunda lista desplegable
    label2 = tk.Label(ventana, text="Seleccione una seccion de NOTICIAS")
    label2.place(x=100, y=120)
    
    combo_lista2 = ttk.Combobox(ventana,width=28)
    combo_lista2.place(x=100, y=150)

    # Crear botón "Enviar"
    btn_enviar = ttk.Button(ventana, text="Obtener URLs", command=enviar_opcion_lista2)
    btn_enviar.place(x=100, y=200)

    # Crear TextBox
    label3 = tk.Label(ventana, text="Direcciones(Seleccione una para acceder)")
    label3.place(x=370, y=30)
    text_box = scrolledtext.ScrolledText(ventana, width=80, height=12)
    text_box.place(x=370, y=60)

    # Configurar evento de selección en el TextBox
    text_box.bind("<ButtonRelease-1>", enviar_seleccion)

    #####################################################################################################

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

    #########################################################################################################
    # Crear cuadro de texto de entrada
    label4 = tk.Label(ventana, text="Ingrese palabra a consultar")
    label4.place(x=100, y=270)
    cuadro_texto = tk.Entry(ventana)
    cuadro_texto.place(x=100, y=310)

    # Crear botón para obtener el valor del cuadro de texto
    boton_cargar = tk.Button(ventana, text="Buscar", command=obtener_valor)
    boton_cargar.place(x=100, y=350)

    # Crear botón para borrar el contenido del cuadro de texto
    boton_borrar = tk.Button(ventana, text="Borrar", command=borrar_contenido)
    boton_borrar.place(x=160, y=350)

    # Crear cuadro de texto de salida
    label5 = tk.Label(ventana, text="Sitios WEB coincidentes con la consulta (Selecciones uno)")
    label5.place(x=370, y=270)
    cuadro_salida = scrolledtext.ScrolledText(ventana, width=80,height=12)
    cuadro_salida.place(x=370, y=310)


    
    #########################################################################################################

    def completarNoticia():
        global gurlbase
    
        global glisturl

        global gtextbusq

        global list_dicc2

        if gurlbase == "https://www.ambito.com":
            import Sitio_Ambitos
            list_dicc2=Sitio_Ambitos.web_scraping(glisturl,gtextbusq,gurlbase)

        elif gurlbase == "https://www.eldestapeweb.com":
            import Sitio_Eldestape
            list_dicc2=Sitio_Eldestape.web_scraping(glisturl,gtextbusq,gurlbase)

        elif gurlbase == "https://www.eldiarioar.com/":
            import Sitio_Eldiarioar
            list_dicc2=Sitio_Eldiarioar.web_scraping(glisturl,gtextbusq,gurlbase)

        elif gurlbase == "https://tn.com.ar":
            import Sitio_Tn
            list_dicc2=Sitio_Tn.web_scraping(glisturl,gtextbusq,gurlbase)

        elif gurlbase == "https://www.perfil.com/":
            import Sitio_Elperfil
            list_dicc2=Sitio_Elperfil.web_scraping(glisturl,gtextbusq,gurlbase)
        
        elif gurlbase == "https://www.eltribuno.com":
            import Sitio_Eltribuno
            list_dicc2=Sitio_Eltribuno.web_scraping(glisturl,gtextbusq,gurlbase)

        elif gurlbase == "https://www.infobae.com":
            import Sitio_Infobae
            list_dicc2=Sitio_Infobae.web_scrapping(glisturl,gtextbusq,gurlbase)

        elif gurlbase == "https://www.lanacion.com.ar":
            import Sitio_Lanacion
            list_dicc2=Sitio_Lanacion.web_scraping(glisturl,gtextbusq,gurlbase)
        
        elif gurlbase == "https://www.pagina12.com.ar":
            import Sitio_Pagina12
            list_dicc2=Sitio_Pagina12.web_scraping(glisturl,gtextbusq,gurlbase)
        
        elif gurlbase == "https://www.tiempoar.com.ar":
            import Sitio_Tiempoar
            list_dicc2=Sitio_Tiempoar.web_scraping(glisturl,gtextbusq,gurlbase)



    # Función que utiliza el valor cargado en la variable global
    def otra_funcion3():
        global gurlbase
    
        global glisturl

        global gtextbusq

        global valor_cargado

        if gurlbase == "https://www.ambito.com":
            import Sitio_Ambitos
            global list_dicc
            list_dicc=Sitio_Ambitos.web_scraping(glisturl,gtextbusq,gurlbase)
            llenartextboxnoticoincidente(list_dicc)

        elif gurlbase == "https://www.eldestapeweb.com":
            import Sitio_Eldestape
            list_dicc=Sitio_Eldestape.web_scraping(glisturl,gtextbusq,gurlbase)
            llenartextboxnoticoincidente(list_dicc)
        

        elif gurlbase == "https://www.eldiarioar.com/":
            import Sitio_Eldiarioar
            list_dicc=Sitio_Eldiarioar.web_scraping(glisturl,gtextbusq,gurlbase)
            llenartextboxnoticoincidente(list_dicc)
            
        elif gurlbase == "https://tn.com.ar":
            import Sitio_Tn
            list_dicc=Sitio_Tn.web_scraping(glisturl,gtextbusq,gurlbase)
            llenartextboxnoticoincidente(list_dicc)
        
        elif gurlbase == "https://www.perfil.com/":
            import Sitio_Elperfil
            list_dicc=Sitio_Elperfil.web_scraping(glisturl,gtextbusq,gurlbase)
            llenartextboxnoticoincidente(list_dicc)

        elif gurlbase == "https://www.eltribuno.com":
            import Sitio_Eltribuno
            list_dicc=Sitio_Eltribuno.web_scraping(glisturl,gtextbusq,gurlbase)
            llenartextboxnoticoincidente(list_dicc)

        elif gurlbase == "https://www.infobae.com":
            import Sitio_Infobae
            list_dicc=Sitio_Infobae.web_scrapping(glisturl,gtextbusq,gurlbase)
            llenartextboxnoticoincidente(list_dicc)
            
        elif gurlbase == "https://www.lanacion.com.ar":
            import Sitio_Lanacion
            list_dicc=Sitio_Lanacion.web_scraping(glisturl,gtextbusq,gurlbase)
            llenartextboxnoticoincidente(list_dicc)
        
        elif gurlbase == "https://www.pagina12.com.ar":
            import Sitio_Pagina12
            list_dicc=Sitio_Pagina12.web_scraping(glisturl,gtextbusq,gurlbase)
            llenartextboxnoticoincidente(list_dicc)
        
        elif gurlbase == "https://www.tiempoar.com.ar":
            import Sitio_Tiempoar
            list_dicc=Sitio_Tiempoar.web_scraping(glisturl,gtextbusq,gurlbase)
            llenartextboxnoticoincidente(list_dicc)


            



    def llenartextboxnoticoincidente(list_dicc):
        import funciones
        funciones.procesar_noticias(list_dicc)
        indice_invertido = funciones.crear_indice_invertido(list_dicc)
        noticias_diccionario = []
        noticias_diccionario=funciones.buscar_y_guardar_noticias(indice_invertido,valor_cargado)

        cuadro_salida.delete("1.0", tk.END)  # Borrar contenido actual del cuadro de salida
        
        # Recorrer el diccionario y agregar el título y el enlace al textbox
        for valor in noticias_diccionario.values():
            titulo = valor.get('titulo', '')
            enlace = valor.get('link', '')
            cuadro_salida.insert(tk.END, f"Título: {titulo}\n\n")
            cuadro_salida.insert(tk.END, f"Enlace: {enlace}\n\n")
            cuadro_salida.insert(tk.END, "**********************\n")
        # Configurar evento de selección en el TextBox
        cuadro_salida.bind("<ButtonRelease-1>", enviar_seleccion2)


    def enviar_seleccion2(event):
        # Verificar si hay texto seleccionado en el TextBox
        if cuadro_salida.tag_ranges(tk.SEL):
            # Obtener el texto seleccionado del TextBox
            texto_seleccionado = cuadro_salida.get(tk.SEL_FIRST, tk.SEL_LAST)
            # Llamar a la función deseada con el texto seleccionado
            otra_funcion2(texto_seleccionado)


##############################################################################



    # Iniciar bucle principal
    ventana.mainloop()

    


def abrir_ventana_bienvenida():

    global ventana_bienvenida

    ventana_bienvenida = tk.Tk()
    ventana_bienvenida.title("RECUPERACION AVANZADA DE INFORMACION 2023 - GONZALO RAMON TOLAY")

    # Establecer el tamaño de la ventana
    ventana_bienvenida.geometry("900x500")  # Cambia las dimensiones según tus necesidades

 
    # Cambiar el color de fondo de la ventana
    ventana_bienvenida.configure(bg="lightblue")


    # Etiqueta de bienvenida
    etiqueta_bienvenida = tk.Label(ventana_bienvenida, text="NewsXplorer - Sistema de Recuperacion WEB", foreground="red", font=("Arial", 28))
    etiqueta_bienvenida.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

    
    # Botón para acceder a la ventana principal
    boton_acceder = tk.Button(ventana_bienvenida, text="INICIAR",width=10, height=2,borderwidth=2, relief="solid",command=abrir_ventana_principal)
    boton_acceder.place(relx=0.5, rely=0.9, anchor=tk.CENTER)
    

    ###########################3
    from PIL import ImageTk, Image
    # Cargar la imagen
    ruta_imagen = "imagen2.png"  # Reemplaza con la ruta de tu imagen
    imagen = Image.open(ruta_imagen)

    # Redimensionar la imagen
    imagen = imagen.resize((600, 300))

    # Crear un objeto ImageTk para mostrar la imagen en la ventana
    imagen_tk = ImageTk.PhotoImage(imagen)

    # Crear un widget Label para mostrar la imagen
    label_imagen = tk.Label(ventana_bienvenida, image=imagen_tk)
    label_imagen.place(relx=0.5, rely=0.5, anchor=tk.CENTER)



    ########################################3

    # Iniciar bucle principal de la ventana de bienvenida
    ventana_bienvenida.mainloop()



# Llamar a la función para abrir la ventana de bienvenida

abrir_ventana_bienvenida()
