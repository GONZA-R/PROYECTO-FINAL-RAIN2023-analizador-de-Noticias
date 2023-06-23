import funciones
#####################################################################################################

import requests
from bs4 import BeautifulSoup
def conseguir_url(url,textobusq):
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            urls_noticias=[]
            divs = soup.find_all('div', {'class': 'sidebar__main'}) #Segun la estructura html de la pagina
            #los links a necesitar se encuentran en la class = d23_content-section
            for div in divs:
                links = div.find_all('a')
                for link in links:
                    href = link.get('href')
                    if href  and textobusq+'/' in href and not href.startswith('https://www.lanacion.com.ar/'+textobusq):
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
        
        titulo = soup.find('h1', class_='com-title --font-primary --sixxl --font-extra')
        if titulo:
            titulo = titulo.text.strip()
        else:
            titulo = ""  # O cualquier valor por defecto que desees asignar si no se encuentra el elemento
        #obtener subtitulo de la noticia
        resumen = soup.find('h2', class_='com-subhead --bajada --m-xs-')

        if resumen:
            resumen = resumen.text.strip()
        else:
            resumen = ""  # O cualquier valor por defecto que desees asignar si no se encuentra el elemento

        div_contenido = soup.find('div', class_='col-deskxl-10 offset-deskxl-1 col-desksm-11')
        # Crear una lista para almacenar los párrafos   
        lista_parrafos = []

        if div_contenido:
            # Buscar todos los elementos <p> dentro del div
            parrafos = div_contenido.find_all('p')

            # Recorrer los elementos <p> y obtener el texto de cada uno
            for parrafo in parrafos:
                texto = parrafo.get_text()
                lista_parrafos.append(texto)
            pass

        else:
            print("")
        # Diccionario con cada elemento de la pagina a consultar
        noticias.append({'titulo': titulo,'resumen': resumen, 'contenido': lista_parrafos,'sitio':'La Nacion','url_sitio':url_base,'seccion':textobusq,'link':link}) 

    return noticias


listdiv= [
    'Tránsito y transporte',
    'Clima',
    'Política',
    'Economía',
    'Dólar Hoy',
    'Propiedades',
    'El Mundo',
    'Sociedad',
    'Buenos Aires',
    'Seguridad',
    'Educación',
    'Cultura',
    'Comunidad',
    'Salud',
    'Ciencia',
    'Deportes',
    'Turismo',
    'Tecnologia'
]
listdiv=funciones.procesar_lista(listdiv)


def obtener_lista_url_completa(url_base,textobusq):
    lista_url_completa = []
    #textobusq=""
    #textobusq = input('\nIngrese la sección de noticias: ')###Es con el item selecionado
    url=url_base+'/'+textobusq+'/'
    lista_de_noticias = conseguir_url(url,textobusq)
    lista_de_noticias = list(set(lista_de_noticias))
    lista_de_noticias.sort()
    lista_url_completa = [url_base + noticia for noticia in lista_de_noticias]
    patron = 'https://www.lanacion.com.ar/'+textobusq+'/'
    lista_url_completa= [url for url in lista_url_completa if url.startswith(patron)]
    return lista_url_completa,textobusq


"""
url_base = 'https://www.lanacion.com.ar'

lista_url_completa,textobusq = obtener_lista_url_completa(url_base)

list_dic_noticias=web_scraping(lista_url_completa,textobusq,url_base)#Aqui se llama a la funcion que se encarga de traer los titulos,resumenes

funciones.procesar_noticias(list_dic_noticias)

indice_invertido = funciones.crear_indice_invertido(list_dic_noticias)

funciones.buscar_y_mostrar_noticias(indice_invertido)
"""



