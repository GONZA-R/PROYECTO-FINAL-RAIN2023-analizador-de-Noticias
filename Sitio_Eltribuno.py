import funciones
#####################################################################################################

import requests
from bs4 import BeautifulSoup
def conseguir_url(url):
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            urls_noticias=[]
            divs = soup.find_all('div', {'class': 'sitio'}) #Segun la estructura html de la pagina
            #los links a necesitar se encuentran en la class = d23_content-section
            for div in divs:
                links = div.find_all('a')
                for link in links:
                    href = link.get('href')
                    if href and 'ttag' not in href:
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


        titulo = soup.find('div', class_='article-info-wrapper')
        if titulo:
                titulo = titulo.find('h1').text.strip()
        else:
                titulo = ""  # O cualquier valor por defecto que desees asignar si no se encuentra el elemento


        #obtener subtitulo de la noticia
        resumen = soup.find('p', class_='preview newDetailTextChange')
        if resumen:
                div_fecha = resumen.find('span', class_='detail-date')
                if div_fecha:
                    div_fecha.extract()  # Eliminar el div "notapropia" del árbol del documento
                
                resumen = resumen.text.strip()
        else:
            resumen = ""  # O cualquier valor por defecto que desees asignar si no se encuentra el elemento
       

        div_contenido = soup.find('div', class_='note-body newDetailTextChange clearfix')


        # Crear una lista para almacenar los párrafos
            
        lista_parrafos = []

        if div_contenido:

            div_notapropia = div_contenido.find('div', class_='notapropia')
            if div_notapropia:
                div_notapropia.extract()  # Eliminar el div "notapropia" del árbol del documento

            # Buscar todos los elementos <p> dentro del div
            parrafos = div_contenido.find_all('p')

            # Recorrer los elementos <p> y obtener el texto de cada uno
            for parrafo in parrafos:
                texto = parrafo.get_text()
                lista_parrafos.append(texto)

        else:
            print("No se encontró el div de contenido.")
   
        
        # Diccionario con cada elemento de la pagina a consultar
        noticias.append({'titulo': titulo,'resumen': resumen, 'contenido': lista_parrafos,'sitio':'El Tribuno Jujuy','url_sitio':url_base,'seccion':textobusq,'link':link}) 

        
    return noticias



#####################################################################################################

listdiv=['Economia','Politica','Informacion General','Internacional', 'Nacional', 'Policiales', 'Municipios', 'Espectáculos', 'Tecnología'
         , 'Mujer', 'Tendencia', 'Vida y Tendencia', 'Sociedad', 'Onda Estudiantil', 'Salud']

listdiv=funciones.procesar_lista(listdiv)

def obtener_lista_url_completa(url_base,textobusq):
    lista_url_completa = []
    #textobusq=""
    #textobusq = input('\nIngrese la sección de noticias: ')###Es con el item selecionado
    url=url_base+'/jujuy/seccion/'+textobusq+'/'
    lista_de_noticias = conseguir_url(url)
    lista_de_noticias = list(set(lista_de_noticias))
    lista_de_noticias = [noticia for noticia in lista_de_noticias if noticia is not None]
    lista_de_noticias.sort()
    lista_url_completa = [url_base + noticia for noticia in lista_de_noticias]
    return lista_url_completa,textobusq

"""
url_base = 'https://www.eltribuno.com'

lista_url_completa,textobusq = obtener_lista_url_completa(url_base)

list_dic_noticias=web_scraping(lista_url_completa,textobusq,url_base)#Aqui se llama a la funcion que se encarga de traer los titulos,resumenes

funciones.procesar_noticias(list_dic_noticias)

indice_invertido = funciones.crear_indice_invertido(list_dic_noticias)

funciones.buscar_y_mostrar_noticias(indice_invertido)
"""




