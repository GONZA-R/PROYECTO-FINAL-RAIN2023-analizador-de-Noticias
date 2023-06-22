###########################
#Borrar pantalla
import os
def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')
#############################


import re
def eliminar_caracteres(cadena):
    caracteres = ['"', "'", ",", ";",":",".","-","“","”","°","(",")","/","[","]","$","?","¿","¡","!","%","‘","’","–","—"]
    for caracter in caracteres:
        cadena = cadena.replace(caracter, "")
    return cadena

def eliminar_numeros_lista(lista):
    patron_numeros = r'\d+(?:,\d+)*(?:\.\d+)?'
    lista_sin_numeros = [re.sub(patron_numeros, '', cadena).strip() for cadena in lista]
    return lista_sin_numeros

def eliminar_caracteres_unicos(lista):
    lista_filtrada = [palabra for palabra in lista if len(set(palabra)) > 1]
    return lista_filtrada


from nltk.corpus import stopwords

def eliminar_stopwords(lista_palabras):
    # Obtenemos las stopwords para español
    stop_words_es = set(stopwords.words('spanish'))
    
    stop_words_personalizadas = ['cada','este','cómo']
    # Combinamos ambos conjuntos de stopwords
    stop_words = stop_words_es.union(stop_words_personalizadas)

    # Eliminamos las stopwords de la lista de palabras
    lista_sin_stopwords = [palabra for palabra in lista_palabras if not palabra.lower() in stop_words]
    
    return lista_sin_stopwords

from unidecode import unidecode
def procesar_lista(lista):
    resultado = []
    for elemento in lista:
        elemento = elemento.lower()
        elemento = elemento.replace(" ", "-")
        elemento = unidecode(elemento)
        resultado.append(elemento)
    return resultado



def crear_indice_invertido(noticias):
    indice = {}
    for i, noticia in enumerate(noticias):
        titulo = noticia["titulo"]
        resumen = noticia["resumen"]
        contenido = noticia["contenido"]
        sitio = noticia["sitio"]
        url_sitio = noticia["url_sitio"]
        seccion = noticia["seccion"]
        link = noticia["link"]

        # Agregar términos del título al índice invertido
        for palabra in titulo.split():
            if palabra not in indice:
                indice[palabra] = []
            indice[palabra].append(noticia)

        # Agregar términos del resumen al índice invertido
        for palabra in resumen.split():
            if palabra not in indice:
                indice[palabra] = []
            indice[palabra].append(noticia)

        # Agregar términos del contenido al índice invertido
        for frase in contenido:
            for palabra in frase.split():
                if palabra not in indice:
                    indice[palabra] = []
                indice[palabra].append(noticia)

        # Agregar términos de la sección al índice invertido
        for palabra in seccion.split():
            if palabra not in indice:
                indice[palabra] = []
            indice[palabra].append(noticia)

        # Agregar términos del sitio al índice invertido
        for palabra in sitio.split():
            if palabra not in indice:
                indice[palabra] = []
            indice[palabra].append(noticia)

    return indice

import tkinter as tk
from tkinter import messagebox

def buscar_noticias(indice, palabra_clave):
    if palabra_clave in indice:
        return indice[palabra_clave]
    else:
        messagebox.showinfo("Alerta", "No se encontraron resultados con esa busqueda.")
        return []



def eliminar_elementos_repetidos(lista):
    lista_sin_repetidos = []
    for elemento in lista:
        if elemento not in lista_sin_repetidos:
            lista_sin_repetidos.append(elemento)
    return lista_sin_repetidos


def buscar_y_guardar_noticias(indice_invertido,palabra_clave):
    #palabra_clave = input("Ingrese una palabra clave para buscar noticias: ")
    palabra_clave = palabra_clave.lower()
    noticias_relacionadas = buscar_noticias(indice_invertido, palabra_clave)
    noticias_relacionadas = eliminar_elementos_repetidos(noticias_relacionadas)

    noticias_diccionario = {}

    if noticias_relacionadas:
        print("\nNoticias relacionadas con la palabra clave:", palabra_clave)
        for i, noticia in enumerate(noticias_relacionadas):
            noticia_diccionario = {
                "titulo": noticia["titulo"],
                "resumen": noticia["resumen"],
                "contenido": noticia["contenido"],
                "sitio": noticia["sitio"],
                "url_sitio": noticia["url_sitio"],
                "seccion": noticia["seccion"],
                "link": noticia["link"]
            }
            noticias_diccionario[i] = noticia_diccionario

        return noticias_diccionario
    else:
        print("No se encontraron noticias relacionadas con la palabra clave:", palabra_clave)
        return noticias_diccionario


################
#posible funcion para mostrar noticias

def imprimir_elemento(noticias):
    elemento = noticias[0]
    print('\n' + elemento['titulo'])
    print('\n' + elemento['resumen'])
    print('\n')
    print(elemento['contenido'])
    print('\n')
    print(elemento['seccion'])
    print('\n')
    print(elemento['sitio'])
    print('\n')
    print(elemento['url_sitio'])
    print('\n')
    print(elemento['link'])



url_bases=['https://www.ambito.com','https://www.eldestapeweb.com','https://www.eldiarioar.com/',
           'https://www.perfil.com/','https://www.eltribuno.com','https://www.infobae.com','https://www.lanacion.com.ar',
           'https://www.pagina12.com.ar','https://www.tiempoar.com.ar','https://tn.com.ar']
url_bases = sorted(url_bases)



def procesar_noticias(list_dic_noticias):
    for noticia in list_dic_noticias:
        resumen_actual = noticia['titulo']
        resumen_actual = resumen_actual + noticia['resumen']

        nuevo_resumen = noticia['contenido']
        nuevo_resumen = ' '.join(nuevo_resumen)
        
        nuevo_resumen = resumen_actual + nuevo_resumen
        nuevo_resumen = eliminar_caracteres(nuevo_resumen)
        nuevo_resumen = nuevo_resumen.split()
        nuevo_resumen = eliminar_numeros_lista(nuevo_resumen)
        nuevo_resumen = [elemento.lower() for elemento in nuevo_resumen]
        nuevo_resumen = list(filter(None, nuevo_resumen))
        nuevo_resumen = eliminar_stopwords(nuevo_resumen)
        nuevo_resumen = eliminar_caracteres_unicos(nuevo_resumen)
        noticia['contenido'] = nuevo_resumen
