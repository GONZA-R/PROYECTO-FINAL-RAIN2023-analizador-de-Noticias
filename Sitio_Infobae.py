import funciones
import requests
from bs4 import BeautifulSoup
#####################################################################################################
def conseguir_url(url,textobusq):
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            urls_noticias=[]
            divs = soup.find_all('div', {'class': 'd23_content-section'}) #Segun la estructura html de la pagina
            #los links a necesitar se encuentran en la class = d23_content-section
            for div in divs:
                links = div.find_all('a')
                for link in links:
                    href = link.get('href')
                    if href and (textobusq+'/2023') in href:
                        urls_noticias.append(href)
            return urls_noticias
#####################################################################################################


import requests
from bs4 import BeautifulSoup

def web_scrapping(links,textobusq,url_base):
    noticias = []
    for link in links:
            
        url = link
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
            
        # Obtener título de la noticia

        titulo = soup.find('div', class_='d23-article-header')
        if titulo:
                titulo = titulo.find('h1').text.strip()
        else:
                titulo = ""  # O cualquier valor por defecto que desees asignar si no se encuentra el elemento


        #obtener subtitulo de la noticia
        resumen = soup.find('div', class_='d23-article-header')
        if resumen:
                resumen = resumen.find('h2').text.strip()
        else:
            resumen = ""  # O cualquier valor por defecto que desees asignar si no se encuentra el elemento

        
        # Obtener contenido de la noticia
        div_contenido = soup.find('div', class_='d23_content-section')


        # Crear una lista para almacenar los párrafos
            
        lista_parrafos = []

        if div_contenido:

            # Buscar todos los elementos <p> dentro del div
            parrafos = div_contenido.find_all('p')

            # Recorrer los elementos <p> y obtener el texto de cada uno
            import re

            for parrafo in parrafos:
                texto = parrafo.get_text()
                lista_parrafos.append(texto)

        else:
            print("")
        
        # Diccionario con cada elemento de la pagina a consultar
        noticias.append({'titulo': titulo,'resumen': resumen, 'contenido': lista_parrafos,'sitio':'Infobae','url_sitio':url_base,'seccion':textobusq,'link':link}) 

    
    return noticias


def web_scrapping_div(links):
    elementodiv=[]
    url = links
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    div_contenido = soup.find_all('div', class_='dropdown')
    listdiv = []
    if div_contenido:
        for div_element in div_contenido:
            elementodiv = div_element.find('a')
            texto = elementodiv.get_text(strip=True)
            listdiv.append(texto)
    else:
            print("No se encontró el div de contenido.")
    listdiv.remove('Últimas Noticias')
    listdiv=funciones.procesar_lista(listdiv)
    return listdiv


def obtener_lista_url_completa(url_base):
    lista_url_completa = []
    textobusq=""
    textobusq = input('\nIngrese la sección de noticias: ')###Es con el item selecionado
    url = url_base+'/'+textobusq+'/'
    lista_de_noticias = conseguir_url(url, textobusq)
    lista_de_noticias = list(set(lista_de_noticias))
    lista_de_noticias.sort()
    lista_url_completa = [url_base + noticia for noticia in lista_de_noticias]
    return lista_url_completa,textobusq



url_base = 'https://www.infobae.com'

lista_url_completa,textobusq = obtener_lista_url_completa(url_base)

listdiv=web_scrapping_div(url_base)

list_dic_noticias=web_scrapping(lista_url_completa,textobusq,url_base)#Aqui se llama a la funcion que se encarga de traer los titulos,resumenes

funciones.procesar_noticias(list_dic_noticias)

indice_invertido = funciones.crear_indice_invertido(list_dic_noticias)

funciones.buscar_y_mostrar_noticias(indice_invertido)

