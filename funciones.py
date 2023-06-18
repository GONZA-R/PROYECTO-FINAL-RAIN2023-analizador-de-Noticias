###########################
#Borrar pantalla
import os
def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')
#############################


import re
def eliminar_caracteres(cadena):
    caracteres = ['"', "'", ",", ";",":",".","-","“","”","°","(",")","/","[","]","$","?","¿","¡","!","%","‘","’"]
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