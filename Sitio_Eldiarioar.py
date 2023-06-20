
import funciones
#####################################################################################################

import requests
from bs4 import BeautifulSoup
def conseguir_url(url,textobusq):
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            urls_noticias=[]
            divs = soup.find_all('div', {'class': 'row'}) #Segun la estructura html de la pagina
            #los links a necesitar se encuentran en la class = d23_content-section
            for div in divs:
                links = div.find_all('a')
                for link in links:
                    href = link.get('href')
                    #if href and 'autores' not in href:
                    if href and href.startswith('https://www.eldiarioar.com/'+textobusq+'/') and href != 'https://www.eldiarioar.com/'+textobusq+'/':
                        urls_noticias.append(href)
            return urls_noticias
#####################################################################################################
import requests
from bs4 import BeautifulSoup

 
def web_scraping(links,textobusq,url_base):
    noticias = []
    for link in links:
        url = link
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')


        titulo = soup.find('div', class_='news-header')
        if titulo:
                titulo = titulo.find('h1').text.strip()
        else:
                titulo = ""  # O cualquier valor por defecto que desees asignar si no se encuentra el elemento



        resumen = soup.find('div', class_='news-header')
        if resumen is not None:
            resumen = resumen.find('h2')
            if resumen is not None:
                resumen = resumen.text.strip()
            else:
                resumen = ""
        else:
            resumen = ""

        div_contenido = soup.find('div', class_='partner-wrapper article-page__body-row')


        # Crear una lista para almacenar los párrafos
            
        lista_parrafos = []

        if div_contenido:

            div_twitters = div_contenido.find_all('figure', class_='embed-container--type-twitter')
            for div_twitter in div_twitters:
                div_twitter.decompose()

            # Buscar todos los elementos <p> dentro del div
            parrafos = div_contenido.find_all('p')

            # Recorrer los elementos <p> y obtener el texto de cada uno
            for parrafo in parrafos:
                texto = parrafo.get_text()
                lista_parrafos.append(texto)

        else:
            print("")
        # Diccionario con cada elemento de la pagina a consultar 
        noticias.append({'titulo': titulo,'resumen': resumen, 'contenido': lista_parrafos,'sitio':'El Diario AR','url_sitio':url_base,'seccion':textobusq,'link':link}) 

    return noticias
#####################################################################################################

listdiv = [
    'Política',
    'Economía',
    'Sociedad',
    'Mundo',
    'Latinoamérica',
    'Deportes',
    'Cultura',
    'Medios',
    'Tecnología',
    'Servicios',
    'Conexiones',
    'Mejor vivir'
]

listdiv=funciones.procesar_lista(listdiv)


def obtener_lista_url_completa(url_base):
    lista_url_completa = []
    textobusq=""
    textobusq = input('\nIngrese la sección de noticias: ')###Es con el item selecionado
    url=(url_base+textobusq+'/')
    lista_de_noticias = conseguir_url(url, textobusq)
    lista_de_noticias = list(set(lista_de_noticias))
    lista_de_noticias = [noticia for noticia in lista_de_noticias if noticia is not None]
    lista_de_noticias.sort()
    lista_url_completa.extend(lista_de_noticias)
    return lista_url_completa,textobusq



url_base = 'https://www.eldiarioar.com/'

lista_url_completa,textobusq = obtener_lista_url_completa(url_base)

list_dic_noticias=web_scraping(lista_url_completa,textobusq,url_base)#Aqui se llama a la funcion que se encarga de traer los titulos,resumenes

funciones.procesar_noticias(list_dic_noticias)

indice_invertido = funciones.crear_indice_invertido(list_dic_noticias)

funciones.buscar_y_mostrar_noticias(indice_invertido)



